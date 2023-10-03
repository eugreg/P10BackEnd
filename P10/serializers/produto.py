from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField
from P10.models import Produtos, Tag
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProdutosCreateSerializer(ModelSerializer):
    imagens_attachment_key = SlugRelatedField(
            source="imagem",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
            many=True
        )
    imagem = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Produtos
        fields = '__all__'
    
    
    def create(self, validated_data=None):
        breakpoint()
        imagens = validated_data.get('imagem', None)
        tags = validated_data.get('tag', None)
        del validated_data['imagem']
        del validated_data['tag']
        novoProduto = Produtos.objects.create(**validated_data)
        for imagem in imagens:
            novaImagem = Image.objects.get(attachment_key=imagem.attachment_key)
            novoProduto.imagem.add(novaImagem)            
        for tag in tags:
            novoProduto.tag.add(Tag.objects.get(id=tag.id))
        novoProduto.save()
        return novoProduto
        

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
    imagem = SerializerMethodField()

    def get_imagem(self, obj):
        imagem_instance = obj.imagem.first()  

        if imagem_instance:
            return imagem_instance.file.url  

        return None

    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 2

class ProdutosDetailSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False, read_only=True, many=True)
    class Meta:
        model = Produtos
        fields = "__all__"
        depth = 2
