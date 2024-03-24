from setuptools import find_packages, setup

setup(
    name="{{ cookiecutter.repo_name }}",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    version="0.1.0",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author_name }}",
)
