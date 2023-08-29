from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from P10.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade", "total" ] 
      
    
    def get_total(self, obj):
        return obj.produto.preco * obj.quantidade
        

class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
    usuario = CharField(source="usuario.username", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra

class CriarEditarCompraSerializer(ModelSerializer):
    intens = ItensCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ("intens","usuario")
