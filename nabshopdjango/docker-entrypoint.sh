#!/bin/sh
#!/bin/sh

while ! nc -z db 3306 ; do
  echo "Waiting for the MySQL Server"
  sleep 3
done


# Apply database migrations
echo "Apply database migrations"
# python manage.py nabshop
python manage.py migrate


# echo "Collection static"
python manage.py collectstatic

# Start server
echo "Starting server"
python manage.py runserver

# gunicorn nabshopdjango.wsgi:application --bind 127.0.0.1:8000
