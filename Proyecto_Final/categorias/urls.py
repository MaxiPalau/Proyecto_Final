
from django.urls import path
from categorias.views import list_tipo, create_tipo, update_tipo, delete_tipo
urlpatterns = [
    # # path('tipos/', List_tipo.as_view(), name='tipos'),
    path('tipos/', list_tipo, name='tipos'),
    # # path('create-tipo/', Create_tipo.as_view(), name='create_tipo'),
    path('create-tipo/', create_tipo, name='create_tipo'),
    # # path('edit-tipo/<int:pk>/', Edit_tipo.as_view(), name='edit_tipo'),
    path('update-tipo/<pk>/', update_tipo, name='update_tipo'),
    # # path('delete-tipo/<int:pk>/', Delete_tipo.as_view(), name='delete_tipo'),
    path('delete-tipo/<pk>/', delete_tipo, name='delete_tipo'),
]