# Makefile for {{cookiecutter.project_name}}

.PHONY: install
install:
	pip install -U pip setuptools wheel
	pip install -e .[dev]
	pre-commit install

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
	prefect server start

.PHONY: stop-prefect-server
stop-prefect-server:
	pkill -f "prefect server"

.PHONY: deploy-prefect
deploy-prefect:
	python pipelines/flows.py

{% endif -%}

.PHONY: test
test: install
	coverage run -m pytest
	coverage report -m

.PHONY: test-html
test_html: test
	python -m http.server --directory htmlcov/

.PHONY: lint
lint:
	flake8 .

.PHONY: format
format:
	black .

.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete