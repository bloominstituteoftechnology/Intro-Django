from django.conf.urls import url
from notes import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
]
