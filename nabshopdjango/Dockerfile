FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN addgroup app && adduser -S -G app app

# Required to install mysqlclient with Pip
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update \
    && apk add python3 python3-dev mariadb-dev build-base libpq-dev \
    && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base \
    && pip install --upgrade pip \
    && pip install pipenv


# RUN mkdir -p /vol/web/static \
#     && mkdir -p /vol/web/media \
#     && chown -R app:app /vol \
#     && chmod -R 755 /vol

# ENV PATH="/py/bin:$PATH"

# Install pipenv
# RUN pip install --upgrade pip 
# RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/

# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system --dev

# Copy the application files into the image
COPY . /app/
RUN chmod +x /app/docker-entrypoint.sh 
RUN chown -R app:app /app
USER app

# Expose port 8000 on the container
EXPOSE 8000
