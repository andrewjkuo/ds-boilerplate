# Repository Instructions

These instructions add project-specific context on top of the global Codex instructions from `~/.codex`.
Keep this file focused on information that is true for this repo; avoid restating generic workflow guidance that already lives in `~/.codex`, `README.md`, or the `Makefile`.

## Project overview

Describe the actual project here. Keep it short and concrete: what the repo is for, what it produces, and what correct work looks like.

Keep domain facts, glossary terms, invariants, workflows, data semantics, and business rules in `CONTEXT.md`. Keep this file focused on how agents should operate in this repo: commands, structure, source-of-truth boundaries, risks, and verification.

## Commands

- Treat `README.md` and `Makefile` as the source of truth for setup, test, lint, and run commands.
- Document only non-obvious or project-specific commands here when they exist.

## Working defaults

- Prefer small, correct, reviewable changes over broad rewrites.
- Inspect existing code, tests, config, and docs before guessing about project behavior.
- Find root causes before patching symptoms unless the task explicitly asks for a temporary workaround.
- Do not add production dependencies, change public interfaces, or restructure major folders without a clear project-specific reason.

## Architecture

- `src/{{ cookiecutter.package_name }}/`: reusable project code; prefer putting durable logic here
- `tests/`: unit tests for code in `src/`
- `pipelines/`: orchestration entry points{% if cookiecutter.use_prefect not in ['yes', 'y', 'YES', 'Y'] %}; may be absent if Prefect was not selected{% endif %}
- `notebooks/`: exploration and communication; refactor stable logic back into `src/`
- `conf/`: versioned configuration
- `data/`: local data split into raw, intermediate, model input, and model output stages
- `models/`: trained artifacts or summaries
- `CONTEXT.md`: domain concepts, invariants, workflows, and vocabulary
- `docs/adr/`: durable architectural and product decisions
{% if cookiecutter.include_streamlit_app in ['yes', 'y', 'YES', 'Y'] -%}
- `app_streamlit/`: Streamlit app scaffold
{% endif -%}
{% if cookiecutter.include_fastapi_app in ['yes', 'y', 'YES', 'Y'] -%}
- `app_fastapi/`: FastAPI app scaffold
{% endif -%}
- `tasks/`: repo-local session scratchpad and lessons

## Task tracking

- Use GitHub Issues for backlog, prioritization, PRDs, and durable implementation tickets.
- Use `tasks/todo.md` only as an ephemeral session scratchpad for substantial work in progress.
- Read relevant ADRs in `docs/adr/` before changing architecture, public interfaces, data contracts, workflow patterns, or other areas where prior decisions may constrain the change.
- Add durable architectural, product, modelling, or workflow decisions as ADRs in `docs/adr/`.
- Use `tasks/lessons.md` for repo-specific corrections, recurring gotchas, or reusable mistakes that should change future work in this repo.

## Conventions

- Keep reusable domain logic out of notebooks and app entry points when practical.
- Prefer extending existing modules under `src/{{ cookiecutter.package_name }}/` before adding parallel helpers.
- Treat raw data as immutable and keep transformations explicit in code.
- Add or update tests for non-trivial behavior changes.
- Keep documentation up to date when behavior, setup, commands, configuration, data assumptions, or user-facing workflows change.

## Risk notes

- Do not commit `.env`, local data, secrets, or generated model artifacts unless the task explicitly requires it.
- Do not edit generated or derived outputs directly when the source code or pipeline should change instead.
- Keep repo-level instructions specific to this project and avoid repeating generic Codex behavior from global settings.

## Verification expectations

Before saying done, run the most relevant subset of:

```bash
make test
make lint
uv build
```

Add extra validation commands here if this project adopts them. Do not claim completion without verification; if something cannot be run, explain exactly what was blocked and what should be run next.

## Agent skills

### Issue tracker

Issues and PRDs are tracked in GitHub Issues for this repository once a GitHub remote exists. See `docs/agents/issue-tracker.md`.

### Triage labels

Triage uses the default canonical role strings (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Domain docs are configured as single-context (root `CONTEXT.md` + root `docs/adr/`). See `docs/agents/domain.md`.

### Local setup

This repo records the workflow that installed skills should follow, but does not include the skills or global Codex config. See `docs/agents/setup.md`.
