import os
{% if cookiecutter.cloud_provider == 'aws' -%}
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

ENV = os.getenv("ENV", "production")


def connect_to_aws_s3():
    try:
        if ENV == "production":
            s3 = boto3.client("s3")
        else:
            s3 = boto3.client(
                "s3",
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                region_name=os.getenv("AWS_REGION"),
            )
        return s3
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error in AWS S3 connection: {e}")
        return None
{% elif cookiecutter.cloud_provider == 'gcp' -%}
from google.cloud import storage
from google.oauth2 import service_account

ENV = os.getenv("ENV", "production")


def connect_to_gcp_storage():
    try:
        if ENV == "production":
            client = storage.Client()
        else:
            credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            if credentials_path:
                load_credentials = service_account.Credentials
                credentials = load_credentials.from_service_account_file(
                    credentials_path
                )
                client = storage.Client(credentials=credentials)
            else:
                client = storage.Client()
        return client
    except Exception as e:
        print(f"Error in GCP Storage connection: {e}")
        return None
{% elif cookiecutter.cloud_provider == 'azure' -%}
from azure.storage.blob import BlobServiceClient

ENV = os.getenv("ENV", "production")


def connect_to_azure_blob():
    try:
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        blob_client = BlobServiceClient.from_connection_string(connect_str)
        return blob_client
    except Exception as e:
        print(f"Error in Azure Blob connection: {e}")
        return None
{% else -%}
def connect_to_dummy_storage():
    print("No cloud provider selected.")
{% endif -%}
