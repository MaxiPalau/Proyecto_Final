from django.contrib import admin
from .models import Marcas

# Register your models here.
class Display_marcas(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'active')

admin.site.register(Marcas, Display_marcas)