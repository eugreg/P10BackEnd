from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    Preço = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    quantidade = models.IntegerField(null=True, default=0)
    fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereço = models.CharField(max_length=150)
    email = models.EmailField(null=False, blank=True)
    avaliacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
