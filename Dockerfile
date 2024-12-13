FROM python:3.11-alpine AS builder

LABEL title="Flask application DOCKER TP"\
    version="1.0.0" \
    created="2024-12-13"

RUN apk add --no-cache build-base libffi-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-alpine

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY app.py .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]