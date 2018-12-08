# Django Deployment
1. Packages Needed
    - `gunicorn`
        - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
        - Installation:
            - `pipenv install gunicorn` in the virtual shell.
            - `heroku config:set WEB_CONCURRENCY=3`
                - You can have 2-4 processes running on a Django app at any given time on `free`, `hobby`, `standard-1x` dynos. Web concurrency is set by default if you leave this blank. You should know the memory requirements of your application before setting this, and it defaults to 3 as a sensible default.
            - create a file in the root directory call `Profile`
                - type in the file `web: gunicorn message:app_name
                - you can set a custom timeout via `gunicorn hello:app --timeout 10
                - If you app has memory leakage then you can restart workers after a given number of requests via `gunicorn hello:app --max-requests 1200`
    - `psycopg2`
        = Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
        - Installtion
            - pipenv install psycopg2
            - No further requirments at this point, but you can visit `http://initd.org/psycopg/docs/` for more infomation and advanced documentation.
    - dj-database-url
        - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application. The dj_database_url.config method returns a Django database connection dictionary, populated with all the data specified in your URL. There is also a conn_max_age argument to easily enable Django’s connection pool.
        - installation
            - pipenv install dj-database-url
            - inside of settings.py of your project do `import dj_database-url`
            - Add this as well to the same file below the default one to configure the database for postgres in production and sqlite3 in development:
            ```
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
            ```
    - `python-decouple`
        - Decouple helps you to organize your settings so that       you can change parameters without having to redeploy       your app.
        ```
            It also makes easy for you to:

            1. store parameters on ini or .env files;
            2. define comprehensive default values;
            3. properly convert values to the correct data type;
            4. have only one configuration module to rule all your instances.
            
            It was originally designed for Django, but became an independent generic tool for separating settings from code.
        ```
        - create a .env file in the root directory and enter your key=value pairs for your data you want to keep secret.
        Inside the file where said variables are being used, import it at the top of the file via `from decouple import config` and then do something to the effect of `DEBUG = config('DEBUG', default=False, cast=bool)` the cast will convert your .env string to whatever you are typecasting it to and default sets it to a default value when it is left blank.
    - `pipenv install whitenoise`
        - With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS providers.)
        - WhiteNoise takes care of best-practices for you, for instance:
            1. Serving compressed content (gzip and Brotli formats, handling Accept-Encoding and Vary headers correctly)
            2. Setting far-future cache headers on content which won’t change
        - installation
            - `pipenv install whitenoise`
            - 
            ```
                MIDDLEWARE = [
                     # 'django.middleware.security.SecurityMiddleware',
                     'whitenoise.middleware.WhiteNoiseMiddleware',
                ]
            ```
            - `whitenoise.middleware.WhiteNoiseMiddleware` **should be placed *DIRECTLY* below** `django.middleware.security.SecurityMiddleware`
            - To add forever-cacheable files and compression support add the following code to the bottom of your `settings.py` folder.
                - `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`
            - refer to http://whitenoise.evans.io/en/stable/ for more advanced documentation.
    - If you are using a virtual environment then you shoul create requirements.txt file to have file to let various places like Heroku or other developers know what requirements are needed for your project. Simpley run the following code in the root of your project. This takes a look at your currently installed extensions, creates a file called `requirements.txt` and then stores the extensions as a key=value pair listing. With the key being the extension package and the value being the version you are using.
        - `pip freeze > requirements.txt`

    - Heroku
        - Make sure everything is up-to-date for your repo via
            1. `git add .`
            2. `git commit -m "descriptive message"`
            3. `git push`
        - After that push to heroku
            1. `heroku create app_name`
            2. `git push heroku master`
        - Once deployed you need to run model migrations via:
            `heroku run ./manage.py migrate` - for existing migrations. If you have new migrations then run `heroku run ./manage.py makemigrations` like you would locally and then migrate afterwards.
            - Next create a super user for the heroku postgresql database via:
                `heroku run createsuperuser`
            - You will be prompted a series of questions for the super user's `username`, `email`, and `password`&`confirm password`.

If you can visit your application and everything is working then congratulations! You are now published in production on Heroku using Postgresql!

___

# Logging Experience with Heroku

I ran the command **`heroku logs`** to get my logs in the CLI.

Here is the result:

![heroku logs for sprint challenge](logs.png)

___

# Sprint Questions

Summarize the key steps in the deployment process.
1.  What went well?
    - The entire process went pretty well. I did have some trouble with ALLOWED_HOSTS causing my page to show a 404 error, but that was fixed by adding the name of my app into the ALLOWED_HOSTS array.
    
2. What challenges did you face?
    - Setting up ALLOWED_HOSTS.
3. How far did you get?
    - I was able to fully deploy my application with day 4 work completed.
4. Which docs did you think were the most helpful?
    - The docs for whitenoise were extremely useful and easy to setup. The dj_database_url docs were useful but were more confusing to setup.
5. Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past.
    - I liked the whitenoise docs because it was only like one step to get everything setup for the basics, and then there was more if you wanted to get more fancy. I know that many docs are not set up to configure this easily. Also, the docs