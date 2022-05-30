from django.contrib import admin

from .models import Localizacao

# Register your models here.

@admin.action(description="Ativar todas as localizações")
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description="Desativar todas as localizações")
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)


class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'latitude',
        'longitude',
        'ativa',
    ]
    list_filter = [
        'ativa'
    ]
    search_fields = [
        'nome'
    ]
    actions = [
        ativar_todos,
        desativar_todos,
    ]


admin.site.register(Localizacao, LocalizacaoAdmin)
