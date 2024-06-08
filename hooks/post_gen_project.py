import os
import shutil


repo_name = "{{cookiecutter.repo_name}}"
include_streamlit_app = "{{cookiecutter.include_streamlit_app}}"
include_fastapi_app = "{{cookiecutter.include_fastapi_app}}"

repo_path = os.getcwd()

if include_streamlit_app.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(repo_path, 'app_streamlit'))

if include_fastapi_app.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(repo_path, 'app_fastapi'))
