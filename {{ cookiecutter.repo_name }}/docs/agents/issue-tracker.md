# Issue Tracker: GitHub

Issues and PRDs for this repo are tracked in GitHub Issues after the repo is pushed to GitHub.

## Conventions

- Track backlog and implementation work as GitHub issues.
- Track PRDs as GitHub issues with a clear `PRD:` prefix in the issue title.
- Apply triage labels using the canonical mappings in `triage-labels.md`.
- Keep durable status, prioritization, and discussion in GitHub issue threads instead of local markdown files.
- Use `tasks/todo.md` only for short-lived session planning while work is actively underway.

## Enhanced workflow prerequisites

The documented workflow is still readable without special tooling, but automated issue creation or skill-driven triage needs:

- The repo has a GitHub remote.
- The GitHub CLI (`gh`) is installed and authenticated when a skill needs to create or update issues.
- Codex has access to the relevant skills on the machine running it.

These skills and global Codex settings do not ship with this template. This file records the repo-local workflow that people, Codex, and installed skills should follow.

## When a skill says "publish to the issue tracker"

Create or update a GitHub issue in this repository with the relevant scope, acceptance criteria, and labels.

## When a skill says "fetch the relevant ticket"

Open the referenced GitHub issue by number or URL and use that thread as the source of truth.
