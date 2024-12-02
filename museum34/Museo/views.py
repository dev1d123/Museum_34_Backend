from rest_framework import viewsets
from .models import Usuario, Modelos, Configuracion, Comentarios, Favorito, Articulos
from .serializers import UsuarioSerializer, ModelosSerializer, ConfiguracionSerializer, ComentariosSerializer, FavoritoSerializer, ArticulosSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ModelosViewSet(viewsets.ModelViewSet):
    queryset = Modelos.objects.all()
    serializer_class = ModelosSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer
