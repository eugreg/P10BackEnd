from rest_framework.serializers import ModelSerializer
from P10.models import Tag

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"