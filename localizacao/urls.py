from django.urls import path

from .views import (ListaLocalizacaoView, LocalizacaoCreateView,
                    LocalizacaoDeleteView, LocalizacaoUpdateView)

urlpatterns = [
    path('', ListaLocalizacaoView.as_view(), name='localizacao.index'),
    path('novo/', LocalizacaoCreateView.as_view(), name='localizacao.novo'),
    path('editar/<int:pk>', LocalizacaoUpdateView.as_view(), name='localizacao.editar'),
    path('remover/<int:pk>', LocalizacaoDeleteView.as_view(), name='localizacao.remover'),
]
