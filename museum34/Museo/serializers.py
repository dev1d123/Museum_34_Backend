from rest_framework import serializers
from .models import Usuario, Modelos, Configuracion, Comentarios, Favorito, Articulos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ModelosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelos
        fields = '__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class ArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulos
        fields = '__all__'