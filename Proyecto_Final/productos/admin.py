from django.contrib import admin
from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_marcas, Estados

# Register your models here.
admin.site.register(Tipo)

class Display_marcas(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'active')

admin.site.register(Marcas, Display_marcas)

class Display_productos(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'sku', 'tipo', 'stock', 'precio', 'estado', 'active')

admin.site.register(Productos, Display_productos)

class Display_distribuidores(admin.ModelAdmin):
    list_display = ('razon_social', 'direccion', 'localidad', 'pais', 'telefono', 'mail', 'web', 'cuit', 'descripcion', 'active')

admin.site.register(Distribuidores, Display_distribuidores)

class Display_dist_marcas(admin.ModelAdmin):
    list_display = ('marca', 'distribuidor')
    
admin.site.register(Distribuidores_marcas, Display_dist_marcas)

class Display_estados(admin.ModelAdmin):
    list_display = ('estado', 'descripcion')

admin.site.register(Estados, Display_estados)