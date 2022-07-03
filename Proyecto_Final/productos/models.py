
from django.db import models
from marcas.models import Marcas 
from categorias.models import Tipo

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, related_name='producto') # relacionada con el modelo Marcas
    modelo = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='producto') # relacionada con el modelo Tipo
    precio = models.FloatField()
    stock = models.IntegerField()
    descuento = models.FloatField()
    novedad = models.BooleanField()    
    imagen = models.ImageField(upload_to = 'prod_images', default='')
    descripcion = models.CharField(max_length=200, blank=True, default='')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre

class Estados(models.Model):
    estado = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    def __str__(self):
        return str(self.estado)