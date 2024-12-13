FROM python:3.11-alpine AS builder

RUN apk add --no-cache build-base libffi-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
