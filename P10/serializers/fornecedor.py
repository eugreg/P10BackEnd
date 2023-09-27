from rest_framework.serializers import ModelSerializer

from P10.models import Fornecedor

class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = "__all__"

class FornecedorListSerializer(ModelSerializer):
    
    class Meta:
        model = Fornecedor
        fields = "__all__"  

class FornecedorDetailSerializer(ModelSerializer):    
    class Meta:
        model = Fornecedor
        fields = "__all__"
        depth = 1