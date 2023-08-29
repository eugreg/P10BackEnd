from rest_framework.viewsets import ModelViewSet

from P10.models import Compra
from P10.serializers import CompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
