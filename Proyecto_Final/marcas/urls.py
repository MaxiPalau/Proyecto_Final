from django.urls import path
from marcas.views import list_marcas, create_marca, update_marca, delete_marca

urlpatterns = [
    path('marcas/', list_marcas, name = 'marcas'),
    path('create-marca/', create_marca, name='create_marca'),
    path('update-marca/<pk>', update_marca, name='update_marca'),
    path('delete-marca/<pk>', delete_marca, name='delete_marca'),
]
