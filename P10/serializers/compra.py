from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from P10.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade", "total" ] 
        depth = 1
    
    def get_total(self, obj):
        return obj.produto.preco * obj.quantidade
        

class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
    usuario = CharField(source="usuario.username", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
