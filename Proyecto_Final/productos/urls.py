from django.urls import path
from productos.views import search_product_view, Create_product, Detail_product, List_productos, Delete_product, Update_product
from productos.views import Create_distribuidor, Create_distribuidor_marca, Create_tipo, Create_marca, List_marcas, Edit_marca 
from productos.views import Delete_marca, List_distribuidor, Edit_distribuidor, Delete_distribuidor

urlpatterns = [
    path('', List_productos.as_view(), name = 'productos'),
    path('search-product/', search_product_view, name = 'search_product'),
    path('create-product/', Create_product.as_view(), name = 'create_product'),
    path('detail-producto/<int:pk>/', Detail_product.as_view(), name='detail_producto'),
    path('delete-producto/<int:pk>/', Delete_product.as_view(), name='delete_producto'),
    path('update-producto/<int:pk>/', Update_product.as_view(), name='update_producto'),
    path('marcas/', List_marcas.as_view(), name = 'marcas'),
    # path('detail-marca/<int:pk>/', Detail_marca.as_view(), name='detail_marca'),
    path('create-marca/', Create_marca.as_view(), name='create_marca'),
    path('edit-marca/<int:pk>/', Edit_marca.as_view(), name='edit_marca'),
    path('delete-marca/<int:pk>/', Delete_marca.as_view(), name='delete_marca'),
    path('distribuidores/', List_distribuidor.as_view(), name='distribuidores'),
    path('create-distribuidor/', Create_distribuidor.as_view(), name='create_distribuidor'),
    path('edit-distribuidor/<int:pk>/', Edit_distribuidor.as_view(), name='edit_distribuidor'),
    path('delete-distribuidor/<int:pk>/', Delete_distribuidor.as_view(), name='delete_distribuidor'),
    path('create-tipo/', Create_tipo.as_view(), name='create_tipo_view'),
    path('create-distribuidorm/', Create_distribuidor_marca.as_view(), name='create_distribuidor_marca'),
    
]
