from django.urls import path
from distribuidores.views import list_distribuidor, create_distribuidor, update_distribuidor
from distribuidores.views import delete_distribuidor
# from distribuidores.views import list_distribuidor_marca, update_distribuidor_marca, delete_distribuidor_marca, create_distribuidor_marca

urlpatterns = [
    # path('distribuidores/', List_distribuidor.as_view(), name='distribuidores'),
    path('distribuidores/', list_distribuidor, name='distribuidores'),
    # path('create-distribuidor/', Create_distribuidor.as_view(), name='create_distribuidor'),
    path('create-distribuidor/', create_distribuidor, name='create_distribuidor'),
    # path('edit-distribuidor/<int:pk>/', Edit_distribuidor.as_view(), name='edit_distribuidor'),
    path('update-distribuidor/<pk>', update_distribuidor, name='update_distribuidor'),
    # path('delete-distribuidor/<int:pk>/', Delete_distribuidor.as_view(), name='delete_distribuidor'),
    path('delete-distribuidor/<pk>', delete_distribuidor, name='delete_distribuidor'),
    # path('dist-marca/', list_distribuidor_marca, name='list_distribuidor_marca'),
    # path('create-distribuidorm/', Create_distribuidor_marca.as_view(), name='create_distribuidor_marca'),
    # path('create-distribuidorm/', create_distribuidor_marca, name='create_distribuidor_marca'),
    # path('update-distribuidorm/<pk>', update_distribuidor_marca, name='update_distribuidor_marca'),
    # path('delete-distribuidorm/<pk>', delete_distribuidor_marca, name='delete_distribuidor_marca'),
]
