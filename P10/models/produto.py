from django.db import models
from uploader.models import Image


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    Preço = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    quantidade = models.IntegerField(null=True, default=0)
    fornecedor = models.CharField(max_length=100)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome
