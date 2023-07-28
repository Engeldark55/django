from django.db import models

#migrar tablas en sqlite3 python3 manage,py makemigrations 
#python3 manage,py migrate

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(default='null')
    publico = models.BooleanField()
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    creacion = models.DateField()