# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Project Structure
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
├── AGENTS.md              <- Repo-local Codex instructions for this project.
├── CONTEXT.md             <- Domain context for agents and contributors.
{% endif -%}
├── Makefile               <- Makefile with useful commands for project setup and running analysis.
├── README.md              <- The top-level README for developers using this project.
├── app                    <- App-specific code, requirements file and Dockerfile.
├── conf                   <- Configuration files that can be stored in source control.
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
{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
├── docs
│   ├── adr                <- Architecture decision records.
│   └── agents             <- Agent workflow docs.
{% endif -%}
├── src                    <- Source code for use in this project.
│   └── {{ cookiecutter.package_name }}
│       ├── __init__.py    <- Make {{ cookiecutter.package_name }} a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
├── tasks                  <- Repo-local session scratchpad and lessons.
{% endif -%}
└── tests                  <- Tests for functions in src.
```

## Getting Started

### Setup

1. **Install uv** (if you don't already have it):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install Dependencies and Initialize Git** (uv will create `.venv` automatically):
   ```bash
   git init
   uv sync --extra dev
   uv run pre-commit install
   ```

   Alternatively, you can use the `make` command:
   ```bash
   git init
   make install
   ```

   To work inside the environment directly:
   ```bash
   source .venv/bin/activate
   ```

   Note: The Makefile exports `UV_PROJECT_ENVIRONMENT=.venv` so `uv run` uses the synced virtual environment. If you call `uv run` manually outside the Makefile, either export that variable or activate `.venv` first.

   The template defaults to Python 3.11+ (see `requires-python` in `pyproject.toml`). If you need a different version, update that field before syncing.

3. **Make Initial Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
### Codex Support Files

This project includes optional repo-local Codex scaffolding:

- `AGENTS.md`: project-specific instructions that complement any global `~/.codex` settings
- `CONTEXT.md`: project domain vocabulary, invariants, workflows, and data assumptions
- `docs/agents/issue-tracker.md`: issue tracker conventions for skills that create or read tickets
- `docs/agents/triage-labels.md`: canonical label mappings plus a small `gh` bootstrap path
- `docs/agents/domain.md`: how skills should consume `CONTEXT.md` and ADRs
- `docs/agents/setup.md`: what still needs to exist in global/local Codex setup
- `docs/adr/README.md`: ADR purpose and starter template
- `tasks/todo.md`: an ephemeral plan/progress scratchpad for substantial active work
- `tasks/lessons.md`: repo-specific lessons and recurring gotchas

The Codex skills themselves and your global Codex config do not port with this repo. Keep that personal setup outside this repo, for example in dotfiles or a machine bootstrap checklist. The repo-local files make the repo usable without that setup and give installed skills the repo-local configuration they need when they are available.

By default, this scaffold assumes GitHub Issues for backlog, PRDs, prioritization, and durable implementation tickets. The optional triage labels are `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`; create them with the `gh` commands in `docs/agents/triage-labels.md` after this repo exists on GitHub.

Use `AGENTS.md` for repo operating instructions and `CONTEXT.md` for domain truth. ADRs in `docs/adr/` are the durable decision record.

If you plan to use Codex in this repo, update `AGENTS.md` early with real setup commands, verification commands, project layout, operational risks, and local conventions. Put domain vocabulary, datasets, units, invariants, and business rules in `CONTEXT.md`.

These files make the repo more self-contained when used across machines with different Codex global configuration.

{% endif -%}

### Usage

#### Data

- **Immutability**: Raw data should not be edited. Transform data through your processing pipeline.
- **Directory Structure**: Organize any local data into `01_raw`, `02_intermediate`, `03_model_input`, and `04_model_output`.

#### Pipelines

- **Prefect**: Prefect is the default orchestration tool but you are free to use whatever technology you like. If Prefect is selected:
   - **Task and Flow Definition**: Prefect tasks and flows are defined in `pipelines/tasks.py` and `pipelines/flows.py`.
   - **Execution**: Use the Makefile to spin up the Prefect server and manage pipelines.
 
#### Code Quality

- **Black**: Black is installed as a pre-commit hook and will automatically format any python code. This enables faster code review and small diffs.
- **Flake8**: Flake8 is used for linting and installed as a pre-commit hook.

#### Notebooks

- **Purpose**: Notebooks are for exploration and communication. Refactor useful code into the `src` directory.
- **nbstripout**: Notebook output should ~not~ rarely be committed to source control because it creates ugly diffs and risks data leakage. Nbstripout is installed as a pre-commit hook. It can be ignored by setting the ```"keep_output": true``` metadata on a cell.
- **Auto-reloading**:
  ```python🚡
  %load_ext autoreload
  %autoreload 2
  ```

#### Applications

- **Streamlit and FastAPI**: If selected, templates are provided with `requirements.txt` and `Dockerfile` for building containerized apps.

### Cloud Storage and Database Connections

- **Cloud Storage**: If selected, utility functions for connecting to cloud storage are in `utils/cloud_storage.py`. Configuration settings are added to `.env`.
- **Database Connections**: If selected, utility functions for database connections are in `utils/db.py`. Configuration settings are added to `.env`.

### Project Philosophy

The goal is to maintain modularity and separation of concerns:
- **Shared Code**: All reusable code should reside in the `src/{{ cookiecutter.package_name }}` directory.
- **Apps, Pipelines, and Notebooks**: Use the shared code in apps, pipelines, and notebooks, ensuring that your project remains clean and maintainable.

## Acknowledgements

This project template is based on the [Data Science Boilerplate](https://github.com/andrewjkuo/ds-boilerplate), influenced by [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/), [Kedro](https://kedro.org/), and [govcookiecutter](https://best-practice-and-impact.github.io/govcookiecutter/#govcookiecutter).
