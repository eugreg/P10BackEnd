from rest_framework.viewsets import ModelViewSet
from P10.models import Descontos
from P10.serializers import DescontoSerializer

class DescontoViewSet(ModelViewSet):
    queryset = Descontos.objects.all()
    serializer_class = DescontoSerializer

