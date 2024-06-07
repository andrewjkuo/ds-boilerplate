# GLOBALS

# COMMANDS

.PHONY: install
install:
	pip install -U pip setuptools wheel
	pip install -e .[dev]
	pre-commit install

.PHONY: build
build:
	docker build -t {{ cookiecutter.repo_name }} .

.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

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
