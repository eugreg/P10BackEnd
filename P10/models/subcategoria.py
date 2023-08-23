from django.db import models

from .categoria import Categoria

class SubCategoria(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, related_name="subcategorias")
    
    def __str__(self):
        return self.descricao