"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path

# -- IMPORT VIEWS AND TEMPLATES -- #
from notes.views import notes

# -- IMPORT FOR REST API -- #
from rest_framework import routers
from notes.api import PersonalNoteViewSet

# --- VIEWS FOR AUTH TOKENS -- #
from rest_framework.authtoken.views import obtain_auth_token

# --- IMPORTS FOR GRAPH-QL --- #
from graphene_django.views import GraphQLView

# REST API ROUTER #
router = routers.DefaultRouter()
router.register("notes", PersonalNoteViewSet)
# path('', notes),
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api-token-auth/", obtain_auth_token),
    path("api/", include(router.urls)),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
