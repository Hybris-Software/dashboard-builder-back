FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

WORKDIR /djangoapp
COPY ./scripts /scripts/
COPY ./djangoapp .

ENTRYPOINT ["/scripts/docker/entrypoint.sh"]
