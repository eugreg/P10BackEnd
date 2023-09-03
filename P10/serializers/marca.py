from rest_framework.serializers import ModelSerializer

from P10.models import Marca
 
 
class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"