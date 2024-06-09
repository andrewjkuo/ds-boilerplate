# Makefile for {{cookiecutter.project_name}}

.PHONY: install
install:
	pip install -U pip setuptools wheel
	pip install -e .[dev]
	pre-commit install

{% if cookiecutter.include_streamlit_app in ['yes', 'y', 'YES', 'Y'] -%}

.PHONY: streamlit_build
streamlit_build:
	docker build -f app_streamlit/Dockerfile -t {{cookiecutter.repo_name}}_webapp .

.PHONY: streamlit_run
streamlit_run:
	docker run -p 8501:8501 {{cookiecutter.repo_name}}_webapp

{% endif -%}
{% if cookiecutter.include_fastapi_app in ['yes', 'y', 'YES', 'Y'] -%}

.PHONY: fastapi_build
fastapi_build:
	docker build -f app_fastapi/Dockerfile -t {{cookiecutter.repo_name}}_api .

.PHONY: fastapi_run
fastapi_run:
	docker run -p 8000:8000 {{cookiecutter.repo_name}}_api

{% endif -%}

.PHONY: test
test: install
	coverage run -m pytest
	coverage report -m

.PHONY: test_html
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