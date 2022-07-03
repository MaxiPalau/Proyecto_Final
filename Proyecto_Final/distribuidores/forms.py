from django import forms
# from distribuidores.models import Distribuidores, Distribuidores_marcas
from distribuidores.models import Distribuidores


class Distribuidores_form(forms.ModelForm):
    class Meta:
        model = Distribuidores
        fields = '__all__'

# class Distribuidores_marcas_form(forms.ModelForm):
#     class Meta:
#         model = Distribuidores_marcas
#         fields = '__all__'
