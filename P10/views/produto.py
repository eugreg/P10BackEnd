from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from P10.models import Produtos
from P10.serializers import( ProdutosListSerializer, ProdutosDetailSerializer, ProdutosSerializer)

class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [ "categoria"]
    search_fields = ["nome", "categoria", "fornecedor"]
    ordering_fields = ["nome", "categoria"]
    ordering = ["nome"]

    serializer_class = {
        "list": ProdutosListSerializer,
        "retrieve": ProdutosDetailSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializer_class.get(self.action, ProdutosSerializer)
