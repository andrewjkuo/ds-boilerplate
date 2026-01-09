FROM python:3.11-slim-buster

WORKDIR /app

# Install uv (for package management)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Create and use a virtual environment for the app
RUN uv venv /app/.venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:${PATH}"
ENV UV_PYTHON=/app/.venv/bin/python

COPY src src
COPY pyproject.toml pyproject.toml
RUN uv pip install .

COPY app_fastapi/requirements.txt requirements.txt
RUN uv pip install -r requirements.txt

COPY app_fastapi/main.py main.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
