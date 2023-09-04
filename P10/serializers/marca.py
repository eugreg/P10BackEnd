from rest_framework.serializers import ModelSerializer

from P10.models import Marca
 
 
class MarcaSerializer(ModelSerializer):
    def get_imagem(self, obj):
        imagem_instance = obj.imagem.first()  

        if imagem_instance:
            return imagem_instance.file.url  

        return None

    class Meta:
        model = Marca
        fields = "__all__"