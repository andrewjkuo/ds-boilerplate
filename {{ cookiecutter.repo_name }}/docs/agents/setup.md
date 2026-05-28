# Agent Setup

This repo includes repo-local instructions for Codex and related engineering skills. It does not include the global Codex configuration or the skill implementations themselves.

The portability rule is: the repo must be usable without your personal global setup, and better when that setup is present.

## What ships with this repo

- `AGENTS.md`: repo-specific operating instructions for agents.
- `CONTEXT.md`: domain vocabulary, invariants, workflows, and data assumptions.
- `docs/agents/`: workflow configuration that skills can read.
- `docs/adr/`: durable decision records.
- `tasks/`: temporary session scratchpad and repo-specific lessons.

## Baseline mode

With only Codex and this repo, agents should still follow the workflow documented here:

- Use `AGENTS.md` for repo operating instructions.
- Use `CONTEXT.md` for domain truth.
- Use `docs/adr/` for durable decisions.
- Use GitHub Issues as the backlog if the repo has a GitHub remote and `gh` is available.
- Use `tasks/todo.md` only as temporary active-session scratch.
- Use `tasks/lessons.md` for repo-specific reusable lessons.

If a referenced skill is not installed, follow the documented workflow manually where practical and say what is missing.

## Enhanced mode

The workflow is smoother when the machine also has:

- Your preferred global Codex instructions.
- The relevant skills installed in the local Codex skills directory.
- GitHub CLI (`gh`) installed and authenticated if using the GitHub issue workflow.
- A GitHub remote for this repo if issues and PRDs should be published to GitHub.

Keep this personal setup outside the template, for example in dotfiles or a separate machine bootstrap checklist. The template should document the repo contract, not vendor your whole local Codex environment.

## Skill behavior

When skills are installed and available to Codex, they can be used in two ways:

- Automatically, when the task clearly matches a skill's description.
- Explicitly, when you name the skill in your request.

The repo-local files do not trigger skills by themselves. They give installed skills the project-specific configuration they need once a skill is invoked or selected.
