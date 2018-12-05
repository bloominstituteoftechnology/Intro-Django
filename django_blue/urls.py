"""django_blue URL Configuration

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
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path, re_path

from rest_framework import routers
from rest_framework.authtoken import views
from users_app.api import PersonalNoteViewSet
from things.api import PersonalThingViewSet
from users_app import views as views2

router = routers.DefaultRouter()
router.register(r'users_app', PersonalNoteViewSet)
router.register(r'things', PersonalThingViewSet)

urlpatterns = [
    url(r'^$', views2.index, name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^users/', include('users_app.urls')),
    url(r'^things/', include('things.urls')),
    re_path(r'^api-token-auth/', views.obtain_auth_token)
]


