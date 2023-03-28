FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN addgroup app && adduser -S -G app app

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update \
    && apk add python3 python3-dev mariadb-dev build-base libpq-dev \
    && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base \
    && pip install --upgrade pip \
    && pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --dev

COPY . /app/
RUN chmod +x /app/docker-entrypoint.sh 
RUN chown -R app:app /app
USER app

EXPOSE 8000
