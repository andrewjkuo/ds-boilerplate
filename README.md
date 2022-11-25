# Data Science Boilerplate
A standardised project structure for doing and sharing data science work that enforces best practices.

This template has been heavily influenced by [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/), [Kedro](https://kedro.org/) and [govcookiecutter](https://best-practice-and-impact.github.io/govcookiecutter/#govcookiecutter) but I've added a few features of my own.

## Usage
1. Install cookiecutter.
   ```bash
   pip install cookiecutter
   ```
2. Start a new project. You will be prompted to enter some configuration values.
   ```bash
   cookiecutter gh:andrewjkuo/ds-boilerplate
   ```

## Project Structure
The directory structure of your new project looks like this:
```
├── Dockerfile             <- Dockerfile to build a basic image.
├── Makefile               <- Makefile with useful commands for project setup and running analysis.
├── README.md              <- The top-level README for developers using this project.
├── conf
│   ├── base               <- Configuration files that can be stored in source control.
│   └── local              <- Local secrets and credentials that should not be stored in source control.
├── data
│   ├── 01_raw             <- The original, immutable data dump.
│   ├── 02_intermediate    <- Intermediate data that has been transformed.
│   ├── 03_model_input     <- The final, canonical data sets for modeling.
│   └── 04_model_output    <- Outputs from models (e.g. predictions).
├── models                 <- Trained and serialised models or model summaries.
├── notebooks              <- Jupyter notebooks.
├── references             <- Data dictionaries, manuals and all other explanatory materials.
├── requirements.txt       <- The requirements file for reproducing the analysis environment.
├── setup.py               <- Makes project pip installable so src can be imported.
├── src                    <- Source code for use in this project.
│   ├── __init__.py        <- Make src a Python module.
│   └── data               <- Scripts to download or generate data.
│   └── features           <- Scripts to turn raw data into features for modeling.
│   └── model              <- Scripts to train models and make predictions.
│   └── utils              <- Scripts with utility functions.
│   └── visualisation      <- Scripts to create exploratory and results-oriented visualisations.
└── tests                  <- Tests for functions in src.
```

## Future
* Test this template in more environments.
* Explore using `poetry` for dependency management.
* Add the option to conditionally create files for specific kinds of projects based on cookiecutter prompts (e.g. a streamlit app or Flask API).
* Add functionality to automatically generate documentation.