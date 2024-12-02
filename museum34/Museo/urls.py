from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, ModelosViewSet, ConfiguracionViewSet, ComentariosViewSet, FavoritoViewSet, ArticulosViewSet
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'modelos', ModelosViewSet)
router.register(r'configuraciones', ConfiguracionViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'favoritos', FavoritoViewSet)
router.register(r'articulos', ArticulosViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Las rutas de la API estarán en la raíz de esta aplicación
]