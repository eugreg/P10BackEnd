from rest_framework.serializers import ModelSerializer, SlugRelatedField
from P10.models import Produtos
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutosSerializer(ModelSerializer):
    class Meta:
        imagem_attachment_key = SlugRelatedField(
            source="imagem",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        imagem = ImageSerializer(required=False, read_only=True)
        model = Produtos
        fields = "__all__"


class ProdutosListSerializer(ModelSerializer):
    class Meta:
        imagem=ImageSerializer(required=False)
        model = Produtos
        fields = ["id", "nome", "categoria", "fornecedor", "quantidade", "preco", "desconto"]


class ProdutosDetailSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1
