from django.contrib import admin

from .models import Localizacao

# Register your models here.

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'latitude',
        'longitude',
        'ativa',
    ]

admin.site.register(Localizacao, LocalizacaoAdmin)
