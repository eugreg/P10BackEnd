from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False, default=None)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=100   )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Fornecedores"