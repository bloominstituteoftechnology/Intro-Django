For the deployment process to Heroku I followed the steps laid out in the readme. I had my Heroku CLI installed from a previous back end project so I was able to skip ahead to installing the needed packages of gunicorn, psycopg2, dj-databse-url, and whitenoise (python-decouple was previously installed for local testing). Once the packages were installed deployment completed releatively easily, but unfortunately easy deployment is not the same as a working deployment.

When trying to access the server via browser I kept receiving status errors of 400 or 500. After some debugging I came to the realization that my code was missing the STATIS_ROOT element in settings.py (this element was mentioned in the documentation, but was listed after the fact and not emphasized as needed for proper implementation)and that my DATABASE setup needed to be cleared and a default value added:

<!-- STATIC_ROOT = os.path.join(BASE_DIR, 'static') -->

<!-- DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600) -->

Once these elements were updated/added and migrations were completed the server was fully functional and was completely accessible via browser with all the expected functionality.