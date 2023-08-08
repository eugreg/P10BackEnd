from django.db import models
from uploader.models import Image

from P10.models import  Fornecedor, Categoria, Descontos


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    quantidade = models.IntegerField(null=True, default=0)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.PROTECT,related_name="Produtos")
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT,related_name="Produtos")
    desconto = models.ForeignKey(Descontos,on_delete=models.PROTECT,related_name="Produtos")
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
