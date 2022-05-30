from django.urls import path

from .views import ListaLocalizacaoView, LocalizacaoCreateView

urlpatterns = [
    path('', ListaLocalizacaoView.as_view(), name='localizacao.index'),
    path('novo/', LocalizacaoCreateView.as_view(), name='localizacao.novo')
]
