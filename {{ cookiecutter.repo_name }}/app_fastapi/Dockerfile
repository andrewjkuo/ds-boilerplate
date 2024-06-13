FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install -U pip setuptools wheel

COPY src src
COPY pyproject.toml pyproject.toml
RUN pip install .

COPY app_fastapi/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app_fastapi/main.py main.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]