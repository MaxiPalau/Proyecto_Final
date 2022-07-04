from django.contrib import admin
from site_extras.models import Inicio, About

class Display_titulo(admin.ModelAdmin):
    list_display = ('titulo','subtitulo')

admin.site.register(Inicio, Display_titulo)

class Display_About(admin.ModelAdmin):
    list_display = ('nombre','puesto','descripcion')

admin.site.register(About, Display_About)
