from rest_framework.serializers import ModelSerializer
from P10.models import Sazonal

class SazonalSerializer(ModelSerializer):
    class Meta:
        model = Sazonal
        fields = "__all__"