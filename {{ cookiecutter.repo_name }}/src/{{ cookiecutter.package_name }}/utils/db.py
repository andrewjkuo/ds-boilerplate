{% if cookiecutter.database_type == 'postgres' -%}
import os
import psycopg2

def connect_to_postgres():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT')
    )
    return conn
{% elif cookiecutter.database_type == 'mysql' -%}
import os
import mysql.connector

def connect_to_mysql():
    conn = mysql.connector.connect(
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        host=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DB')
    )
    return conn
{% else -%}
def connect_to_dummy_database():
    print("No database type selected.")
{% endif -%}