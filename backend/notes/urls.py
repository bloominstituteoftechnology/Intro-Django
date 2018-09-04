from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

from notes.api import NoteViewSet

app_name = 'notes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/notes/', NoteViewSet),
    path('<str:pk>', views.ViewDetail.as_view(), name='detail'),
    re_path(r"^api-token-auth/", obtain_auth_token),
    re_path(r"^api-auth/", include("rest_framework.urls")),


   

]