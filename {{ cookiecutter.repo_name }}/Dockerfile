FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update -y && apt-get install -y gcc

COPY requirements.txt requirements.txt
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

COPY src src
COPY setup.py setup.py
RUN pip install .

CMD ["bash"]