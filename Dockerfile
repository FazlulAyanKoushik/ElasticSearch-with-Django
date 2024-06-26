# Base build image
FROM python:3.10-alpine as base
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

COPY . /app/

# Here we install the dependencies for the project and remove them after the build is done to keep the image size small as possible.
RUN apk add --update --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    libpq

RUN pip install -r /app/requirements.txt
