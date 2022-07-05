from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User_profile')
    descripcion = models.CharField(max_length=200, default='-', blank=True)
    link = models.CharField(max_length=100, default='-', blank=True)
    image = models.ImageField(upload_to = 'profile_images', default='default.jpg')

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'

    def __str__(self):
        return str(User.objects.get(id = self.username_id))