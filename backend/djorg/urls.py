
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken import views
from notes.serializers import PersonalNoteViewSet
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
