from django import forms
from .models import Marcas

class Marcas_form(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = '__all__'