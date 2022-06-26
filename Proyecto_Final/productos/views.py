from http.client import HTTPResponse
from django.shortcuts import render,redirect
from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_marcas, Estados
from productos.forms import Productos_form, Marcas_form, Distribuidores_form, Distribuidores_marcas_form, Tipo_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group

# Create your views here.

def usuario_logueado(request):
    if request.user.is_authenticated:
        username  = request.user.username
        id_usuario = User.objects.filter(username__icontains = username).values('id')
        id_grupo = Group.objects.filter(user__in = id_usuario).values('name')
        return id_grupo
    else:
        id_grupo = {}
        return id_grupo

def list_productos(request):
    id_grupo = usuario_logueado(request)
    producto = Productos.objects.all()
    context = {'object_list':producto, 'id_grupo':id_grupo}
    return render(request, 'products/productos.html', context=context)

def search_product(request):
    id_grupo = usuario_logueado(request)

    productos = Productos.objects.filter(nombre__icontains = request.GET['search'])
    marcas = Marcas.objects.filter(nombre__icontains = request.GET['search']).values('id')
    tipos = Tipo.objects.filter(categoria__icontains = request.GET['search']).values('id')
    if productos.exists():
        context = {'productos':productos, 'id_grupo':id_grupo}
    elif marcas.exists():
        productos = Productos.objects.filter(marca__in = marcas)
        context = {'productos':productos, 'id_grupo':id_grupo}
    elif tipos.exists():
        productos = Productos.objects.filter(tipo__in = tipos)
        context = {'productos':productos, 'id_grupo':id_grupo}
    else:
        context = {'errors':'No se encontraron productos.', 'id_grupo':id_grupo}
    return render(request, 'products/search_product.html', context = context)

def create_product(request):
    id_grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Productos_form()
            context = {'form':form, 'id_grupo':id_grupo}
            return render(request, 'products/create_product.html', context=context)
        else:
            form = Productos_form(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():
                new_product = Productos.objects.create(
                    nombre = form.cleaned_data['nombre'],
                    precio = form.cleaned_data['precio'],
                    sku = form.cleaned_data['sku'],
                    novedad = form.cleaned_data['novedad'],
                    marca = form.cleaned_data['marca'],
                    modelo = form.cleaned_data['modelo'],
                    tipo = form.cleaned_data['tipo'],
                    stock = form.cleaned_data['stock'],
                    descuento = form.cleaned_data['descuento'],
                    imagen = request.FILES['imagen'],
                    descripcion = form.cleaned_data['descripcion'],
                    active = form.cleaned_data['active']
                )
                new_product.save()
                context ={'new_product':new_product, 'id_grupo':id_grupo}
            return render(request, 'products/create_product.html', context=context)
    else:
        return redirect('index')

class List_productos(ListView):
    model = Productos
    template_name = 'products/productos.html'

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
    template_name = 'products/delete_producto.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        self.object.active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('productos')

class Update_product(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = 'products/update_producto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_producto', kwargs={'pk':self.object.pk})

class List_marcas(LoginRequiredMixin, ListView):
    model = Marcas
    template_name = 'distribuidores/marcas.html'

# class Detail_marca(LoginRequiredMixin, DetailView):
#     model = Marcas
#     template_name = 'distribuidores/detalle_marca.html'

class Create_marca(LoginRequiredMixin, CreateView):
    model = Marcas
    template_name= 'distribuidores/create_marca.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('marcas')

class Edit_marca(LoginRequiredMixin, UpdateView):
    model = Marcas
    template_name = 'distribuidores/edit_marca.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('marcas')

class Delete_marca(LoginRequiredMixin, DeleteView):
    model = Marcas
    template_name = 'distribuidores/delete_marca.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        print(self.object.active)
        self.object.active = False
        print(self.object.active)
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('marcas')

class List_distribuidor(LoginRequiredMixin, ListView):
    paginate_by = 6
    model = Distribuidores
    template_name = 'distribuidores/distribuidores.html'


# class Detail_distribuidor(LoginRequiredMixin, DetailView):
#     model = Distribuidores
#     template_name = 'distribuidores/detalle_distribuidor.html'

class Create_distribuidor(LoginRequiredMixin, CreateView):
    model = Distribuidores
    template_name= 'distribuidores/create_distribuidor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('distribuidores')

class Edit_distribuidor(LoginRequiredMixin, UpdateView):
    model = Distribuidores
    template_name = 'distribuidores/edit_distribuidor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('distribuidores')

class Delete_distribuidor(LoginRequiredMixin, DeleteView):
    model = Distribuidores
    template_name = 'distribuidores/delete_distribuidor.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        self.object.active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('distribuidores')

class Create_distribuidor_marca(LoginRequiredMixin, CreateView):
    model = Distribuidores_marcas
    template_name= 'distribuidores/create_distribuidor_marca.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('index')

class Create_tipo(LoginRequiredMixin, CreateView):
    model = Tipo
    template_name= 'products/create_tipo.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('tipos')

class List_tipo(LoginRequiredMixin, ListView):
    paginate_by = 6
    model = Tipo
    template_name = 'products/tipos.html'

class Edit_tipo(LoginRequiredMixin, UpdateView):
    model = Tipo
    template_name= 'products/edit_tipo.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('tipos')

class Delete_tipo(LoginRequiredMixin, DeleteView):
    model = Tipo
    template_name = 'products/delete_tipo.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        print(self.object.active)
        self.object.active = False
        print(self.object.active)
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('tipos')



#
# 
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