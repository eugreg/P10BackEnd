from django.contrib import admin

from P10.models import Produtos, Fornecedor, Compra, Categoria, Descontos, ItensCompra, Sazonal, SubCategoria, Marca, Tag

admin.site.register(Produtos)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Descontos)
admin.site.register(ItensCompra)
admin.site.register(Sazonal)
admin.site.register(SubCategoria)
admin.site.register(Marca)
admin.site.register(Tag)


class IntensCompraInline(admin.TabularInline):
    model = ItensCompra
    

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [IntensCompraInline]
