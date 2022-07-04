from django.urls import path
from accounts.views import login_view, logout_view, register_view, profile_view, create_profile, update_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('create-profile/', create_profile, name='create_profile'),
    path('update-profile/<pk>/', update_profile, name='update_profile'),
]