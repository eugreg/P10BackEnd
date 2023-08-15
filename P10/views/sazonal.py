from rest_framework.viewsets import ModelViewSet
from P10.serializers import SazonalSerializer
from P10.models import Sazonal

class SazonalViewSet(ModelViewSet):
    queryset = Sazonal.objects.all()
    serializer_class = SazonalSerializer
    