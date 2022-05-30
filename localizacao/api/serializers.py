from localizacao import models
from rest_framework import serializers


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Localizacao
        fields = '__all__'
