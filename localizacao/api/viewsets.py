from localizacao import models
from localizacao.api import serializers
from rest_framework import viewsets


class LocalizacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocalizacaoSerializer
    queryset = models.Localizacao.objects.all()
