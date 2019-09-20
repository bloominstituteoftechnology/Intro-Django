from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import current_user, UserList

from notes.api import NoteViewSet

app_name = 'notes'
urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),


   

]