from django import forms

from .models import Localizacao


class LocalizacaoForm(forms.ModelForm):
    class Meta:
        model = Localizacao
        fields = ['nome', 'latitude', 'longitude', 'ativa']
