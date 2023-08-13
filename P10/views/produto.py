from rest_framework.viewsets import ModelViewSet

from P10.models import Produtos
from P10.serializers import( ProdutosListSerializer, ProdutosDetailSerializer, ProdutosSerializer)

class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = {
        "list": ProdutosListSerializer,
        "retrieve": ProdutosDetailSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializer_class.get(self.action, ProdutosSerializer)
