from django.contrib import admin
# from .models import Distribuidores, Distribuidores_marcas
from distribuidores.models import Distribuidores

# Register your models here.
class Display_distribuidores(admin.ModelAdmin):
    list_display = ('razon_social', 'direccion', 'localidad', 'pais', 'telefono', 'mail', 'web', 'cuit', 'descripcion', 'active')

admin.site.register(Distribuidores, Display_distribuidores)

# class Display_dist_marcas(admin.ModelAdmin):
#     list_display = ('marca', 'distribuidor')
    
# admin.site.register(Distribuidores_marcas, Display_dist_marcas)