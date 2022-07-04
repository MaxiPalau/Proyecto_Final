from django.contrib import admin
from django.urls import path, include
from site_extras.views import  Leyendas_inicio, Detalle_about

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Leyendas_inicio.as_view(), name = 'index'),
    path('', Detalle_about.as_view(), name = 'about'),  
] 