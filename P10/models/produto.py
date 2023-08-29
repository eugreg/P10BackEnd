from django.db import models
from uploader.models import Image

from .fornecedor import  Fornecedor
from .categoria import Categoria
from .desconto import Descontos
from .sazonal import Sazonal


class Produtos(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=150, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    quantidade = models.IntegerField(null=True, default=0)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.PROTECT, null=False, related_name="Produtos")
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT, null=False, related_name="Produtos")
    sazonal = models.ForeignKey(Sazonal, on_delete=models.PROTECT, null=True, related_name="Produtos")
    desconto = models.ForeignKey(Descontos,on_delete=models.PROTECT, null=True, related_name="Produtos")
    imagem = models.ManyToManyField(
        Image,
        related_name="+",
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Produtos"
