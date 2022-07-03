from django.db import models
# from marcas.models import Marcas

# Create your models here.
class Distribuidores(models.Model):
    razon_social = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    cuit = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Distribuidor'
        verbose_name_plural = 'Distribuidores'

    def __str__(self):
        return self.razon_social

# class Distribuidores_marcas(models.Model):
#     marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, related_name='nombre_marca')
#     distribuidor = models.ForeignKey(Distribuidores, on_delete=models.CASCADE, related_name='nombre')
#     active = models.BooleanField(default=True)
    
#     class Meta:
#         verbose_name = 'Distribuidores x marca'
#         verbose_name_plural = 'Distribuidores x marcas'

#     def __str__(self):
#         return str(self.distribuidor)