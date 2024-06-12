from prefect import task

@task
def hello_task():
    print("Hello world!")