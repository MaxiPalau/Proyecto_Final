from django import forms
from .models import Tipo

class Tipo_form(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'