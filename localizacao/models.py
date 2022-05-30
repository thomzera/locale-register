from django.db import models


# Create your models here.
class Localizacao(models.Model):
    nome = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome
