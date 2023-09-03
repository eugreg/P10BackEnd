
from rest_framework.viewsets import ModelViewSet
from P10.models import Marca
from P10.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

