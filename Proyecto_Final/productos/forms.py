from django import forms
# from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_marcas
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

# class Marcas_form(forms.ModelForm):
#     class Meta:
#         model = Marcas
#         fields = '__all__'

# class Distribuidores_form(forms.ModelForm):
#     class Meta:
#         model = Distribuidores
#         fields = '__all__'

# class Distribuidores_marcas_form(forms.ModelForm):
#     class Meta:
#         model = Distribuidores_marcas
#         fields = '__all__'

# class Tipo_form(forms.ModelForm):
#     class Meta:
#         model = Tipo
#         fields = '__all__'