from django.contrib import admin
from .models import Usuario, Modelos, Configuracion, Comentarios, Favorito, Articulos

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Modelos)
admin.site.register(Configuracion)
admin.site.register(Comentarios)
admin.site.register(Favorito)
admin.site.register(Articulos)
