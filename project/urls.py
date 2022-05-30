from django.contrib import admin
from django.urls import include, path
from localizacao.api import viewsets as localizacoesviewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'/localizacoes', localizacoesviewsets.LocalizacaoViewSet, basename="Localizacao")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('localizacoes/', include('localizacao.urls')),
    path('api', include(route.urls)),
]
