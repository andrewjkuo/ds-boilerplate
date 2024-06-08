FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install -U pip setuptools wheel

COPY src src
COPY pyproject.toml pyproject.toml
RUN pip install .

COPY app_streamlit/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app_streamlit/app.py app.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]