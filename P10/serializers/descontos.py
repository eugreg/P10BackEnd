from rest_framework.serializers import ModelSerializer
from P10.models import Descontos

class DescontoSerializer(ModelSerializer):
    class Meta:
        model = Descontos
        fields = "__all__"