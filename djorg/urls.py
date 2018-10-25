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
from rest_framework import routers
from notes.api import PersonalNoteViewSet

from django.urls import path, include, re_path
# Set up the route to authenticate users
from rest_framework.authtoken import views

# Make and register a default router
router = routers.DefaultRouter()
# 'r' means this is a regualr expression. Interpret the string as literally as possible
router.register(r'notes', PersonalNoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # sets the path to '/api/notes'. We can use router.register to add as many paths
    # as we want without needing to add them to urlpatterns
    path('api/', include(router.urls)),
    # add endpoint for user authentication
    re_path(r'^api-token-auth/', views.obtain_auth_token)
    # '^' means 'match the beginnin of the string' in a regular expression
    # 're_path' means it is a path that interprets the endpoint as a regex instead of a fixed string    
]