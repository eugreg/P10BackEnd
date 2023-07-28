from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereço = models.CharField(max_length=150)
    email = models.EmailField(null=False, blank=True)
    avaliacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
