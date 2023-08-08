from django.db import models


class Descontos(models.Model):
    descricao = models.CharField(max_length=100)
    porcentagem = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.porcentagem