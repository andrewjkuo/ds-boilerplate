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
├── models                 <- Trained and serialised models or model summaries.
├── notebooks              <- Jupyter notebooks.
├── pipelines              <- 
├── pyproject.toml         <- 
├── references             <- Data dictionaries, manuals and all other explanatory materials.
├── src                    <- Source code for use in this project.
│   └── {{ cookiecutter.package_name }}
│       ├── __init__.py    <- Make {{cookiecutter.package_name}} a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Scripts with utility functions.
│       └── visualisation  <- Scripts to create exploratory and results-oriented visualisations.
└── tests                  <- Tests for functions in src.

```

## Getting Started
1. Setup and activate your virtual environment using your tool of choice.
2. Navigate to your new project and initialise Git.
   ```
   git init
   ```
3. Install necessary packages using `pip` and the `pre-commit` hooks.
   ```
   pip install -U pip setuptools
   pip install -r requirements.txt
   pre-commit install
   ```
   or use the `make` command.
   ```
   make req_hooks
   ```
4. Make desired changes to the project structure (e.g. you may want to alter the directories in `src` or `data` depending on your project requirements).
5. Stage all your project files, and make your first commit.
   ```
   git add .
   git commit -m "Initial commit"
   ```
6. Install your project in editable mode so that your functions code can be called (e.g. from a Jupyter Notebook).
   ```
   pip install -e .
   ```
   or use the `make` command.
   ```
   make install
   ```

## Usage
### Data
Data is immutable and raw data should not be edited. The code you write should move the raw data through a pipeline to your final analysis. By default, the `data` directory is included in the `.gitignore` file.

### Pipelines
Code should be structured as standalone functions like nodes in a DAG. We can then orchestrate and execute our pipeline by adding commands to the Makefile.

### Notebooks
Notebooks are for exploration and communication. They should not be used for data processing or model training and prediction. All useful code should be refactored and moved to the relevant pipeline in `src`.

Once src has been installed, you can import functions in your notebooks. Put the following cell at the top of your notebooks:
```python
# Load the "autoreload" extension so that code can change
%load_ext autoreload

# Always reload modules so that as you change code in src, it gets loaded
%autoreload 2
```

Notebooks do not play nicely with source control. They create ugly diffs and make it easy to unintentionally commit sensitive data. To deal with this, `nbstripout` is activated as a pre-commit hook and will automatically strip your notebooks of all output. If you would like to keep the output of certain cells or entire notebooks, add the following tag to your cell or notebook metadata respectively:
```json
{
    "keep_output": true
}
```

### Requirements
Requirements should be stored in ```requirements.txt``` using ```pip freeze```. By default, ```pip freeze``` will include your editable package so use the following command:
```
pip freeze --exclude-editable > requirements.txt
```

### Black
Black is "the uncompromising Python code formatter". It enforces PEP 8 compliance, improves readability and reduces git diffs. It is setup as a pre-commit hook but you can also call it separately.
```
black .
```
or use the `make` command:
```
make format
```

### Flake8
Flake8 is a Python linter and is setup as a pre-commit hook. You can also call it separately.
```bash
flake8 .
```
or use the `make` command:
```
make lint
```

### Testing: Pytest + Coverage
Unit tests should be written using the `pytest` framework and test coverage measured using the `coverage` package. To run tests use the make command:
```
make test
```
or for html output:
```
make test_html
```

## Acknowledgements
Project based on the [Data Science Boilerplate](https://github.com/andrewjkuo/ds-boilerplate) template, which was influenced by [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/), [Kedro](https://kedro.org/) and [govcookiecutter](https://best-practice-and-impact.github.io/govcookiecutter/#govcookiecutter).

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
   pip install -U pip setuptools
   pip install -e .[dev]
   pre-commit install
   git init
   ```

   Alternatively, you can use the `make` command:
   ```bash
   make install
   git init
   ```

3. **Make Initial Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

### Usage

#### Data

- **Immutability**: Raw data should not be edited. Transform data through your processing pipeline.
- **Directory Structure**: Organize data into `01_raw`, `02_intermediate`, `03_model_input`, and `04_model_output`.

#### Pipelines

- **Prefect**: Prefect is the default orchestration tool but you are free to use whatever technology you like. If Prefect is selected:
   - **Task and Flow Definition**: Prefect tasks and flows are defined in `pipelines/tasks.py` and `pipelines/flows.py`.
   - **Execution**: Use the Makefile to spin up the Prefect server and manage pipelines.

#### Notebooks

- **Purpose**: Notebooks are for exploration and communication. Refactor useful code into the `src` directory.
- **Auto-reloading**:
  ```python
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