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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from notes.api import PersonalNoteViewSet
from music.api import PersonalMusicViewSet

router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)
router.register(r'music', PersonalMusicViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
    re_path(r'^api/', include(router.urls)),
    path(r'token-auth/', obtain_jwt_token),
    


    
]
