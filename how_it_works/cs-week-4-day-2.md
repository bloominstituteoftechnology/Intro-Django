Django is, like Python, a pragmatic “one right way to do it” system, specifically a web application framework built on the principles of convention over configuration and fast iterative design. The Django ecosystem bills itself as “the web framework for perfectionists with deadlines” - these many included features are what makes it quick to build an MVP with. 

Objectives

* set up and use the Django admin interface
* migrate models with new fields added
* subclass and specialize a model
* run SQL and ORM commands to investigate Django's SQL database

## Setting up and using the Django admin interface

1. Start the environment and server:

```
pipenv shell
./manage.py runserver
```

2. To make an admin account, run:

```
./manage.py createsuperuser
```
Add a user `admin` with whatever password you choose.

3. We need to tell the admin interface which tables we’re interested in seeing.

In the notes/admin.py file:
```
from .models import Note

# and register the Note model with the admin site with:

admin.site.register(Note)
```

## Migrating models with new fields added

* Adding new fields
* Making migrations
* Applying migrations

1. Open `notes/models.py` and add:

```
created_at = models.DateTimeField(auto_now_add=True)
last_modified = models.DateTimeField(auto_now=True)
```

2. In the terminal, make the migration:

```
./manage.py makemigrations
```

You will get the following:

```
You are trying to add the field ‘created_at’ with ‘auto_now_add=True’ to note
without a default; the database needs something to populate existing rows.

1) Provide a one-off default now (will be set on all existing rows)
2) Quit, and let me add a default in models.py
Select an option:
```

Default can sometimes be specified with:

```
foo = whateverField(default=value)

# Or you can allow the field to be blank with:

foo = whateverField(blank=True)
```

3. Use option 1 with suggested default of timezone.now.

```
 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
```

4. Do the migration: `./manage.py migrate`

If you run the server, you might notice that the new fields aren’t showing up in the admin interface. This is because when you use `auto_now`, the field gets set to read-only, and such fields aren’t shown in the panel.

5. Get the read-only fields to show up in the interface:

```
class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)
```

## Subclassing and specializing a model

* Add additional functionality to an existing model
* Create a new model in the process
* Django hides the database details

1. Create a new model that inherits from another: personal notes. Open up `notes/models.py`

2. Inherit from Note and add the additonal fields we need

```
class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

`on_delete` specifies that if the user gets delete, so too do the notes associated with that user

3. Access the built-in user functionality:

```
from django.contrib.auth.models import User
```

4. Get the read-only fields to show up in the interface:

```
from .models import Note, Tag, PersonalNote

admin.site.register(PersonalNote)
```

5. Migrate !!!

```
./manage.py makemigrations # to build a new migration

./manage.py makemigrations # to show the newly built migration

./manage.py migrate # to make the table

./manage.py runserver # to see changes on the server
```

6. You'll see 0 personal notes, so add one

## Running SQL and ORM commands to investigate Django's SQL database

* How does Django do things under the hood?

* How does Django's ORM functionality make things easier than SQL to access data?

1. We can take a look in the database with `./manage.py dbshell`

2. `.tables` will display a list of tables

3. `pragma table_info(notes_note);` will show column names and types for the table `notes_note`

4. `.headers on` and `.mode column` will adjust some settings to clean up the presentation if we open a table

5. We can look at all notes

```
sqlite> select * from notes_note;
a54425dbde5b45dcaa3ea99bbb1dfff6|Note example 1|This is a test.|2018-09-18 14:35:31.071071|2018-09-18 14:35:31.081006|tag
1b5d462d4e2146149f54964385f3eac0|Note example 2|This is a test.|2018-09-18 14:35:31.071071|2018-09-18 14:35:31.081006|tag
b6fa2285ea42477aa014693fe3a279b2|Personal note example 1|This is a test.|2018-09-18 14:54:50.444503|2018-09-18 14:54:50.444637|Example tag
```

6. We can look at personal notes

```
sqlite> select * from notes_personalnote;
b6fa2285ea42477aa014693fe3a279b2|1
```

We end up with a note pointer ID to the primary key of the note

7. We can look at users

```
sqlite> select id, username from auth_user;
1|blkfltchr
```

### We can look at usernames related to personalnotes 

We could do a big join to make this happen but Django makes this all happen under the hood

1. Drop out of the SQLite shell and open a Python shell with: `./manage.py shell`

2. Import personal notes: `from notes.models import Note, PersonalNote`

3. Pull the lists into variable: `pn = PersonalNote.objects.all()`

`notes = Note.objects.all()`

4. Take a look at the Personal note fields of the 0th record:

```
>>> pn[0].title
'Personal note example 1'
>>> pn[0].user
<User: blkfltchr>
```

5. Get a specific note using its primary key

```
>>> notes[2].id
UUID('b6fa2285-ea42-477a-a014-693fe3a279b2')

>>> n2 = Note.objects.get(pk='b6fa2285-ea42-477a-a014-693fe3a279b2')
>>> n2.title
'Personal note example 1'
>>> n2.content
'This is a test.'
```

Get lets us retrieve a specific field. We could also get using title, content, etc.

6. We can filter by partial strings

```
>>> n = Note.objects.filter(title__startswith='N')
>>> n
<QuerySet [<Note: Note object (a54425db-de5b-45dc-aa3e-a99bbb1dfff6)>, <Note: Note object (1b5d462d-4e21-4614-9f54-964385f3eac0)>]>
```