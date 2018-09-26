from django.conf.urls import url
from notes import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r"^$", views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
