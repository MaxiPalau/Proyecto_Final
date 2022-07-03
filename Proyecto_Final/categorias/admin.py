from django.contrib import admin
from .models import Tipo

# Register your models here.
class Display_categorias(admin.ModelAdmin):
    list_display = ('categoria', 'descripcion', 'active')

admin.site.register(Tipo, Display_categorias)