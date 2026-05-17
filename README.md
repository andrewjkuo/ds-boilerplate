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

- `include_codex_scaffolding`: include `AGENTS.md` plus `tasks/todo.md`, `tasks/lessons.md`, and `tasks/decisions.md`
- `include_streamlit_app`: include a starter Streamlit app under `app_streamlit/`
- `include_fastapi_app`: include a starter FastAPI app under `app_fastapi/`
- `use_prefect`: include Prefect task and flow scaffolding under `pipelines/`
- `cloud_provider`: include cloud storage utility code and matching dependencies
- `database_type`: include database utility code and matching dependencies

If `include_codex_scaffolding=no`, the generated project will not include `AGENTS.md` or `tasks/`.

## Project Structure
The directory structure of your new project looks like this:
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
├── AGENTS.md              <- Optional repo-local Codex instructions for the generated project.
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
├── src                    <- Source code for use in this project.
│   └── package
│       ├── __init__.py    <- Make package a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
├── tasks                  <- Optional repo-local Codex task tracking and lessons.
└── tests                  <- Tests for functions in src.
```

Optional prompts remove their corresponding files and folders during generation.

## Codex Support

If you enable `include_codex_scaffolding`, the generated project includes lightweight Codex support files that are meant to remain useful even on machines without the same global `~/.codex` setup.

- `AGENTS.md`: project-specific guidance for commands, structure, debugging, and verification
- `tasks/todo.md`: a lightweight plan/progress file for substantial tasks
- `tasks/lessons.md`: repo-specific corrections and recurring gotchas
- `tasks/decisions.md`: notable architectural, modelling, or workflow decisions

## Future
* Test this template in more environments.
* Add functionality to automatically generate documentation.
