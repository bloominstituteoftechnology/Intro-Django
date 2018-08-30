from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views import index

from music.api import MusicViewSet

urlpatterns = [
    path('', index),
    path('api/login/', obtain_jwt_token),
    path('api/music/', MusicViewSet)
]