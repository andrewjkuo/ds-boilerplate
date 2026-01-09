# Makefile for {{cookiecutter.project_name}}
UV ?= uv
UV_PROJECT_ENVIRONMENT ?= .venv
export UV_PROJECT_ENVIRONMENT

.PHONY: install
install:
	$(UV) sync --extra dev
	$(UV) run pre-commit install

{% if cookiecutter.include_streamlit_app in ['yes', 'y', 'YES', 'Y'] -%}

.PHONY: streamlit-build
streamlit-build:
	docker build -f app_streamlit/Dockerfile -t {{cookiecutter.repo_name}}_webapp .

.PHONY: streamlit-run
streamlit-run:
	docker run -p 8501:8501 {{cookiecutter.repo_name}}_webapp

{% endif -%}
{% if cookiecutter.include_fastapi_app in ['yes', 'y', 'YES', 'Y'] -%}

.PHONY: fastapi-build
fastapi-build:
	docker build -f app_fastapi/Dockerfile -t {{cookiecutter.repo_name}}_api .

.PHONY: fastapi-run
fastapi-run:
	docker run -p 8000:8000 {{cookiecutter.repo_name}}_api

{% endif -%}
{% if cookiecutter.use_prefect in ['yes', 'y', 'YES', 'Y'] -%}

.PHONY: start-prefect-server
start-prefect-server:
	$(UV) run prefect server start

.PHONY: stop-prefect-server
stop-prefect-server:
	pkill -f "prefect server"

.PHONY: deploy-prefect
deploy-prefect:
	$(UV) run python pipelines/flows.py

{% endif -%}

.PHONY: test
test: install
	$(UV) run coverage run -m pytest
	$(UV) run coverage report -m

.PHONY: test-html
test_html: test
	$(UV) run python -m http.server --directory htmlcov/

.PHONY: lint
lint:
	$(UV) run pflake8 .

.PHONY: format
format:
	$(UV) run black .

.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
