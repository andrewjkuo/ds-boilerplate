from prefect import flow, serve
import os
from dotenv import load_dotenv
from {{cookiecutter.package_name}}.utils.util import yaml2dict

from tasks import hello_task

# Load environment variables
load_dotenv()
environment = os.getenv("ENV", "production")

# Load public config
params = yaml2dict("conf/parameters.yaml")


@flow
def hello_flow():
    hello_task()


if __name__ == "__main__":
    deployment = hello_flow.to_deployment(name="hello_flow")
    serve(deployment)
