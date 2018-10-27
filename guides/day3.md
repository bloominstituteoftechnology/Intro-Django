# Day 3: Setting up a RESTful API

## Installing the REST Framework

We’ll be using the django REST framework: http://www.django-rest-framework.org/

Open the shell if you aren’t in it and install the framework:

```
pipenv install djangorestframework
```

Next, we need to tell the project about this.  Open
`[name_of_project]/settings.py`

Under `INSTALLED_APPS` add `'rest_framework'` to the list.

We also need to add some boilerplate to set up permissions:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
```

This will allow read/write permissions for logged in users and read only for
anonymous users.

Launch the server and make sure everything is working, debug, and commit.

## Expose the PersonalNotes Model

Next, we need to add more boilerplate.  In the `notes` folder, create a new file
called `api.py`.  This will use something called serializers and viewsets to
describe which parts of the model we want to expose to the API.

First, in `api.py`, import the serializers:

```python
from rest_framework import serializers
```

We’ll also need to import the `PersonalNote` class so that we can use it here.

Convention is to name the serializer classes after what they are serializing.
It will inherit from the specific serializer we are using for this project:

```python
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
```

Inside this class, we will make an _inner class_ (nested class) called a `Meta`
to tell it what parts of the model we want to access:

```python
    # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
```

To visualize this, we will use something called a viewset.  Add `viewsets` to
what is being imported from `rest_framework`:

```python
from rest_framework import serializers, viewsets
```

Create a new class for this, using the same naming convention as the serializer
and inheriting from `viewsets.ModelViewSet`

```python
class PersonalNoteViewSet(viewsets.ModelViewSet):
```

Link this back to the serializer class we made previously:

```python
    serializer_class = PersonalNoteSerializer
```

Next, add which records to search for.  We could use filters here, but for now,
grab all of them:

```python
queryset = PersonalNote.objects.all()
```

There isn’t anything we can check just yet to ensure that this is working, but
let’s make sure we haven’t broken anything.

At this point, we should have:

```python
from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
```

Run the server, debug, commit.

## Add Routes

Lastly, we need to add a route to be able to access this functionality.  In the
project folder, open `urls.py`.

We’ll need to import two things here: router functionality for Django, and the
`PersonalNoteViewSet` we just created.

```python
from rest_framework import routers
from notes.api import PersonalNoteViewSet
```

Next, make a default router from the routers package, then register that router:

```python
router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)
```

This is similar to setting up a route in express, but we’re saying for this
route, this (`PersonalNoteViewSet`) is the data we want to associate with it.
(The `r` means that this is a regular expression, and to interpret the string as
literally as possible--somewhat overkill in this case.) 

Next, we need to add the URL to the `urlpatterns` list. In order to do that,
we'll be using a function called `include()` that we get from `django.urls`:

```python
from django.urls import path, include
```

And in `urlpatterns`:

```python
    path('api/', include(router.urls)),
```

This will set the path to `/api/notes`.  We can use `router.register` to add
as many paths as we want this way, without needing to add them to `urlpatterns`

## Test the API

Run the server, navigate to `/api/` and review the information there.  Click the
link to `notes` and review that as well.

Use the admin feature at the bottom to attempt to post a new note.  This will
fail.

The reason is that our `PersonalNote` model requires a username as well.  We
need to add that in.  

## Add the Required `user` Field, Use the Debugger

We can do that in our serializer by overriding a method from
`serializers.HyperlinkedModelSerializer` called `create`. This method needs to
return a new `PersonalNote` object constructed from the passed-in data, which is
in the `validated_data` parameter, like so by default:

In `api.py`, `PersonalNoteSerializer`:

```python
    # !!! Broken code still missing the user field

    def create(self, validated_data):
        note = PersonalNote.objects.create(**validated_data)
        return note
```

But we need to add the `user` field into the mix. If the user is logged in to
Django through this browser, that information is automatically included in the
request... but where? Let's use the debugger to explore and find out.

In `api.py`, `PersonalNoteSerializer`:

```python
    def create(self, validated_data):
        import pdb; pdb.set_trace()  # Start the debugger here
        pass
```

Run this and use the debugger to the data present at this breakpoint.  If you
dig into `self`, you will find eventually find a context with a request.  As an
educated guess, using what we’ve previously learned about requests, it is fair
to hypothesize that a user is associated with the request.  Try it out:

```python
self.context['request'].user
```

Exit the debugger and add a new variable in `create` to store the user retrieved
from the location in `self` that we just discovered. Feed it in to `PersonalNote.objects.create` as an additional keyword argument:

```python
    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note
```

This will add the needed data to the create method and allow the form to work.
Return to the `/api/notes/` page and test.  

You will receive a `201 Created` that may appear at first as if the data is
being overwritten.  Return to the main list page to confirm that everything is
being saved.  

Debug as needed, then commit.  

## Filter Results by User

Finally, we have one major problem remaining.  Right now, any user can request
and see all of the notes that are in the database.  We need to filter them so
that only the appropriate ones are returned.  Return to `api.py`,
`PersonalNoteViewSet`.

Change `queryset` to initialize with `Note.objects.none()`.  This will create
the variable with an empty dictionary of the correct type.  To make a decision
based on whether or not the user is anonymous, and return only the notes that
belong to the logged in user, we can override a method called
`get_queryset(self)`.

Load the user into a variable.  This class has access to the `request` directly,
so it can be found with `self.request.user`.  

```python
    def get_queryset(self):
        user = self.request.user
```

If `user.is_anonymous`, we can return an empty dictionary of notes.  Otherwise,
we can use a filter to return only the correct ones with
`Note.objects.filter(user=user)`.

```python
    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
```

Test, debug, and commit.

## Set up CORS

In order to get your site to run well with a front-end, you might need to set up CORS:

https://github.com/ottoyiu/django-cors-headers

After installation (_follow the instructions at the link, above!_), setting:

```python
CORS_ORIGIN_ALLOW_ALL = True
```

should be enough.

