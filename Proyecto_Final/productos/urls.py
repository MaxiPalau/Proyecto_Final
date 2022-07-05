from django.urls import path
from productos.views import search_product, create_product, list_productos, detail_product, update_product, delete_product, compra_product

urlpatterns = [
    path('', list_productos, name = 'productos'),
    path('search-product/', search_product, name = 'search_product'),
    path('create-product/', create_product, name = 'create_product'),
    path('detail-producto/<pk>', detail_product, name='detail_producto'),
    path('delete-producto/<pk>/', delete_product, name='delete_producto'),
    path('update-producto/<pk>', update_product, name='update_producto'),
    path('compra-producto/<pk>', compra_product, name='compra_producto'),
]
