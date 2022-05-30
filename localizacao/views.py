from django.shortcuts import render
from django.views.generic import ListView

from .models import Localizacao


# Create your views here.
class ListaLocalizacaoView(ListView):
    model = Localizacao
    queryset = Localizacao.objects.all().order_by('nome')
