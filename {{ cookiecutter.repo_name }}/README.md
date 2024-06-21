# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Project Structure
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
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
│   └── {{ cookiecutter.package_name }}
│       ├── __init__.py    <- Make {{ cookiecutter.package_name }} a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
└── tests                  <- Tests for functions in src.
```

## Getting Started

### Setup

1. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install Dependencies and Initialize Git**:
   ```bash
   git init
   pip install -U pip setuptools
   pip install -e .[dev]
   pre-commit install
   ```

   Alternatively, you can use the `make` command:
   ```bash
   git init
   make install
   ```

3. **Make Initial Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

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
