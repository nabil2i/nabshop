FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN addgroup app && adduser -S -G app app


# Required to install mysqlclient with Pip
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update \
    && apk add python3 python3-dev mariadb-dev build-base \
    && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system --dev

# Copy the application files into the image
COPY . /app/

# RUN chown -R app:app /app
# USER app

# Expose port 8000 on the container
EXPOSE 8000