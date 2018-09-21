## Getting started

1. Sign up for Heroku

2. Install the Heroku CLI

- To check version: `$ heroku --version`
- To install: `$ brewinstall heroku/brew/heroku`

3. From your terminal, `$ heroku login`

4. Inside virtualenv, install new dependencies in your project/repo directory:

- `$ pipenv install gunicorn` - the webserver for Heroku to use (rather than the one built-in to Django)
- `$ pipenv install psycopg2-binary` - PostgreSQL client binaries
- `$ pipenv install dj-database-url` - enables parameterizing the database connection (so Heroku uses PostgreSQL but local is still SQLite)
- `$ pipenv install python-decouple` - set important/secret values as environment variables
- `$ pipenv install whitenoise` - optimizes deployment of static files (you may not have any, but it's good to add this now)

5. Inside virtualenv, create a requirements.txt file in your project root directory with the command: `pip freeze > requirements.txt`

## Preparing your project

1. Copy this dotenv info to `.env` in your repository (this should be on `.gitignore`)

# Example env vars - rename to .env and customize (don't check in)

```
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL="sqlite:///db.sqlite3"

# Change the secret key! In your Django shell:
# from django.utils.crypto import get_random_string
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# get_random_string(50, chars)

SECRET_KEY="+x0ifha!f@*u5f1(c6x#ibaic@di-av=7v-zr&-^=2!e(l4vk2"
DEBUG=True
```

2. ALLOWED_HOSTS and DATABASE_URL are probably already correct for your local environment, but read/understand them

3. Inside a python repl: `./manage.py shell` generate a new secret key: 

```
>>> import random

>>> ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
```

4. `djorg/settings.py` will need a new import: `import dj_database_url`

5. Change `ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])`

6. Change 

```
DATABASES = {
    'default': dj_database_url.config('DATABASE_URL', default='sqlite:///db.sqlite3')
}
```

![dj_database_url explained](https://ibin.co/4GTpOlxF3pp2.png)

7. Create a Procfile in root directory with the following line of code

```
web: gunicorn djorgnotes.wsgi
```

8. Configure whitenoise by adding the following: `'whitenoise.middleware.WhiteNoiseMiddleware',` to `MIDDLEWARE = []` in `settings.py`

```
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## Creating a Heroku project

1. Makes the project and add Heroku as a remote to your git repository so you can push to it to deploy

```
$ heroku create blakes-djorg-notes
```

2. Make a PostgreSQL database associated with the project (and set the `DATABASE_URL` Heroku config var, equivalent to a local environment variable)

```
$ heroku addons:create heroku-postgresql:hobby-dev
```

3. Login to Heroku.com and set the config vars: 

```
ALLOWED_HOSTS=.herokuapp.com, 
DEBUG=False,  
SECRET_KEY=somenewsecret
```

4. Make sure you're all committed. Then `$ git push heroku master`