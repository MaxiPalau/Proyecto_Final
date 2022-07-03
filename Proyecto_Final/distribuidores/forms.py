from django import forms
from distribuidores.models import Distribuidores

class Distribuidores_form(forms.ModelForm):
    class Meta:
        model = Distribuidores
        fields = '__all__'
