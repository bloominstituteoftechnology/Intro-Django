release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
web: gunicorn django_blue.wsgi --log-file -