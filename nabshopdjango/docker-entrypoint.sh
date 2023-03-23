#!/bin/sh

# Wait for database to load
while ! nc -z db 3306 ; do
  echo "Waiting for the MySQL Server..."
  sleep 3
done

# Applying database migrations
echo "Applying database migrations..."

# Run the migrations
echo "Running migratoins..."
python manage.py migrate

# Populate the database with some sample data
echo "Populating the database with dummy data..."
python manage.py nabshopdb

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Start server
echo "Starting server..."
# python manage.py runserver 0.0.0.0:8000

gunicorn nabshopdjango.wsgi:application --bind 0.0.0.0:8000
