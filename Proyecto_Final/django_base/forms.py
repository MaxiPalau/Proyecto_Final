# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class Registro_usuario_form(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
#     first_name = forms.CharField(label='Nombre')
#     last_name = forms.CharField(label='Apellido')
    

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#         # fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {k:'' for k in fields}
