"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# import router functionality and PersonalNoteViewSet
from rest_framwork import routers
from notes.api import PersonalNoteViewSet

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # sets the path to '/api/notes'. We can use router.register to add as many paths
    # as we want without needing to add them to urlpatterns
    path('api/', include(router.urls))
]

# Make and register a default router
router = routers.DefaultRouter()
# 'r' means this is a regualr expression. Interpret the string as literally as possible
router.register(r'notes', PersonalNoteViewSet)

