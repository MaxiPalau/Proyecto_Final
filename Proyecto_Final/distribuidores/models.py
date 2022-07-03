from django.db import models

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