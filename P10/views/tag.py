from rest_framework.viewsets import ModelViewSet
from P10.serializers import TagSerializer
from P10.models import Tag

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    