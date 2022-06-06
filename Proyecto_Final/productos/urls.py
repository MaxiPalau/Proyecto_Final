from django.urls import path
from productos.views import productos, search_product_view, create_product_view

urlpatterns = [
    path('', productos, name = 'productos'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-product/', create_product_view, name = 'create-product'),
]
