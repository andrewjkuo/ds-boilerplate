import os
import shutil

include_streamlit_app = "{{cookiecutter.include_streamlit_app}}"
include_fastapi_app = "{{cookiecutter.include_fastapi_app}}"
use_prefect = "{{cookiecutter.use_prefect}}"

proj_path = os.getcwd()
utils_dir = os.path.join(proj_path, "src", "{{cookiecutter.package_name}}", "utils")

# Remove unnecessary app templates
if include_streamlit_app.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(proj_path, 'app_streamlit'))

if include_fastapi_app.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(proj_path, 'app_fastapi'))

if use_prefect.lower() not in ['yes', 'y']:
    os.remove(os.path.join("pipelines", "tasks.py"))
    os.remove(os.path.join("pipelines", "flows.py"))

# Remove unnecessary utility functions
if "{{cookiecutter.cloud_provider}}" == 'none':
    os.remove(os.path.join(utils_dir, "cloud_storage.py"))

if "{{cookiecutter.database_type}}" == 'none':
    os.remove(os.path.join(utils_dir, "db.py"))
