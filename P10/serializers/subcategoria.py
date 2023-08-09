from rest_framework.serializers import ModelSerializer
from P10.models import SubCategoria

class SubCategoriaSerializer(ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = "__all__"