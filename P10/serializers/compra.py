from rest_framework.serializers import ModelSerializer, CharField

from P10.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade"]
        depth = 2
        

class CompraSerializer(ModelSerializer):
    class Meta:
        status = CharField(source="get_status_display", read_only=True)
        usuario = CharField(source="usuario.username", read_only=True)
        itens = ItensCompraSerializer(many=True, read_only=True)
        model = Compra
        fields = "__all__"
