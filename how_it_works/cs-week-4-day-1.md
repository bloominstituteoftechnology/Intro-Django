Django is, like Python, a pragmatic “one right way to do it” system, specifically a web application framework built on the principles of convention over configuration and fast iterative design. The Django ecosystem bills itself as “the web framework for perfectionists with deadlines” - these many included features are what makes it quick to build an MVP with. 

Objectives

* setup and use basic Python/Django development environment
* describe and use the Django migration system
* add a data model to Django
* add data to the database using a Python shell
* use a .env file to track `SECRET_KEY` and other variables

## Setting up and using basic Python/Django development environment

1. Create a pipenv virtual environment:

```
$ pipenv --three
```

`--three` option tells it to use Python3

2. Verify that the `Pipfile` was created in the root of the repo.

3. Activate pipenv with `$ pipenv shell`

You should see the command line change to the name of your repo/folder followed by a dash and a random string.

4. Once you are in the virtual environment, install django:

```
$ pipenv install django
```

5. Start a project with `django-admin startproject [name_of_project] .`

Replace `[nameofproject]` with the name of your project. The `.` tells it to create the project in the current directory. Otherwise, it would create a project in a subdirectory called [name_of_project]. 

Navigate to the [name_of_project] folder with `$ cd [name_of_project]` to make sure it was created and has boilerplate files such as `__init__.py`.

6. Start the server by navigating to the project folder root/[name_of_project] and running `$ ./manage.py runserver`

## Describing and using the Django migration system

**What are migrations?** 

The mapping between the classes that exist and the SQL database. This mapping is called migrations and Django is great at doing this. The migrate code takes a model, turns it into a table, and creates a SQL out of it. When we initialize a Django app, migrations are created. We can see these by running `./manage.py showmigrations`

**What is the SQL behind migrations?** 

To take a closer look at what is being done, you can look at the SQL queries that Django is building. This step is entirely optional, and is only for the curious–which should be you!

```
./manage.py sqlmigrate [package_name] [migration_id]
# for example
./manage.py sqlmigrate admin 0001_initial
```

**How to apply migrations?**

To actually run the migrations, use:

```
./manage.py migrate
```

Check them by showing migrations again: `./manage.py showmigrations`. The list of migrations should show an `[X]` for each item. Run the server again with `./manage.py runserver` and confirm that the migration warning is not present. There won’t be a change to the actual page that renders. After you migrate, there will also be a `db.sqlite3` (the sqlite database that was just created - it has tables for all of the info you migrated) that wasn't in the root directory before.

## Adding a data model to django

**What is a model?** 

At the core of Django, your data is represented by models. Django automatically translates actions on the models into a variety of other things: SQL statements, API endpoints, and so on.

In the `notes` folder, open `models.py`.

Create a class called `notes` that inherits from `models.Model` (This gives our new class access to all of the built-in functionality in models.Model) and add the following variables to the class:

```
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
```

We also need something to serve as a unique identifier for each record. We’ll use something called a UUID (Universally unique identifier) for this:

```
from uuid import uuid4 # First, import the library

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # Second, add the field
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
```

* Primary key is how the database tracks records.
* Default calls a function to randomly generate a unique identifier.
* We make editable false because we never want to change the key.
* Put it at the top of the list of fields because it’s sort of like the index for the record.

**How do we make migrations?** 

We need to tell the project that the app exists. 

1. Open `settings.py` from the project folder. Find the section for `INSTALLED_APPS` and add `'notes'`, or other apps as appropriate. In the console, check for migrations again with `./manage.py showmigrations`. The notes app should show up in the list now, but it has no migrations.

2. To generate the migrations, run: `$ ./manage.py makemigrations`. This will look at our models and see if any are newer than what's in the database then generate them if they are. (If you get an error that there are no changes to make, double-check that you have saved `models.py`). This makemigrations command will generate a file: `/notes/migrations/0001_initial.py` 

3. Show migrations again to make sure they appear, then do the migration: `./manage.py migrate`

## Adding data to the database using the python shell

There’s a Python shell built into Django that can be used to test the models and other Django entities that you create in the code. This can be a useful tool for experimenting and debugging.

**How do we launch the shell?**

`manage.py` has its own shell. Run `$ ./manage.py shell` to bring up a Python repl.

>>> The input line should change to 

**How do we import the model?**

```
>>> from notes.models import Note
```

`Note` should return the following

```
>>> Note
<class 'notes.models.Note'>
```

**How do we save new notes to the database?**

```
n = Note(title=”example”, content=”This is a test.”)
```

`n` should return the following

```
>>> n
<Note: Note object (1f0fe66d-dd30-4daa-84c1-fa7f5390a538)>
>>> n.title
'example'
>>> n.content
'This is a test.'
>>> n.id
UUID('1f0fe66d-dd30-4daa-84c1-fa7f5390a538')
```

Call `n.save()` to save the new note in the database

Exit the terminal - `exit()`, then restart it - `./manage.py shell`

We have to import the Note class again, using `from notes.models import Note`

There is another built in method that will retrieve all existing objects of a class: `Note.objects.all()` which will return `<QuerySet [<Note: Note object (1f0fe66d-dd30-4daa-84c1-fa7f5390a538)>]>`. Set `all_notes = Note.objects.all()` and view the first note with `all_note[0]`. This will return the following:

```
>>> all_notes[0]
<Note: Note object (1f0fe66d-dd30-4daa-84c1-fa7f5390a538)>
>>> all_notes[0].title
'example'
>>> all_notes[0].content
'This is a test.'
```

## Using a .env file to track the SECRET_KEY and other variables

Django uses its `SECRET_KEY` variable in `settings.py` for a variety of cryptographic purposes, it’s important that we keep it out of source control.

**How to use a .env file?**

1. We’re going to make use of a module called Python Decouple by installing it in the virtual environment: `pipenv install python-decouple`

2. Once it’s installed, we can bring it into settings.py with: `from decouple import config`

3. Remove the key from settings and add it to your .env file (creating it in your root folder if you have to):

```
SECRET_KEY='...whatever it was in the settings file...'
# Then change the line in settings.py to:
SECRET_KEY = config('SECRET_KEY')
```

4. We should also move DEBUG to the config file. Because the file is a string, and DEBUG expects a bool, we need to cast it: `DEBUG = config('DEBUG', cast=bool)`

We do this not for security, but so that it can be changed as needed on a development machine, without modifying the source code. Add `DEBUG = True` to .env as well.

5. Before moving on, verify that `.env` is in `.gitignore` and commit.

**Why shouldn't it be checked into source control?**

We can have different secret keys in development vs in production, or in development we might want debug to be true then in production, we might want debug to be false.