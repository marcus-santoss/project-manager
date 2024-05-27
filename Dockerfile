FROM docker.io/python:3.12.3-slim

WORKDIR /app
COPY ./pyproject.toml pyproject.toml

RUN apt-get update -y \
    && apt-get upgrade -y \
    && pip install poetry \
    && poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi --no-root --only main

COPY . .

EXPOSE 8000/tcp
CMD python manage.py migrate \
    && gunicorn ProjectManager.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 2 \
        --preload \
        --log-file - \
        --log-level=debug \
        --error-logfile -
