from django import forms
from productos.models import Productos

class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'