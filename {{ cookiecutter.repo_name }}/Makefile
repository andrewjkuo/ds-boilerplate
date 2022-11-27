.PHONY: build format install lint notebook req req_hooks test test_html

req:
	pip install -U pip setuptools
	pip install -r requirements.txt

req_hooks: req
	pre-commit install

install: req
	pip install -e .

build:
	docker build -t {{ cookiecutter.repo_name }} .

notebook: req
	jupyter notebook

test: req
	coverage run -m pytest
	coverage report -m

test_html: test
	python -m http.server --directory htmlcov/

lint:
	flake8 .

format:
	black .
