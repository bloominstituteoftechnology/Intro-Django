Django is, like Python, a pragmatic “one right way to do it” system, specifically a web application framework built on the principles of convention over configuration and fast iterative design. The Django ecosystem bills itself as “the web framework for perfectionists with deadlines” - these many included features are what makes it quick to build an MVP with. 

Objectives

* set up the Django REST Framework and connect a model to an endpoint
* control which information is exposed based on the currently-logged-in user

## Setting up the Django REST Framework and connect a model to an endpoint

**Install the framework**

1. Open the shell if you aren’t in it and install the framework: `pipenv install djangorestframework`

2. Tell the project about this. Open `[name_of_project]/settings.py`

Under `INSTALLED_APPS` add `'rest_framework'` to the list.

3. We also need to add some boilerplate to set up permissions:

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
```

This will allow read/write permissions for logged in users and read only for anonymous users.

**Expose the PersonalNotes model**

1. In the `notes` folder, create a new file called `api.py`

2. Import the serializers and import the PersonalNote class from models:

```
from rest_framework import serializers
from .models import PersonalNote
```

3. Name the serializer classes after what they are serializing. We need to register the model and the fields within the model we're interested in. 

```
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
```

4. Add viewsets to what is being imported from rest_framework: `from rest_framework import serializers, viewsets`

5. Create a new class for this, using the same naming convention as the serializer and inheriting from `viewsets.ModelViewSet`

6. Link this back to the serializer class we made previously and add which records to search for. We could use filters here, but for now, grab all of them:

```
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
```

7. Run the server, debug, commit.

**Add routes**

1. In the project folder, open `urls.py`.

2. Import two things here: router functionality for Django, and the `PersonalNoteViewSet` we just created

```
from rest_framework import routers
from notes.api import PersonalNoteViewSet
```

3. Make a default router from the routers package, then register that router:

```
router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)
```

We'll have a variety of endpoints here, all under the api path

4. Add the URL to the `urlpatterns` list. In order to do that, we’ll be using a function called `include()` that we get from `django.urls`:

```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

This will set the path to `/api/notes`. We can use `router.register` to add as many paths as we want this way, without needing to add them to urlpatterns

5. Run the server: `./manage.py runserver`, navigate to `/api/notes` and review the information there

## Controlling which information is exposed based on the currently-logged-in user

**Add an additional `user` field when creating a `PersonalNote`**

We can do that in our serializer by overriding a method from `serializers.HyperlinkedModelSerializer` called `create`. This method needs to return a new `PersonalNote` object constructed from the passed-in data, which is in the `validated_data` parameter, like so by default:

1. Override create functionality by creating a new PersonalNote and passing in validated data

```
def create(self, validated_data):
        note = PersonalNote.objects.create(**validated_data)
        return note
```
2. Add the user `field` into the mix. If the user is logged in to Django through this browser, that information is automatically included in the request… Use the debugger to explore and find out.

```
def create(self, validated_data):
        import pdb; pdb.set_trace()  # Start the debugger here
        note = PersonalNote.objects.create(**validated_data)
        return note
```

3. Use input `l`, `self` and `validated_data` in the python debugger to list where we are (the line with the arrow (12) is the line that's about to execute)

```
-> note = PersonalNote.objects.create(**validated_data)
(Pdb) l
  7             model = PersonalNote
  8             fields = ('title', 'content')
  9
 10         def create(self, validated_data):
 11             import pdb; pdb.set_trace()  #Start the debugger here
 12  ->         note = PersonalNote.objects.create(**validated_data)
 13             return note
 14
 15
 16     class PersonalNoteViewSet(viewsets.ModelViewSet):
 17         serializer_class = PersonalNoteSerializer
 ```

 ```
 (Pdb) self
PersonalNoteSerializer(context={'request': <rest_framework.request.Request object>, 'format':None, 'view': <notes.api.PersonalNoteViewSet object>}, data=<QueryDict: {'csrfmiddlewaretoken': ['z43Qj31CciLPuHwsZIwSDWJzqoqfoyjGvoucTCD2mcdyiNpitfzp6iFGF3a2MmVe'], 'title': ['test2'], 'content': ['test2']}>):
    title = CharField(max_length=200)
    content = CharField(allow_blank=True, required=False, style={'base_template': 'textarea.html'})
```

```
(Pdb) validated_data
{'title': 'test2', 'content': 'test2'}
```

4. As an educated guess, using what we’ve previously learned about requests, it is fair to hypothesize that a user is associated with the request. Try it out:

```
self.context['request'].user
```

5. Exit the debugger and add a new variable in `create` to store the user retrieved from the location in `self` that we just discovered. Feed it in to `PersonalNote.objects.create` as an additional keyword argument:

```
    def create(self, validated_data):
        user = self.context[‘request’].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note
```

6. Return to the `/api/notes/` page and test.

You will receive a `201 Created` that may appear at first as if the data is being overwritten. Return to the main list page to confirm that everything is being saved

**Filter results by currently-logged-in user**

Finally, we have one major problem remaining. Right now, any user can request and see all of the notes that are in the database. We need to filter them so that only the appropriate ones are returned.

1. Return to `api.py`, `PersonalNoteViewSet`

2. Change `queryset` to initialize with `Note.objects.none()`: 

This will create the variable with an empty dictionary of the correct type

3. To make a decision based on whether or not the user is anonymous, and return only the notes that belong to the logged in user, we can override a method called `get_queryset(self)`

```
    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
```

4. If `user.is_anonymous`, we can return an empty dictionary of notes. Otherwise, we can use a filter to return only the correct ones with `Note.objects.filter(user=user)`.

5. Test, debug, and commit.