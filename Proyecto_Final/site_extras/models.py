from tabnanny import verbose
from django.db import models

class Inicio(models.Model):
    titulo = models.CharField(max_length=200, blank=True, default='Bienvenido a')
    subtitulo = models.CharField(max_length=200, blank=True, default='Ferreteria 2010')

    class Meta:
        verbose_name = 'Inicio Titulo'
        verbose_name_plural = 'Inicio Titulos'
     
    def __str__(self):
        return self.titulo


class About(models.Model):
    nombre = models.CharField(max_length=200, blank=True, default='')
    puesto = models.CharField(max_length=200, blank=True, default='')
    descripcion = models.CharField(max_length=400, blank=True, default='')

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de nosotros'
     
    def __str__(self):
        return self.nombre
