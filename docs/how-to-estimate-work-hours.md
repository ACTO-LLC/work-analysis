# How To: Estimate Work Hours from GitHub Commits

Estimate billable/work hours for any GitHub user by analyzing commit timestamps across all repositories and organizations.

## Prerequisites

- **Python 3.9+** (uses `zoneinfo`)
- **GitHub CLI** (`gh`) — authenticated with access to the target repos
  - Install: https://cli.github.com/
  - Auth: `gh auth login`

## Quick Start

```bash
# Current month for default user (ehalsey)
python scripts/gh-work-hours.py --start 2026-02-01 --end 2026-02-28

# Any user, any month
python scripts/gh-work-hours.py --author octocat --start 2026-01-01 --end 2026-01-31
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--author` | `ehalsey` | GitHub username |
| `--start` | *(required)* | Start date `YYYY-MM-DD` (inclusive) |
| `--end` | *(required)* | End date `YYYY-MM-DD` (inclusive) |
| `--timezone` | `America/Los_Angeles` | IANA timezone for date boundaries |
| `--max-gap` | `120` | Max minutes between commits before starting a new session |
| `--first-bonus` | `30` | Minutes credited before the first commit in each session |
| `--format` | `console` | Output format: `console`, `markdown`, or `json` |
| `--output` | stdout | Write to a file instead of printing |
| `--emails` | *(none)* | Additional author emails to search |

## Output Formats

### Console (default)

Formatted tables printed to the terminal:

```bash
python scripts/gh-work-hours.py --start 2026-02-01 --end 2026-02-28
```

### Markdown

Tables matching the style in `docs/`, with expandable session detail:

```bash
python scripts/gh-work-hours.py --start 2026-02-01 --end 2026-02-28 \
  --format markdown --output docs/work-hours-2026-02.md
```

### JSON

Structured data for programmatic use or piping into other tools:

```bash
python scripts/gh-work-hours.py --start 2026-02-01 --end 2026-02-28 \
  --format json --output data.json
```

## How the Algorithm Works

The script implements the **git-hours** algorithm:

1. **Fetch** — Queries the GitHub Search API for all commits by the author in the date range. Deduplicates by SHA.
2. **Normalize** — Converts UTC timestamps to the target timezone and filters by local date (handles UTC boundary edge cases).
3. **Session grouping** — Sorts all commits chronologically across repos. Consecutive commits ≤ `max-gap` apart are grouped into the same work session. Larger gaps start a new session.
4. **Duration** — Each session's duration = (last commit − first commit) + `first-bonus`. The bonus accounts for work done before the first commit of a session.
5. **Repo attribution** — Each inter-commit gap is credited to the second commit's repo. The first-bonus goes to the first commit's repo. Single-commit sessions get the full bonus.

### Example

```
09:00  commit A (repo-x)     ← session starts, 30min bonus → repo-x
09:45  commit B (repo-x)     ← 45min gap → repo-x
10:30  commit C (repo-y)     ← 45min gap → repo-y
                               session total: 1.5h + 0.5h bonus = 2.0h

14:00  commit D (repo-y)     ← 3.5h gap from C → new session, 30min bonus → repo-y
                               session total: 0h + 0.5h bonus = 0.5h
```

## Tuning Parameters

The defaults (`--max-gap 120 --first-bonus 30`) work well for most developers. Adjust if needed:

```bash
# Tighter sessions (1h gap, 20min bonus) — lower estimate
python scripts/gh-work-hours.py --start 2026-02-01 --end 2026-02-28 \
  --max-gap 60 --first-bonus 20

# Looser sessions (3h gap, 45min bonus) — higher estimate
python scripts/gh-work-hours.py --start 2026-02-01 --end 2026-02-28 \
  --max-gap 180 --first-bonus 45
```

Run with a few different values to see sensitivity and pick what best reflects your work style.

## Limitations

- **Lower-bound estimate** — Only counts time between commits. Code review, debugging without commits, meetings, and design work are not captured.
- **GitHub Search API cap** — Returns at most 1,000 results. The script warns if this limit is hit. For very active months, narrow the date range.
- **Merge commits** — Included by default (they still represent work). Check session detail in the markdown report to see individual commit messages.
- **Multi-author sessions** — If two people commit to different repos within the gap window, those commits merge into one session. Use `--max-gap` to adjust if this is an issue.
