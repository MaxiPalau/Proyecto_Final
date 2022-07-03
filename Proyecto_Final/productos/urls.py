from django.urls import path

# from productos.views import  Create_product, Detail_product, List_productos, Delete_product, Update_product
# from productos.views import Create_distribuidor, Create_distribuidor_marca, Create_tipo, Create_marca, List_marcas, Edit_marca 
# from productos.views import Delete_marca, List_distribuidor, Edit_distribuidor, Delete_distribuidor, List_tipo, Edit_tipo, Delete_tipo
from productos.views import search_product, create_product, list_productos, detail_product, update_product, delete_product
# from productos.views import create_marca, update_marca, delete_marca, list_marcas
# from productos.views import create_marca, update_marca, delete_marca, list_distribuidor, create_distribuidor, update_distribuidor
# from productos.views import delete_distribuidor, create_distribuidor_marca
# from productos.views import delete_distribuidor, create_distribuidor_marca, list_tipo, create_tipo, update_tipo, delete_tipo
# from productos.views import list_distribuidor_marca, update_distribuidor_marca, delete_distribuidor_marca


urlpatterns = [
    # path('', List_productos.as_view(), name = 'productos'),
    path('', list_productos, name = 'productos'),
    path('search-product/', search_product, name = 'search_product'),
    # path('create-product/', Create_product.as_view(), name = 'create_product'),
    path('create-product/', create_product, name = 'create_product'),
    # path('detail-producto/<int:pk>/', Detail_product.as_view(), name='detail_producto'),
    path('detail-producto/<pk>', detail_product, name='detail_producto'),
    # path('delete-producto/<int:pk>/', Delete_product.as_view(), name='delete_producto'),
    path('delete-producto/<pk>/', delete_product, name='delete_producto'),
    # path('update-producto/<int:pk>/', Update_product.as_view(), name='update_producto'),
    path('update-producto/<pk>', update_product, name='update_producto'),
    # path('marcas/', List_marcas.as_view(), name = 'marcas'),
    # path('marcas/', list_marcas, name = 'marcas'),
    # path('detail-marca/<int:pk>/', Detail_marca.as_view(), name='detail_marca'),
    # path('create-marca/', Create_marca.as_view(), name='create_marca'),
    # path('create-marca/', create_marca, name='create_marca'),
    # path('edit-marca/<int:pk>/', Edit_marca.as_view(), name='edit_marca'),
    # path('update-marca/<pk>', update_marca, name='update_marca'),
    # path('delete-marca/<int:pk>/', Delete_marca.as_view(), name='delete_marca'),
    # path('delete-marca/<pk>', delete_marca, name='delete_marca'),
    # path('distribuidores/', List_distribuidor.as_view(), name='distribuidores'),
    # path('distribuidores/', list_distribuidor, name='distribuidores'),
    # path('create-distribuidor/', Create_distribuidor.as_view(), name='create_distribuidor'),
    # path('create-distribuidor/', create_distribuidor, name='create_distribuidor'),
    # path('edit-distribuidor/<int:pk>/', Edit_distribuidor.as_view(), name='edit_distribuidor'),
    # path('update-distribuidor/<pk>', update_distribuidor, name='update_distribuidor'),
    # path('delete-distribuidor/<int:pk>/', Delete_distribuidor.as_view(), name='delete_distribuidor'),
    # path('delete-distribuidor/<pk>', delete_distribuidor, name='delete_distribuidor'),
    # # path('tipos/', List_tipo.as_view(), name='tipos'),
    # path('tipos/', list_tipo, name='tipos'),
    # # path('create-tipo/', Create_tipo.as_view(), name='create_tipo'),
    # path('create-tipo/', create_tipo, name='create_tipo'),
    # # path('edit-tipo/<int:pk>/', Edit_tipo.as_view(), name='edit_tipo'),
    # path('update-tipo/<pk>/', update_tipo, name='update_tipo'),
    # # path('delete-tipo/<int:pk>/', Delete_tipo.as_view(), name='delete_tipo'),
    # path('delete-tipo/<pk>/', delete_tipo, name='delete_tipo'),
    # path('dist-marca/', list_distribuidor_marca, name='list_distribuidor_marca'),
    # path('create-distribuidorm/', Create_distribuidor_marca.as_view(), name='create_distribuidor_marca'),
    # path('create-distribuidorm/', create_distribuidor_marca, name='create_distribuidor_marca'),
    # path('update-distribuidorm/<pk>', update_distribuidor_marca, name='update_distribuidor_marca'),
    # path('delete-distribuidorm/<pk>', delete_distribuidor_marca, name='delete_distribuidor_marca'),
]
