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
from django.urls import path, include
from rest_framework import routers
from cards.api import PersonalCardViewSet
from django.urls import path, include, re_path
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'cards', PersonalCardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
]

# {"token":"d808f5e2be7ff087ab5481cd80da53508514eb14"}
# curl -v -H 'Authorization: Token d808f5e2be7ff087ab5481cd80da53508514eb14' http://127.0.0.1:8000/api/cards/
# {"token":"d6bc15574afd72c50908ed3cfa5406182b32e2c8"}(Intro-Django-dLu91mvy)
# curl -v -H 'Authorization: Token d6bc15574afd72c50908ed3cfa5406182b32e2c8' http://127.0.0.1:8000/api/cards/