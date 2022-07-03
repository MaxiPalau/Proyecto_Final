from django import forms
from dist_marca.models import Distribuidores_marcas

class Distribuidores_marcas_form(forms.ModelForm):
    class Meta:
        model = Distribuidores_marcas
        fields = '__all__'