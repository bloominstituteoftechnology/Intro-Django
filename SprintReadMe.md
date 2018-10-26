# Sprint-Challenge--Django-I

This week we got started with Django, and began making Djorg, a project for
personal organization applications. To close the week, the challenge is -
deploy! Getting your application out there is great to learn, shake out bugs,
and get feedback as you can share it with others.

Note: the instructions below assume you're on your `master` branch in git.

The steps to deploy (at a high level) are:

1. Sign up for [Heroku](https://www.heroku.com/)
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. From your terminal, `heroku login`
4. Get to your project/repo directory
5. Install new dependencies. (If using `virtualenv`, use `pip install` as you have been, or migrate to `pipenv`.)
   1. `pipenv install gunicorn` - the webserver for Heroku to use (rather than the one built-in to Django)
   2. `pipenv install psycopg2-binary` - PostgreSQL client binaries
   3. `pipenv install dj-database-url` - enables parameterizing the database connection (so Heroku uses PostgreSQL but local is still SQLite)
   4. `pipenv install python-decouple` - set important/secret values as environment variables
   5. `pipenv install whitenoise` - optimizes deployment of static files (you may not have any, but it's good to add this now)
   6. If using `virtualenv`, you need to create a `requirements.txt` file in your project root directory with the command: `pip freeze > requirements.txt`
6. Prepare your project
   1. Copy the `dotenv` file in this repository to `.env` in your repository (this should _not_ be checked in)
   2. `ALLOWED_HOSTS` and `DATABASE_URL` are probably already correct for your local environment, but read/understand them
   3. Use the example code (you can just run it in a `python` repl) to generate a new secret key and change `SECRET_KEY`
   4. `djorg/settings.py` will need new imports (`from decouple import config` and `import dj_database_url`)
   5. You can use `config` to load the environment variables you set above, e.g. `SECRET_KEY = config('SECRET_KEY')` (`ALLOWED_HOSTS` will be a little trickier, but that's why this is a sprint challenge!)
   6. For the database, you want to both load the `DATABASE_URL` and pass it to `dj_database_url.config` (see [documentation](https://github.com/kennethreitz/dj-database-url))
   7. Make a `Procfile` ([example](https://github.com/heroku/python-getting-started/blob/master/Procfile)) to tell Heroku what to run to start your app. (Hint: the name of your Django project is probably "djorg", not "gettingstarted".)
   8. Configure `whitenoise` (add a few configuration lines to your `settings.py` file per the [documentation](http://whitenoise.evans.io/en/stable/))
   9. Add static settings to your `settings.py`:
   ```
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'static')
   ```
7. `heroku create your-app` - makes the project and adds Heroku as a remote to your git repository so you can push to it to deploy
8. `heroku addons:create heroku-postgresql:hobby-dev` - makes a PostgreSQL database associated with the project (and sets the `DATABASE_URL` Heroku config var, equivalent to a local environment variable)
9. Set the other Heroku config vars, e.g. `ALLOWED_HOSTS=.herokuapp.com`, `DEBUG=False`, and `SECRET_KEY=somenewsecret` - see the [documentation](https://devcenter.heroku.com/articles/config-vars), you can set either via the Heroku CLI or by logging in to the Heroku Dashboard in your browser
10. Deploy! _First, make sure you're all committed_. Then `git push heroku master`

Once you've got it deployed, you'll probably need to run migrations on Heroku
(since it's using a different database then local). You can do this with
`heroku run python manage.py migrate`, and in general
`heroku run python manage.py` is the way to do all the helpful Django things,
just "in production." For example, `heroku run python manage.py createsuperuser`
is a good thing to do, and you can even administer/explore the app/data with
`heroku run python manage.py shell` and `heroku run python manage.py dbshell`.

Of course, chances are you'll run into things as you make your way through the
steps above - and that's okay! Some resource to help:

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) - official tutorial, has a full working example app if you want to step through with that before you try with Djorg
- [Lambda School Python/Django resources](https://github.com/LambdaSchool/Getting-Started/blob/master/PythonDjango.md)

You may also find the `heroku logs` command useful to diagnose errors, as Heroku
error messages are usually not that descriptive. And, while this is a sprint
challenge, it is okay to chat some about your progress and issues you hit - just
make sure you actually type and understand all of your own code, even if you are
finding it from somewhere else. It's also a good practice to note the resources
you use, as comments in your code and sharing them with others via Slack.

The review lecture will step over the above process, giving you a chance to
figure out any parts you miss. But please open a PR before then with:

- A link to your Djorg project repo
- A link to your live site, if you were able to deploy
- A `DeploymentExperiences.md` file where you write summarizing how the process went for you, what went well and what was tricky, and how far you got

For the writing portion, this is meant to practice your skills at
_professional_ writing - in the tech world, that means writing things clearly,
concisely, in a way to get the information across efficiently to an audience
that may be pretty busy (most people only skim most emails). Suggested length
~1-2 paragraphs, and bullet lists can be extremely effective.

Note for bash users: if you ever get in a place where your terminal isn't
printing out newlines properly and is not echoing your keypresses, hit `CTRL-C`
then blindly type in the following command and hit `RETURN`:

```
stty sane
```
