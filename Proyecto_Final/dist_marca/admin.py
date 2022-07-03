from django.contrib import admin
from dist_marca.models import Distribuidores_marcas
# Register your models here.
class Display_dist_marcas(admin.ModelAdmin):
    list_display = ('marca', 'distribuidor')
    
admin.site.register(Distribuidores_marcas, Display_dist_marcas)