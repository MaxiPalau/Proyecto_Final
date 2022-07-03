from django.urls import path
from dist_marca.views import list_distribuidor_marca, update_distribuidor_marca, delete_distribuidor_marca, create_distribuidor_marca

urlpatterns = [
    path('dist-marca/', list_distribuidor_marca, name='list_distribuidor_marca'),
    # path('create-distribuidorm/', Create_distribuidor_marca.as_view(), name='create_distribuidor_marca'),
    path('create-distribuidorm/', create_distribuidor_marca, name='create_distribuidor_marca'),
    path('update-distribuidorm/<pk>', update_distribuidor_marca, name='update_distribuidor_marca'),
    path('delete-distribuidorm/<pk>', delete_distribuidor_marca, name='delete_distribuidor_marca'),
]
