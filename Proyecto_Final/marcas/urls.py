from django.urls import path
from marcas.views import list_marcas, create_marca, update_marca, delete_marca

urlpatterns = [
    # path('marcas/', List_marcas.as_view(), name = 'marcas'),
    path('marcas/', list_marcas, name = 'marcas'),
    # path('detail-marca/<int:pk>/', Detail_marca.as_view(), name='detail_marca'),
    # path('create-marca/', Create_marca.as_view(), name='create_marca'),
    path('create-marca/', create_marca, name='create_marca'),
    # path('edit-marca/<int:pk>/', Edit_marca.as_view(), name='edit_marca'),
    path('update-marca/<pk>', update_marca, name='update_marca'),
    # path('delete-marca/<int:pk>/', Delete_marca.as_view(), name='delete_marca'),
    path('delete-marca/<pk>', delete_marca, name='delete_marca'),
]
