from django.db import models
from marcas.models import Marcas
from distribuidores.models import Distribuidores

# Create your models here.
class Distribuidores_marcas(models.Model):
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, related_name='nombre_marca')
    distribuidor = models.ForeignKey(Distribuidores, on_delete=models.CASCADE, related_name='nombre')
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Distribuidores x marca'
        verbose_name_plural = 'Distribuidores x marcas'

    def __str__(self):
        return str(self.distribuidor)