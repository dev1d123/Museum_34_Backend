from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    clave = models.CharField(max_length=128)
    configuracion = models.OneToOneField(
        'Configuracion', on_delete=models.CASCADE, null=True, blank=True, related_name='usuario'
    )

    def __str__(self):
        return self.nombre
    
class Modelos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Configuracion(models.Model):
    brillo = models.SmallIntegerField(default=50)  # Nivel de brillo, por defecto 50
    volumen = models.SmallIntegerField(default=50)  # Nivel de volumen, por defecto 50
    velocidad_movimiento = models.SmallIntegerField(default=5)  # Velocidad de movimiento, por defecto 5
    sensibilidad = models.SmallIntegerField(default=5)  # Nivel de sensibilidad, por defecto 5
    rutas = models.BooleanField(default=False)  # Indica si las rutas están habilitadas o no
    
    def __str__(self):
        return (
            f"Configuracion {self.id} - Brillo: {self.brillo}, "
            f"Volumen: {self.volumen}, VelocidadMovimiento: {self.velocidad_movimiento}, "
            f"Sensibilidad: {self.sensibilidad}, Rutas: {'Habilitadas' if self.rutas else 'Deshabilitadas'}"
        )

class Comentarios(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='comentarios')
    modelo = models.ForeignKey('Modelos', on_delete=models.CASCADE, related_name='comentarios')    
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comentario de {self.usuario.nombre} sobre {self.modelo.nombre}"

class Favorito(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='favoritos')
    modelo = models.ForeignKey('Modelos', on_delete=models.CASCADE, related_name='en_favoritos')
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorito de {self.usuario.nombre} - {self.modelo.nombre}"
    
class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    resumen = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    revista = models.CharField(max_length=100, blank=True, null=True) 
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo