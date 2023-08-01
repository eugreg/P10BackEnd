from rest_framework.viewsets import ModelViewSet
from P10.models import Categoria
from P10.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer