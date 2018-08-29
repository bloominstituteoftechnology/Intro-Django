from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.view_all_music, name='music'),
]