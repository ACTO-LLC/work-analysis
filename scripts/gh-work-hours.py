#!/usr/bin/env python3
"""Estimate work hours from GitHub commit timestamps using the git-hours algorithm.

Uses `gh api` (GitHub CLI) to fetch commits via the Search API, then groups
them into work sessions based on inter-commit gaps.  Zero external dependencies
— stdlib only (requires Python 3.9+ for zoneinfo).

Algorithm
---------
1. Fetch all commits for the author in the date range via GitHub Search API.
2. Sort chronologically across all repos.
3. Walk the timeline — consecutive commits <= max_gap apart belong to the same
   work session; larger gaps start a new session.
4. Each session's duration = (last - first commit) + first_bonus.
5. Sum all sessions for total estimated hours.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


# ── Data fetching ────────────────────────────────────────────────────────────

def fetch_commits(author: str, start: str, end: str, emails: list[str] | None = None) -> list[dict]:
    """Fetch commits from GitHub Search API via `gh api --paginate`."""

    queries: list[str] = [f"author:{author}+author-date:{start}..{end}"]
    for email in (emails or []):
        queries.append(f"author-email:{email}+author-date:{start}..{end}")

    seen_shas: set[str] = set()
    commits: list[dict] = []

    for q in queries:
        cmd = [
            "gh", "api", "--paginate",
            f"search/commits?q={q}&sort=author-date&order=asc&per_page=100",
            "-q", '.items[] | {sha: .sha, date: .commit.author.date, repo: .repository.full_name, message: (.commit.message | split("\n") | .[0])}',
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        except FileNotFoundError:
            print("Error: `gh` CLI not found. Install it from https://cli.github.com/", file=sys.stderr)
            sys.exit(1)
        except subprocess.CalledProcessError as exc:
            print(f"Error calling gh api: {exc.stderr}", file=sys.stderr)
            sys.exit(1)

        for line in result.stdout.strip().splitlines():
            if not line:
                continue
            item = json.loads(line)
            if item["sha"] not in seen_shas:
                seen_shas.add(item["sha"])
                commits.append(item)

    if not commits:
        print("No commits found for the given author and date range.", file=sys.stderr)
        sys.exit(0)

    total_count_warn(author, start, end)
    return commits


def total_count_warn(author: str, start: str, end: str) -> None:
    """Warn if total_count exceeds 1000 (Search API hard limit)."""
    cmd = [
        "gh", "api",
        f"search/commits?q=author:{author}+author-date:{start}..{end}&per_page=1",
        "-q", ".total_count",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        total = int(result.stdout.strip())
        if total > 1000:
            print(
                f"Warning: {total} total commits found but GitHub Search API "
                f"returns at most 1000. Results may be incomplete.",
                file=sys.stderr,
            )
    except Exception:
        pass  # best-effort warning


# ── Timestamp handling ───────────────────────────────────────────────────────

def parse_and_localize(commits: list[dict], tz: ZoneInfo, start: str, end: str) -> list[dict]:
    """Parse ISO timestamps, convert to local tz, and filter by local date."""
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()

    result: list[dict] = []
    for c in commits:
        dt = datetime.fromisoformat(c["date"]).astimezone(tz)
        if start_date <= dt.date() <= end_date:
            result.append({**c, "datetime": dt})
    result.sort(key=lambda c: c["datetime"])
    return result


# ── Core algorithm ───────────────────────────────────────────────────────────

def build_sessions(commits: list[dict], max_gap: timedelta, first_bonus: timedelta) -> list[dict]:
    """Group commits into work sessions and compute durations."""
    if not commits:
        return []

    sessions: list[dict] = []
    current: list[dict] = [commits[0]]

    for c in commits[1:]:
        gap = c["datetime"] - current[-1]["datetime"]
        if gap <= max_gap:
            current.append(c)
        else:
            sessions.append(_finalize_session(current, first_bonus))
            current = [c]

    sessions.append(_finalize_session(current, first_bonus))
    return sessions


def _finalize_session(commits: list[dict], first_bonus: timedelta) -> dict:
    """Compute duration and per-repo attribution for a single session."""
    start = commits[0]["datetime"]
    end = commits[-1]["datetime"]
    span = end - start
    duration = span + first_bonus

    # Per-repo attribution
    repo_hours: dict[str, float] = defaultdict(float)
    bonus_h = first_bonus.total_seconds() / 3600

    if len(commits) == 1:
        repo_hours[commits[0]["repo"]] += bonus_h
    else:
        # First bonus → first commit's repo
        repo_hours[commits[0]["repo"]] += bonus_h
        # Each gap → second commit's repo
        for i in range(1, len(commits)):
            gap_h = (commits[i]["datetime"] - commits[i - 1]["datetime"]).total_seconds() / 3600
            repo_hours[commits[i]["repo"]] += gap_h

    return {
        "start": start,
        "end": end,
        "duration": duration,
        "commits": commits,
        "repo_hours": dict(repo_hours),
    }


# ── Repo → Client/Project mapping ─────────────────────────────────────────────

def load_repo_mapping(path: str | None) -> dict[str, dict[str, str]]:
    """Load repo → {client, project} mapping from a JSON file."""
    if path is None:
        path = str(Path(__file__).resolve().parent.parent / "config" / "repo-mapping.json")
    if not os.path.isfile(path):
        print(f"Warning: repo mapping file not found at {path}, using empty mapping.", file=sys.stderr)
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("repos", {})


def get_client_project(repo: str, mapping: dict[str, dict[str, str]]) -> tuple[str, str]:
    """Return (client, project) for a repo, falling back to Other / Other."""
    entry = mapping.get(repo)
    if entry:
        return entry["client"], entry["project"]
    return "Other", "Other"


# ── Aggregation helpers ──────────────────────────────────────────────────────

def aggregate(sessions: list[dict], commits: list[dict], repo_mapping: dict[str, dict[str, str]] | None = None) -> dict:
    """Build all summary data structures."""
    total_hours = sum(s["duration"].total_seconds() / 3600 for s in sessions)
    total_commits = len(commits)

    # Per-repo
    repo_hours: dict[str, float] = defaultdict(float)
    repo_commits: dict[str, int] = defaultdict(int)
    for s in sessions:
        for repo, h in s["repo_hours"].items():
            repo_hours[repo] += h
    for c in commits:
        repo_commits[c["repo"]] += 1

    repo_table = []
    for repo in sorted(repo_hours, key=lambda r: repo_hours[r], reverse=True):
        h = repo_hours[repo]
        repo_table.append({
            "repo": repo,
            "hours": h,
            "commits": repo_commits.get(repo, 0),
            "pct": (h / total_hours * 100) if total_hours else 0,
        })

    # Per-day
    day_map: dict[str, dict] = {}
    for s in sessions:
        day_key = s["start"].strftime("%Y-%m-%d")
        if day_key not in day_map:
            day_map[day_key] = {"date": day_key, "weekday": s["start"].strftime("%a"), "hours": 0.0, "sessions": 0, "commits": 0}
        day_map[day_key]["hours"] += s["duration"].total_seconds() / 3600
        day_map[day_key]["sessions"] += 1
        day_map[day_key]["commits"] += len(s["commits"])

    day_table = [day_map[k] for k in sorted(day_map)]
    active_days = len(day_table)
    avg_hours = total_hours / active_days if active_days else 0

    # Per-client/project
    mapping = repo_mapping or {}
    client_hours: dict[tuple[str, str], float] = defaultdict(float)
    client_commits: dict[tuple[str, str], int] = defaultdict(int)
    for repo, h in repo_hours.items():
        client, project = get_client_project(repo, mapping)
        client_hours[(client, project)] += h
    for c in commits:
        client, project = get_client_project(c["repo"], mapping)
        client_commits[(client, project)] += 1

    client_table = []
    for key in sorted(client_hours, key=lambda k: client_hours[k], reverse=True):
        h = client_hours[key]
        client_table.append({
            "client": key[0],
            "project": key[1],
            "hours": h,
            "commits": client_commits.get(key, 0),
            "pct": (h / total_hours * 100) if total_hours else 0,
        })

    return {
        "total_hours": total_hours,
        "total_commits": total_commits,
        "total_sessions": len(sessions),
        "active_days": active_days,
        "avg_hours_per_day": avg_hours,
        "repo_table": repo_table,
        "client_table": client_table,
        "day_table": day_table,
        "sessions": sessions,
    }


# ── Report formatters ────────────────────────────────────────────────────────

def format_console(agg: dict, args: argparse.Namespace) -> str:
    lines: list[str] = []
    lines.append(f"Work Hours Estimate: {args.start} to {args.end}")
    lines.append(f"Author: {args.author}  |  Timezone: {args.timezone}")
    lines.append(f"Max gap: {args.max_gap}min  |  First-commit bonus: {args.first_bonus}min")
    lines.append("=" * 70)
    lines.append(f"Total estimated hours:  {agg['total_hours']:.1f}h")
    lines.append(f"Total commits:          {agg['total_commits']}")
    lines.append(f"Total sessions:         {agg['total_sessions']}")
    lines.append(f"Active days:            {agg['active_days']}")
    lines.append(f"Avg hours/active day:   {agg['avg_hours_per_day']:.1f}h")
    lines.append("")

    # Per-client table
    lines.append("Per-Client Breakdown")
    lines.append("-" * 70)
    lines.append(f"{'Client / Project':<40} {'Hours':>6} {'Commits':>8} {'%':>5}")
    lines.append("-" * 70)
    for r in agg["client_table"]:
        label = f"{r['client']} / {r['project']}"
        lines.append(f"{label:<40} {r['hours']:>6.1f} {r['commits']:>8} {r['pct']:>5.1f}")
    lines.append("")

    # Per-repo table
    lines.append("Per-Repository Breakdown")
    lines.append("-" * 70)
    lines.append(f"{'Repository':<45} {'Hours':>6} {'Commits':>8} {'%':>5}")
    lines.append("-" * 70)
    for r in agg["repo_table"]:
        lines.append(f"{r['repo']:<45} {r['hours']:>6.1f} {r['commits']:>8} {r['pct']:>5.1f}")
    lines.append("")

    # Per-day table
    lines.append("Daily Breakdown")
    lines.append("-" * 70)
    lines.append(f"{'Date':<12} {'Day':<5} {'Hours':>6} {'Sessions':>9} {'Commits':>8}")
    lines.append("-" * 70)
    for d in agg["day_table"]:
        lines.append(f"{d['date']:<12} {d['weekday']:<5} {d['hours']:>6.1f} {d['sessions']:>9} {d['commits']:>8}")

    return "\n".join(lines)


def format_markdown(agg: dict, args: argparse.Namespace) -> str:
    lines: list[str] = []
    lines.append(f"# Work Hours Estimate: {args.start} to {args.end}")
    lines.append("")
    lines.append(f"**Author:** {args.author}  ")
    lines.append(f"**Timezone:** {args.timezone}  ")
    lines.append(f"**Parameters:** max gap = {args.max_gap}min, first-commit bonus = {args.first_bonus}min  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total estimated hours | **{agg['total_hours']:.1f}h** |")
    lines.append(f"| Total commits | {agg['total_commits']} |")
    lines.append(f"| Total sessions | {agg['total_sessions']} |")
    lines.append(f"| Active days | {agg['active_days']} |")
    lines.append(f"| Avg hours/active day | {agg['avg_hours_per_day']:.1f}h |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-client
    lines.append("## Per-Client Breakdown")
    lines.append("")
    lines.append("| Client | Project | Hours | Commits | % of Time |")
    lines.append("|--------|---------|------:|--------:|----------:|")
    for r in agg["client_table"]:
        lines.append(f"| {r['client']} | {r['project']} | {r['hours']:.1f} | {r['commits']} | {r['pct']:.1f}% |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-repo
    lines.append("## Per-Repository Breakdown")
    lines.append("")
    lines.append("| Repository | Hours | Commits | % of Time |")
    lines.append("|------------|------:|--------:|----------:|")
    for r in agg["repo_table"]:
        lines.append(f"| {r['repo']} | {r['hours']:.1f} | {r['commits']} | {r['pct']:.1f}% |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-day
    lines.append("## Daily Breakdown")
    lines.append("")
    lines.append("| Date | Day | Hours | Sessions | Commits |")
    lines.append("|------|-----|------:|---------:|--------:|")
    for d in agg["day_table"]:
        lines.append(f"| {d['date']} | {d['weekday']} | {d['hours']:.1f} | {d['sessions']} | {d['commits']} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Session detail (expandable)
    lines.append("## Session Detail")
    lines.append("")
    for i, s in enumerate(agg["sessions"], 1):
        dur_h = s["duration"].total_seconds() / 3600
        start_str = s["start"].strftime("%Y-%m-%d %H:%M")
        end_str = s["end"].strftime("%H:%M")
        n = len(s["commits"])
        lines.append(f"<details><summary>Session {i}: {start_str}–{end_str} ({dur_h:.1f}h, {n} commits)</summary>")
        lines.append("")
        lines.append("| Time | Repository | Message |")
        lines.append("|------|------------|---------|")
        for c in s["commits"]:
            t = c["datetime"].strftime("%H:%M")
            short_repo = c["repo"].split("/")[-1]
            msg = c["message"][:80]
            lines.append(f"| {t} | {short_repo} | {msg} |")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines)


def format_json(agg: dict, args: argparse.Namespace) -> str:
    def _serialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, timedelta):
            return obj.total_seconds()
        raise TypeError(f"Not serializable: {type(obj)}")

    output = {
        "parameters": {
            "author": args.author,
            "start": args.start,
            "end": args.end,
            "timezone": args.timezone,
            "max_gap_minutes": args.max_gap,
            "first_bonus_minutes": args.first_bonus,
        },
        "summary": {
            "total_hours": round(agg["total_hours"], 2),
            "total_commits": agg["total_commits"],
            "total_sessions": agg["total_sessions"],
            "active_days": agg["active_days"],
            "avg_hours_per_day": round(agg["avg_hours_per_day"], 2),
        },
        "repos": agg["repo_table"],
        "clients": agg["client_table"],
        "days": agg["day_table"],
        "sessions": [
            {
                "start": s["start"].isoformat(),
                "end": s["end"].isoformat(),
                "duration_hours": round(s["duration"].total_seconds() / 3600, 2),
                "commit_count": len(s["commits"]),
                "repo_hours": {k: round(v, 2) for k, v in s["repo_hours"].items()},
                "commits": [
                    {"sha": c["sha"][:8], "time": c["datetime"].isoformat(), "repo": c["repo"], "message": c["message"]}
                    for c in s["commits"]
                ],
            }
            for s in agg["sessions"]
        ],
    }
    return json.dumps(output, indent=2, default=_serialize)


# ── CLI ──────────────────────────────────────────────────────────────────────

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Estimate work hours from GitHub commit timestamps.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python gh-work-hours.py --start 2026-02-01 --end 2026-02-28\n"
               "  python gh-work-hours.py --start 2026-02-01 --end 2026-02-28 --format markdown --output docs/hours.md\n"
               "  python gh-work-hours.py --max-gap 90 --first-bonus 20 --start 2026-01-01 --end 2026-01-31\n",
    )
    p.add_argument("--author", default="ehalsey", help="GitHub username (default: ehalsey)")
    p.add_argument("--start", required=True, help="Start date YYYY-MM-DD (inclusive)")
    p.add_argument("--end", required=True, help="End date YYYY-MM-DD (inclusive)")
    p.add_argument("--timezone", default="America/Los_Angeles", help="IANA timezone (default: America/Los_Angeles)")
    p.add_argument("--max-gap", type=int, default=120, help="Max minutes between commits in a session (default: 120)")
    p.add_argument("--first-bonus", type=int, default=30, help="Minutes credited before first commit per session (default: 30)")
    p.add_argument("--format", choices=["console", "markdown", "json"], default="console", help="Output format (default: console)")
    p.add_argument("--output", help="Write to file instead of stdout")
    p.add_argument("--emails", nargs="*", help="Additional author emails to search")
    p.add_argument("--repo-map", help="Path to repo-mapping JSON file (default: config/repo-mapping.json)")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    tz = ZoneInfo(args.timezone)
    max_gap = timedelta(minutes=args.max_gap)
    first_bonus = timedelta(minutes=args.first_bonus)

    # Fetch
    raw = fetch_commits(args.author, args.start, args.end, args.emails)
    print(f"Fetched {len(raw)} commits from GitHub API.", file=sys.stderr)

    # Normalize & filter
    commits = parse_and_localize(raw, tz, args.start, args.end)
    print(f"{len(commits)} commits after timezone filtering.", file=sys.stderr)

    if not commits:
        print("No commits in the local-date range.", file=sys.stderr)
        sys.exit(0)

    # Sessions
    sessions = build_sessions(commits, max_gap, first_bonus)
    print(f"Grouped into {len(sessions)} work sessions.", file=sys.stderr)

    # Load repo mapping
    repo_mapping = load_repo_mapping(args.repo_map)

    # Aggregate
    agg = aggregate(sessions, commits, repo_mapping)

    # Format
    formatters = {"console": format_console, "markdown": format_markdown, "json": format_json}
    report = formatters[args.format](agg, args)

    # Output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
            if not report.endswith("\n"):
                f.write("\n")
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
