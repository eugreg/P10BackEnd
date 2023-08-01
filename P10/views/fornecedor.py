from rest_framework.viewsets import ModelViewSet

from P10.models import Fornecedor
from P10.serializers import( FornecedorListSerializer, FornecedorDetailSerializer, FornecedorSerializer)

class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = {
        "list": FornecedorListSerializer,
        "retrieve": FornecedorDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, FornecedorSerializer)