from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User_profile')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='')
    image = models.ImageField(upload_to = 'profile_images', default='')

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'
