from django.db import models

# Create your models here.
class Tipo(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.categoria