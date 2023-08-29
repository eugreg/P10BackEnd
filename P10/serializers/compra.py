from rest_framework.serializers import ModelSerializer, CharField

from P10.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        usuario = CharField(source="usuario.username", read_only=True)
        model = Compra
        fields = "__all__"