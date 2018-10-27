# Day 2: Admin Interface and SQL

## Admin Interface

Now let’s take a look at the admin functions.

Start the environment and server:
```
pipenv shell
./manage.py runserver
```

Open the page in the web browser and navigate to the admin page:
`localhost:8000/admin`.  You will see a login page, but we don’t have an account
to log in with yet.

To make an admin account, run:
```
./manage.py createsuperuser
```

Add a user `admin` with whatever password you choose.

Although it can be tempting to use a short and easy password for things like
this, it is good practice to use a robust passphrase.  You don’t want to forget
and leave a superuser account with a weak password and have it pass to
production.

Run the server and log into the admin account you just created.  You will be
able to see the automatically generated users and groups from the database, but
our notes are missing.

We need to tell the admin interface which tables we're interested in seeing.

In the `notes/admin.py` file:

```python
from .models import Note
```

and register the `Note` model with the admin site with:

```python
admin.site.register(Note)
```

Return to the site admin page.  `Notes` should now be present.  Try adding
and/or editing a few.

If you want to register more models, you can do so with additional `register()`
calls:

```python
admin.site.register(Note)
admin.site.register(PersonalNote)   # etc.
```

## Migrations with New Fields

It would also be nice to track created and modified dates.  

Open `notes/models.py` and add:

```python
created_at = models.DateTimeField(auto_now_add=True)
last_modified = models.DateTimeField(auto_now=True)
```

The argument we are using determines when and how this information should be
updated:  `auto_now_add` only sets on create, while `auto_now` will set on both
create and update.

In the terminal, make the migration:
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
```python
foo = whateverField(default=value)
```

Or you can allow the field to be blank with:
```python
foo = whateverField(blank=True)
```

But this _will not work_ in a `DateTimeField` with `auto_now` or `auto_now_add`
set, so use option 1 with suggested default of `timezone.now`.

Do the migration: `./manage.py migrate`

You might notice that the new fields aren't showing up in the admin interface. This is because when you use `auto_now`, the field gets set to read-only, and such fields aren't shown in the panel.

To get the read-only fields to show up in the interface:

```python
class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)
```

## Personal (per-user) Notes

Next we want to add the ability to handle multiple users, and allow them to have
their own personal notes.

First, we will create a new model that inherits from another: personal notes.
Open up `notes/models.py`

To access the built-in user functionality:
```python
from django.contrib.auth.models import User
```

We could copy and paste the previous notes class to do this, but a better way is
to have it inherit from it and just add the additional fields we need.

```python
class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

What this is doing is importing Django’s built in user class model with
something called a _foreign key_ to create a reference to data on another table.
It works sort of like a pointer in C.

`on_delete=models.CASCADE` helps with the integrity of the data.  In relational
databases, one of the principles is to protect consistency.  There shouldn’t be
an item in one table that references the foreign key of something that has been
removed from another.  Check the readme in the repo for more info.

## Under the Hood with SQL

We can take a look in the database with `./manage.py dbshell`.  If you get an
error, you may need to install sqlite3 using your preferred method.

If it is working, the command prompt will change to `sqlite`.

`.tables` will display a list of tables

`pragma table_info(notes_note);` will show column names and types for the table
`notes_note`.

`.headers on` and `.mode column` will adjust some settings to clean up the
presentation if we open a table.

`SELECT * FROM notes_note;` is a sql command that will select all of the columns
in the notes_note table and display the data present.  By convention, sql
commands are often uppercase, but it is actually case insensitive.

All the notes we have created will be displayed.

Be _very_ careful with sql commands.  The command `DROP` will permanently delete
a table and all of the data inside it without warning. _This language is
powerful and has no mercy_.

Type `.exit` or `CTRL-D` to get out of dbshell.

Back in the virtual environment, because we modified the model to add personal
notes, we need to do another migration.

Complete the migration process as before.  

We also want personal notes to show up on the admin page. Open `admin.py` then
import and register the new class.  Remember, you can use tuples for both of
these.  Don’t forget to use the extra parentheses inside the register function.

Take a look at it in `admin`.  It should be the same as before, but now we have
a `user` field that is automatically populated.

We can use the admin interface to add more users in the user table, if we want.

For now, create a personal note for the admin account.

Go back to the sql shell, and take a look at the `notes_personalnote` table.

You’ll need to use the same three commands as above to display the table.  Note
that the info here is very different.  Instead of having everything, it just has
`user_id` and a foreign key `note_ptr_id`, pointing to a record in the full
notes table.

Take a look at the `notes_note` table.  The rest of the data will be here,
listed under the uuid stored in `note_ptr_id`, a reference by the foreign key.
This is why relational databases are relational.

The `user_id` is also a foreign key that points to Django's built-in `auth_user`
table. Run a `SELECT` query to look in that table, as well.

## Django ORM compared to SQL

Drop out of the SQLite shell and open a Python shell with `./manage.py shell`.

Import personal notes: `from notes.models import PersonalNote`

Pull the list into a variable: `pn = PersonalNote.objects.all()`

Take a look at the name of the 0th record: `pn[0].user`.  Try other fields as
well.

Django lets us access information that is in multiple tables relatively easily.
The sql details are hidden from us (in a good way!).  It does all of the under
the hood operations for us.
