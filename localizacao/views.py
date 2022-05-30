from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import LocalizacaoForm
from .models import Localizacao


# Create your views here.
class ListaLocalizacaoView(ListView):
    model = Localizacao
    queryset = Localizacao.objects.all().order_by('nome')
 

class LocalizacaoCreateView(CreateView):
    model = Localizacao
    form_class = LocalizacaoForm
    success_url = '/localizacoes/'
