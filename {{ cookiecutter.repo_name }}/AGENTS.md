# Repository Instructions

These are repo-local instructions for agents working in this project. They should be useful even when no personal global agent config or optional skills are installed.

Keep this file focused on how to work in this repo: commands, structure, source-of-truth boundaries, risks, and verification. Put domain vocabulary, invariants, workflows, data semantics, and business rules in `CONTEXT.md`.

## Project overview

Describe the actual project here. Keep it short and concrete: what the repo is for, what it produces, and what correct work looks like.

## Minimum operating rules

- Make a short plan before non-trivial work: multi-step tasks, debugging, cross-cutting edits, architecture/API changes, data/schema changes, security-sensitive work, or unclear requirements.
- Inspect existing code, tests, configuration, and docs before guessing about project behavior.
- Find root causes before patching symptoms unless the task explicitly asks for a temporary workaround.
- Keep changes scoped to the task and avoid unrelated formatting, naming, or architectural churn.
- Do not add production dependencies, change public interfaces, or restructure major folders without a clear project-specific reason.
- Run relevant verification before saying work is complete. If verification is blocked, state exactly what could not be run and why.
- When corrected by the user, update `tasks/lessons.md` if the correction reveals a reusable repo-specific rule.

## Commands

- Treat `README.md` and `Makefile` as the source of truth for setup, test, lint, and run commands.
- Document only non-obvious or project-specific commands here when they exist.

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

- Use the configured issue tracker for backlog, prioritization, PRDs, and durable implementation tickets.
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
- Keep repo-level instructions specific to this project and avoid duplicating broad personal agent preferences.

## Verification expectations

Before saying done, run the most relevant subset of:

```bash
make test
make lint
uv build
```

Add extra validation commands here if this project adopts them. Do not claim completion without verification; if something cannot be run, explain exactly what was blocked and what should be run next.
