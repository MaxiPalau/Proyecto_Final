from django.urls import path
from distribuidores.views import list_distribuidor, create_distribuidor, update_distribuidor
from distribuidores.views import delete_distribuidor

urlpatterns = [
    path('distribuidores/', list_distribuidor, name='distribuidores'),
    path('create-distribuidor/', create_distribuidor, name='create_distribuidor'),
    path('update-distribuidor/<pk>', update_distribuidor, name='update_distribuidor'),
    path('delete-distribuidor/<pk>', delete_distribuidor, name='delete_distribuidor'),
]
