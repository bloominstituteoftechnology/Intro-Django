from django.conf.urls import url
from things import views


urlpatterns = [
    url(r'^$', views.users, name='users')
]
