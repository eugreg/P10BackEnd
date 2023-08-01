from rest_framework.serializers import ModelSerializer, SlugRelatedField
from P10.models import Produtos
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutosSerializer(ModelSerializer):
    class Meta:
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        capa = ImageSerializer(required=False, read_only=True)
        model = Produtos
        fields = "__all__"


class ProdutosListSerializer(ModelSerializer):
    class Meta:
        capa=ImageSerializer(required=False)
        model = Produtos
        fields = ["id", "nome", "Preço"]


class ProdutosDetailSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 1
