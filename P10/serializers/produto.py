from rest_framework.serializers import ModelSerializer
from P10.models import Produtos


class ProdutosSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"


class ProdutosListSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = ["id", "nome", "Preço"]


class ProdutosDetailSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1