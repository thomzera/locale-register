# from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LocalizacaoForm
from .models import Localizacao


# Create your views here.
class ListaLocalizacaoView(ListView):
    model = Localizacao
    queryset = Localizacao.objects.all().order_by('nome')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome__contains=filtro_nome)

        return queryset


class LocalizacaoCreateView(CreateView):
    model = Localizacao
    form_class = LocalizacaoForm
    success_url = '/localizacoes/'


class LocalizacaoUpdateView(UpdateView):
    model = Localizacao
    form_class = LocalizacaoForm
    success_url = '/localizacoes/'


class LocalizacaoDeleteView(DeleteView):
    model = Localizacao
    success_url = '/localizacoes/'
