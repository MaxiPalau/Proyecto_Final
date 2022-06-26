from django.shortcuts import render
from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_marcas
from productos.forms import Productos_form, Marcas_form, Distribuidores_form, Distribuidores_marcas_form, Tipo_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse

# Create your views here.
class List_productos(ListView):
    model = Productos
    template_name = 'products/productos.html'
    


def search_product_view(request):
    productos = Productos.objects.filter(nombre__icontains = request.GET['search'])
    marcas = Marcas.objects.filter(nombre__icontains = request.GET['search']).values('id')
    tipos = Tipo.objects.filter(categoria__icontains = request.GET['search']).values('id')
    if productos.exists():
        context = {'productos':productos}
    elif marcas.exists():
        productos = Productos.objects.filter(marca__in = marcas)
        context = {'productos':productos}
    elif tipos.exists():
        productos = Productos.objects.filter(tipo__in = tipos)
        context = {'productos':productos}
    else:
        context = {'errors':'No se encontraron productos.'}
    return render(request, 'products/search_product.html', context = context)


class Create_product(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = 'products/create_product.html'
    fields = '__all__' 
    
    def get_success_url(self):
        return reverse('detail_producto', kwargs={'pk':self.object.pk})

class Detail_product(DetailView):
    model = Productos
    template_name = 'products/detalle_producto.html'

class Delete_product(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'delete_producto.html'

    def get_success_url(self):
        return reverse('productos')

class Update_product(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = 'products/update_producto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_producto', kwargs={'pk':self.object.pk})

class Create_marca(LoginRequiredMixin, CreateView):
    model = Marcas
    template_name= 'distribuidores/create_marca.html'
    fields = '__all__'

    def get_success_url(self):
        return('index')

class Create_distribuidor(LoginRequiredMixin, CreateView):
    model = Distribuidores
    template_name= 'distribuidores/create_distribuidor.html'
    fields = '__all__'

    def get_success_url(self):
        return('index')

class Create_distribuidor_marca(LoginRequiredMixin, CreateView):
    model = Distribuidores_marcas
    template_name= 'distribuidores/create_distribuidor_marca.html'
    fields = '__all__'

    def get_success_url(self):
        return('index')

class Create_tipo(LoginRequiredMixin, CreateView):
    model = Tipo
    template_name= 'products/create_tipo.html'
    fields = '__all__'

    def get_success_url(self):
        return('index')


# def productos(request):
#     producto = Productos.objects.all()
#     #print(producto) 
#     context = {'producto':producto}
#     return render(request, 'productos.html', context=context)
#
# def create_product_view(request):
#     if request.method == 'GET':
#         form = Productos_form()
#         context = {'form':form}
#         return render(request, 'create_product.html', context=context)
#     else:
#         form = Productos_form(request.POST, request.FILES)
#         print(form.is_valid())
#         if form.is_valid():
#             new_product = Productos.objects.create(
#                 nombre = form.cleaned_data['nombre'],
#                 precio = form.cleaned_data['precio'],
#                 sku = form.cleaned_data['sku'],
#                 novedad = form.cleaned_data['novedad'],
#                 marca = form.cleaned_data['marca'],
#                 modelo = form.cleaned_data['modelo'],
#                 tipo = form.cleaned_data['tipo'],
#                 stock = form.cleaned_data['stock'],
#                 descuento = form.cleaned_data['descuento'],
#                 imagen = request.FILES['imagen'],
#                 descripcion = form.cleaned_data['descripcion']
#             )
#             new_product.save()
#             context ={'new_product':new_product}
#         return render(request, 'create_product.html', context=context)
#
# def create_marca_view(request):
#     #print(request.user.groups.all())
#     if request.method == 'GET':
#         form = Marcas_form()
#         context ={'form':form}
#         return render(request, 'create_marca.html', context=context)
#     else:
#         form = Marcas_form(request.POST)
#         if form.is_valid():
#             new_marca = Marcas.objects.create(
#                 nombre = form.cleaned_data['nombre'],
#                 descripcion = form.cleaned_data['descripcion'],
#             )
#             context = {'new_marca':new_marca}
#         return render(request, 'create_marca.html', context=context)
#
# def create_distribuidor_view(request):
#     if request.method == 'GET':
#         form = Distribuidores_form()
#         context = {'form':form}
#         return render(request, 'create_distribuidor.html', context=context)
#     else:
#         form = Distribuidores_form(request.POST)
#         if form.is_valid():
#             new_distribuidor = Distribuidores.objects.create(
#                 razon_social = form.cleaned_data['razon_social'],
#                 direccion = form.cleaned_data['direccion'],
#                 localidad = form.cleaned_data['localidad'],
#                 pais = form.cleaned_data['pais'],
#                 telefono = form.cleaned_data['telefono'],
#                 mail = form.cleaned_data['mail'],
#                 web = form.cleaned_data['web'],
#                 cuit = form.cleaned_data['cuit'],
#                 descripcion = form.cleaned_data['descripcion']
#             )
#             context ={'new_distribuidor':new_distribuidor}
#         return render(request, 'create_distribuidor.html', context=context)
#
#
# def create_distribuidor_marca_view(request):
#     if request.method == 'GET':
#         form = Distribuidores_marcas_form()
#         context = {'form':form}
#         return render(request, 'create_distribuidor_marca.html', context=context)
#     else:
#         form = Distribuidores_marcas_form(request.POST)
#         if form.is_valid():
#             new_distribuidor_m = Distribuidores_Marcas.objects.create(
#                 marca = form.cleaned_data['marca'],
#                 distribuidor = form.cleaned_data['distribuidor'],
#             )
#             context ={'new_distribuidor_m':new_distribuidor_m}
#         return render(request, 'create_distribuidor_marca.html', context=context)
#
#
#
# def create_tipo_view(request):
#     if request.method == 'GET':
#         form = Tipo_form()
#         context = {'form':form}
#         return render(request, 'products/create_tipo.html', context=context)
#     else:
#         form = Tipo_form(request.POST)
#         if form.is_valid():
#             new_tipo = Tipo.objects.create(
#                 categoria = form.cleaned_data['categoria'],
#                 descripcion = form.cleaned_data['descripcion'],
#             )
#             context ={'new_tipo':new_tipo}
#         return render(request, 'products/create_tipo.html', context=context)