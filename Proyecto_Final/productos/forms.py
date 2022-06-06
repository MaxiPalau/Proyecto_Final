from django import forms
from productos.models import Productos

# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField()

class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'