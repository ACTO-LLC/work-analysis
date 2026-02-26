# Work Hours Report

Generate a work hours report from GitHub commits, save the markdown report, commit it, and upsert a GitHub issue with the results.

## Usage

```
/work-hours [author] [YYYY-MM]
```

- `author` — GitHub username (default: `ehalsey`)
- `YYYY-MM` — Target month (default: current month)

## Examples

```
/work-hours                     # ehalsey, current month
/work-hours ehalsey 2025-12     # ehalsey, Dec 2025
/work-hours octocat 2026-01     # different user, Jan 2026
```

## Instructions

You will generate a work hours report and publish it. Follow these steps exactly.

### Step 1 — Parse arguments

Parse `$ARGUMENTS` to extract the author and month.

- If two tokens are provided, the first is `author` and the second is `YYYY-MM`.
- If one token is provided and it matches `YYYY-MM` format (4 digits, dash, 2 digits), treat it as the month with author defaulting to `ehalsey`.
- If one token is provided and it does NOT match `YYYY-MM`, treat it as the author with the month defaulting to the current month.
- If no tokens are provided, default to author `ehalsey` and the current month.

From the `YYYY-MM` value, compute:
- `START_DATE` = first day of the month (`YYYY-MM-01`)
- `END_DATE` = last day of the month (account for month length and leap years)

### Step 2 — Run the script (console output)

Run from the project root `C:\source\work-analysis`:

```bash
python scripts/gh-work-hours.py --author AUTHOR --start START_DATE --end END_DATE --format console
```

Display the full console output to the user so they can see the results immediately.

### Step 3 — Run the script (markdown output)

```bash
python scripts/gh-work-hours.py --author AUTHOR --start START_DATE --end END_DATE --format markdown --output docs/work-hours-YYYY-MM.md
```

This writes the report file to `docs/work-hours-YYYY-MM.md`.

### Step 4 — Commit the report

Stage and commit the generated (or updated) report file:

```bash
git add docs/work-hours-YYYY-MM.md
git commit -m "Add/Update MON YYYY work hours report"
```

Use a descriptive commit message like `Add Jan 2026 work hours report` or `Update Feb 2026 work hours report` depending on whether the file is new or updated. Check `git status` first to determine which.

### Step 5 — Upsert GitHub issue

Search for an existing issue on `ACTO-LLC/work-analysis` whose title contains the phrase for this report:

```bash
gh search issues --repo ACTO-LLC/work-analysis --match title "work hours report for AUTHOR for Mon YYYY" --json number,title
```

Where `Mon YYYY` is the abbreviated month name and year (e.g., `Feb 2026`).

- **If an existing issue is found**: update its body with the markdown report content.

  ```bash
  gh issue edit ISSUE_NUMBER --repo ACTO-LLC/work-analysis --body "MARKDOWN_CONTENT"
  ```

- **If no issue is found**: create a new one.

  ```bash
  gh issue create --repo ACTO-LLC/work-analysis --title "Work hours report for AUTHOR for Mon YYYY" --body "MARKDOWN_CONTENT"
  ```

For the issue body, read the contents of `docs/work-hours-YYYY-MM.md` and use that as the body.

### Step 6 — Report summary

Tell the user:
- Total estimated hours and commit count (from the console output)
- The file path of the saved report
- The commit that was created
- A link to the GitHub issue (created or updated)
