from django.db import models
from uploader.models import Image


class Marca(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ManyToManyField(
        Image,
        related_name="+",
    )
    
    def __str__(self):
        return self.descricao