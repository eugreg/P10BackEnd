from rest_framework.serializers import ModelSerializer, CharField

from P10.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        status = CharField(source="get_status_display", read_only=True)
        usuario = CharField(source="usuario.username", read_only=True)
        model = Compra
        fields = "__all__"