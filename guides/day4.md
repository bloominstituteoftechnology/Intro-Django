--------------------
# Day 4: Token Auth for REST

The Django Rest Framework also provides token authorization.  We will use this
to allow other users to login and access the data specific to them.  Information
can be found here:

http://www.django-rest-framework.org/api-guide/authentication/#authentication


## Set up Token Authentication

Open `settings.py`.

To `INSTALLED_APPS`, add `rest_framework.authtoken`.

If you need them elsewhere, immediately before the boilerplate for `REST_FRAMEWORK`, import `SessionAuthentication`, `BasicAuthentication`, and `TokenAuthentication` from `rest_framework.authentication`

In `REST_FRAMEWORK`, add:

```python
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
```

## Set up the Route

Next, we need to set up the route to authenticate users.  In `urls.py`:

Import `re_path` from `django.urls` and `views` from `rest_framework.authtoken`

```python
from django.urls import path, include, re_path
from rest_framework.authtoken import views
```

Then add the endpoint in `urls.py` by adding the `api-token-auth/` route to
`urlpatterns`:

```python
    re_path(r'^api-token-auth/', views.obtain_auth_token)
```

The `^` is means "match the beginning of the string" in a regular expression.
The `re_path` function is just like `path`, except it interprets the endpoint as
a regex instead of a fixed string.

Do a migration to set up the database.

## Test the Endpoint

We can test this on the bash command line with the [curl](https://curl.haxx.se/)
utility that you might already have installed. (Postman also works.)

Mac/Linux:
```
# The following makes a POST request with the given JSON payload:

curl -X POST -H "Content-Type: application/json" -d '{"username":"admin", "password":"PASSWORD"}' http://127.0.0.1:8000/api-token-auth/
```

Windows command prompt (or other platform if the above doesn't work):

```
# Windows needs some more double quotes and escaping of the payload

curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"admin\", \"password\":\"qazxswedcvfrtgbnhy\"}" http://127.0.0.1:8000/api-token-auth/
```

PowerShell has its own thing independent of `curl`:

```
Invoke-WebRequest http://localhost:8000/api-token-auth/ -Method Post -ContentType "application/json" -Body '{"username":"USER", "password":"PASS"}' -UseBasicParsing
```

If you get back a very large amount of html and other text, you have an error.
Scroll back up and google the error displayed just under your console command
for help troubleshooting.  Many of the errors you can get here are easy to do,
common, and relatively easy to google for information on how to fix.

You should get back one line with a token, for example: 

```json
{"token":"da51ccf5274050cd7332d184246d7d0775dc79e2"}
```

Your token will be different.  Try it out with your token:

```
curl -v -H 'Authorization: Token da51ccf5274050cd7332d184246d7d0775dc79e2' http://127.0.0.1:8000/api/notes/
```

Or, in PowerShell:

```
Invoke-WebRequest http://localhost:8000/api/notes/ -Headers @{"Authorization"="Token da51ccf5274050cd7332d184246d7d0775dc79e2"}
```

Note that the trailing `/` on the URL matters.  You will get a 301 redirect if
you don’t add it here.

When using Axios to send the request, set the header here:

```javascript
axios.post('http://127.0.0.1:8000/api/notes/', data, {
  headers: {
    'Authorization': 'Token da51ccf5274050cd7332d184246d7d0775dc79e2',
  }
}
```
