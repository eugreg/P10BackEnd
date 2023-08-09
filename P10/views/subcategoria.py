from rest_framework.viewsets import ModelViewSet
from P10.serializers import SubCategoriaSerializer
from P10.models import SubCategoria

class SubCategoriaViewSet(ModelViewSet):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer
    