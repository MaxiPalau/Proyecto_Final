from django.urls import path
from dist_marca.views import list_distribuidor_marca, update_distribuidor_marca, delete_distribuidor_marca, create_distribuidor_marca

urlpatterns = [
    path('dist-marca/', list_distribuidor_marca, name='list_distribuidor_marca'),
    path('create/', create_distribuidor_marca, name='create_distribuidor_marca'),
    path('update/<pk>', update_distribuidor_marca, name='update_distribuidor_marca'),
    path('delete/<pk>', delete_distribuidor_marca, name='delete_distribuidor_marca'),
]
