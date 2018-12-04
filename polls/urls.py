from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # index route
    path('', views.index, name='index'),
    # detail route
    path('<int:question_id>/', views.detail, name='detail'),
    # results route
    path('<int:question_id>/results/', views.results, name='results'),
    # vote route
    path('<int:question_id>/vote/', views.vote, name='vote'),