from django.urls import path
from productos.views import productos, search_product_view, create_product_view, create_marca_view, create_distribuidor_view
from productos.views import create_distribuidor_marca_view, create_tipo_view

urlpatterns = [
    path('', productos, name = 'productos'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('create-marca/', create_marca_view, name='create-marca-view'),
    path('create-distribuidor/', create_distribuidor_view, name='create-distribuidor-view'),
    path('create-tipo/', create_tipo_view, name='create_tipo_view'),
    path('create-distribuidorm/', create_distribuidor_marca_view, name='ccreate_distribuidor_marca_view'),
    
]
