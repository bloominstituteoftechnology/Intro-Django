pipenv --three
pipenv shell
pipenv install django


django-admin startproject djorg .
django-admin startapp notes
./manage.py runserver