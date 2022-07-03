from django.contrib import admin
from productos.models import Productos, Tipo, Estados

# Register your models here.
class Display_productos(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'sku', 'tipo', 'stock', 'precio', 'active')

admin.site.register(Productos, Display_productos)

# class Display_estados(admin.ModelAdmin):
#     list_display = ('estado', 'descripcion')

# admin.site.register(Estados, Display_estados)