from django.contrib import admin
from accounts.models import User_profile


# Register your models here.
class Display_profile(admin.ModelAdmin):
    list_display = ('username', 'descripcion', 'link', 'image')

admin.site.register(User_profile, Display_profile)