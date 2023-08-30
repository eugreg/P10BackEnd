from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)
from rest_framework import serializers

from P10.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade", "total"]
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.preco_item


class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")


class CriarEditarItenSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ["produto", "quantidade"]

    def validate(self, data):
        if data["quantidade"] > data["produto"].quantidade:
            raise serializers.ValidationError(
                {
                    "quantidade": "Quantidade solicitada não disponível em estoque."
                }
            )
        return data


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItenSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("itens", "usuario")
    
    def create(self, validated_data): 
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["produto"].preco
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

