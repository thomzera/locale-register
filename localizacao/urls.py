from django.urls import path

from .views import ListaLocalizacaoView

urlpatterns = [
    path('', ListaLocalizacaoView.as_view(), name='localizacao.index')
]
