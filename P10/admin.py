from django.contrib import admin

from P10.models import Produtos, Cliente, Fornecedor, Compra, Categoria, Descontos,ItensCompra

admin.site.register(Produtos)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Descontos)
admin.site.register(ItensCompra)


class IntensCompraInline(admin.TabularInline):
    model = ItensCompra
    

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [IntensCompraInline]
