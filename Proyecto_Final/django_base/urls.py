"""Proyecto_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, about
from site_extras.views import Leyendas_inicio, Detalle_about, Detalle_site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Leyendas_inicio, name = 'index'), 
    path('map/', Detalle_site, name = 'map'),
    path('about/', Detalle_about, name = 'about'),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('distribuidores/', include('distribuidores.urls')),
    path('dist-marca/', include('dist_marca.urls')),
    path('marcas/', include('marcas.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
