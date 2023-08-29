from rest_framework.viewsets import ModelViewSet

from P10.models import Compra
from P10.serializers import CompraSerializer,  CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_queryset_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer