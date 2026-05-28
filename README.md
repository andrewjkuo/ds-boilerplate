# Data Science Boilerplate
A standardised project structure for doing and sharing data science work that enforces best practices.

This template has been influenced by [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/), [Kedro](https://kedro.org/) and [govcookiecutter](https://best-practice-and-impact.github.io/govcookiecutter/#govcookiecutter). The goal is to maintain modularity and separation of concerns:
- **Shared Code**: All reusable code should reside in the `src` directory.
- **Apps, Pipelines, and Notebooks**: Use the shared code in apps, pipelines, and notebooks, ensuring that your project remains clean and maintainable.

## Usage
1. Install [uv](https://docs.astral.sh/uv/) if you don't already have it.
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Start a new project (uvx will download cookiecutter on demand). You will be prompted to enter some configuration values. The template targets Python 3.11+ by default.
   ```bash
   uvx cookiecutter gh:andrewjkuo/ds-boilerplate
   ```

## Template Options

The prompt set is intended to keep generated projects lean. The main toggles are:

- `include_codex_scaffolding`: include `AGENTS.md`, `CONTEXT.md`, `docs/agents/`, `docs/adr/`, and lightweight `tasks/` scratch files
- `include_streamlit_app`: include a starter Streamlit app under `app_streamlit/`
- `include_fastapi_app`: include a starter FastAPI app under `app_fastapi/`
- `use_prefect`: include Prefect task and flow scaffolding under `pipelines/`
- `cloud_provider`: include cloud storage utility code and matching dependencies
- `database_type`: include database utility code and matching dependencies

If `include_codex_scaffolding=no`, the generated project will not include `AGENTS.md`, `CONTEXT.md`, `docs/agents/`, `docs/adr/`, or `tasks/`.

## Project Structure
The directory structure of your new project looks like this:
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
├── AGENTS.md              <- Optional repo-local Codex instructions for the generated project.
├── Makefile               <- Makefile with useful commands for project setup and running analysis.
├── README.md              <- The top-level README for developers using this project.
├── app                    <- App-specific code, requirements file and Dockerfile.
├── conf                   <- Configuration files that can be stored in source control.
├── CONTEXT.md             <- Optional domain context for agents and contributors.
├── data
│   ├── 01_raw             <- The original, immutable data dump.
│   ├── 02_intermediate    <- Intermediate data that has been transformed.
│   ├── 03_model_input     <- The final, canonical data sets for modeling.
│   └── 04_model_output    <- Outputs from models (e.g. predictions).
├── models                 <- Trained and serialized models or model summaries.
├── notebooks              <- Jupyter notebooks.
├── pipelines              <- Pipeline scripts for data processing and model training.
├── pyproject.toml         <- Project metadata and dependencies.
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── src                    <- Source code for use in this project.
│   └── package
│       ├── __init__.py    <- Make package a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
├── docs
│   ├── adr                <- Optional architecture decision records.
│   └── agents             <- Optional agent workflow docs.
├── tasks                  <- Optional repo-local Codex scratchpad files and lessons.
└── tests                  <- Tests for functions in src.
```

Optional prompts remove their corresponding files and folders during generation.

## Codex Support

If you enable `include_codex_scaffolding`, the generated project includes lightweight Codex support files that are meant to remain useful even on machines without the same global `~/.codex` setup.

- `AGENTS.md`: project-specific guidance for commands, structure, debugging, and verification
- `CONTEXT.md`: project domain vocabulary, invariants, workflows, and data assumptions
- `docs/agents/issue-tracker.md`: issue tracker conventions for skills that create or read tickets
- `docs/agents/triage-labels.md`: canonical label mappings plus a small `gh` bootstrap path
- `docs/agents/domain.md`: how skills should consume `CONTEXT.md` and ADRs
- `docs/agents/setup.md`: what still needs to exist in global/local Codex setup
- `docs/adr/README.md`: ADR purpose and starter template
- `tasks/todo.md`: an ephemeral plan/progress scratchpad for substantial active work
- `tasks/lessons.md`: repo-specific corrections and recurring gotchas

The Codex skills themselves and your global Codex config do not port with a generated project. Keep that personal setup outside this template, for example in dotfiles or a machine bootstrap checklist. The generated files make the repo usable without that setup and give installed skills the repo-local configuration they need when they are available.

By default, generated projects assume GitHub Issues for backlog, PRDs, prioritization, and durable implementation tickets. The optional triage labels are `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`; create them with the `gh` commands in `docs/agents/triage-labels.md` after the generated repo exists on GitHub.

Use `AGENTS.md` for repo operating instructions and `CONTEXT.md` for domain truth. ADRs in `docs/adr/` are the durable decision record.

## Future
* Test this template in more environments.
* Add functionality to automatically generate documentation.
