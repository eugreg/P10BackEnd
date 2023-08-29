from rest_framework.viewsets import ModelViewSet

from P10.models import Compra
from P10.serializers import CompraSerializer,  CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    
    def get_queryset_class(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all() 
        if usuario.groups.filter(name="admin"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraSerializer
        return CriarEditarCompraSerializer
    