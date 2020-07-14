Django is, like Python, a pragmatic “one right way to do it” system, specifically a web application framework built on the principles of convention over configuration and fast iterative design. The Django ecosystem bills itself as “the web framework for perfectionists with deadlines” - these many included features are what makes it quick to build an MVP with. 

Objectives

* set up the CORS
* use token authorization to assign correct permissions to various users

## Setting up CORS

In order to get your site to run well with a front-end, you might need to set up CORS:

https://github.com/ottoyiu/django-cors-headers

1. Nagivate to `settings.py` 

2. Add `'corsheaders'` to INSTALLED_APPS

3. Add `'corsheaders.middleware.CorsMiddleware'` and `'django.middleware.common.CommonMiddleware'` to the top of MIDDLEWARE 

4. Specify `CORS_ORIGIN_ALLOW_ALL = True`

## Using token authorization to assign correct permissions to various users

**Set up REST token authorization**

1. Open settings.py, go to INSTALLED_APPS, add `rest_framework.authtoken`

2. Import authentication for REST: `from rest_framework.authentication import TokenAuthentication`

3.  Add Default Auth Classes to the REST_FRAMEWORK:   'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )

**Add a new authorization endpoint, get back a token**

1. Set up the route to authenticate users in `urls.py`, import view

```
from rest_framework.authtoken import views
```

2. Add this line to urlpatterns

```
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token)
]
```
4. Check migrations : `./manage.py showmigrations`

```
authtoken
 [ ] 0001_initial
 [ ] 0002_auto_20160226_1747
```

5. `./manage.py migrate` and `./manage.py runserver`

* Test the endpoint using CURL