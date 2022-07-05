from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import User_profile

class Registro_usuario_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)    

    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class User_edit_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        # fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class Profile_form(forms.ModelForm):
    class Meta:
        model = User_profile
        exclude = ('username',)
        fields = '__all__'

class Update_profile_form(forms.ModelForm):
    class Meta:
        model = User_profile
        exclude = ('username',)
        fields = '__all__'