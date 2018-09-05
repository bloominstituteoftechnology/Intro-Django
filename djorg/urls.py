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

from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from notes.api import PersonalNoteViewSet
from lcai.api import (HomeViewSet,
                      ProjectViewSet,
                      EventoViewSet,
                      MiembrosViewSet,
                      DirectoraViewSet,
                      InvestigadoresViewSet,
                      DoctorandosViewSet,
                      PhdThesisViewSet,
                      ColaboradoresViewSet)

from rest_framework.authtoken import views

router = routers.DefaultRouter()
lcai = routers.DefaultRouter()

# build an endpoint at /api/notes
router.register('notes', PersonalNoteViewSet)
# router.register('lcai/home', HomeViewSet)
# router.register('lcai/directora', DirectoraViewSet)
# router.register('lcai/investigadores', InvestigadoresViewSet)

lcai.register('home', HomeViewSet)
lcai.register('proyectos', ProjectViewSet)
lcai.register('eventos', EventoViewSet)
lcai.register('directora', DirectoraViewSet)
lcai.register('investigadores', InvestigadoresViewSet)
lcai.register('doctorandos', DoctorandosViewSet)
lcai.register('phd-thesis', PhdThesisViewSet)
lcai.register('colaboradores', ColaboradoresViewSet)
lcai.register('miembros', MiembrosViewSet)

urlpatterns = [
    path('polls/', include('polls.urls')),

    # router.urls will take care of ALL the posible api endpoint we can add in
    # the future. It is only needed this line for all posible APIS
    path('api/', include(router.urls)),
    path('api/lcai/', include(lcai.urls)),

    # Token auth endpoint -> this enpoint 'return' a token.
    path('api-token-auth/', views.obtain_auth_token),

    path('admin/', admin.site.urls),
]
