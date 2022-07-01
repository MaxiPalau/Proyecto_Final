from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_marcas, Estados
from productos.forms import Productos_form, Marcas_form, Distribuidores_form, Distribuidores_marcas_form, Tipo_form

# Create your views here.

def usuario_logueado(request):
    if request.user.is_authenticated:
        username  = request.user.username
        id_usuario = User.objects.filter(username__icontains = username).values('id')
        lista_grupo = list(Group.objects.filter(user__in = id_usuario).values_list('name', flat=True))

        for grupo in lista_grupo:
            if grupo == 'Ferreteria':
                return True
            else:
                return False
        # return id_grupo
    else:
        return False

def paginator(request, object, item):
    # object = queryset, lista de objetos que se quieren paginar
    # item = int, cantidad de items por pagina
    grupo = usuario_logueado(request)
    pag = request.GET.get('page', 1)
    paginator = Paginator(object, item)
    try:
        resultados = paginator.page(pag)
    except PageNotAnInteger:
        resultados = paginator.page(1)
    except EmptyPage:
        resultados = paginator.page(paginator.num_pages)
    context = {'object_list':resultados, 'grupo':grupo}
    return context

# Productos basado en funciones obteniendo el grupo del usuario
def list_productos(request):
    producto = Productos.objects.all()
    context = paginator(request, producto, 6)
    return render(request, 'products/productos.html', context=context)
    # grupo = usuario_logueado(request)
    # producto = Productos.objects.all()
    # pag = request.GET.get('page', 1)
    # paginator = Paginator(producto, 6)
    # try:
    #     resultados = paginator.page(pag)
    # except PageNotAnInteger:
    #     resultados = paginator.page(1)
    # except EmptyPage:
    #     resultados = paginator.page(paginator.num_pages)
    # context = {'object_list':resultados, 'grupo':grupo}
    # return render(request, 'products/productos.html', context=context)

def search_product(request):
    grupo = usuario_logueado(request)
    productos = Productos.objects.filter(nombre__icontains = request.GET['search'])
    marcas = Marcas.objects.filter(nombre__icontains = request.GET['search']).values('id')
    tipos = Tipo.objects.filter(categoria__icontains = request.GET['search']).values('id')
    if productos.exists():
        context = {'productos':productos, 'grupo':grupo}
    elif marcas.exists():
        productos = Productos.objects.filter(marca__in = marcas)
        context = {'productos':productos, 'grupo':grupo}
    elif tipos.exists():
        productos = Productos.objects.filter(tipo__in = tipos)
        context = {'productos':productos, 'grupo':grupo}
    else:
        context = {'errors':'No se encontraron productos.', 'grupo':grupo}
    return render(request, 'products/search_product.html', context = context)

def create_product(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Productos_form()
            context = {'form':form, 'grupo':grupo}
            return render(request, 'products/create_product.html', context=context)
        else:
            form = Productos_form(request.POST, request.FILES)
            
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
                context ={'new_product':new_product, 'grupo':grupo}
            else:
                f_error = form.errors
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}
            return render(request, 'products/create_product.html', context=context)
    else:
        return redirect('index')

def detail_product(request,pk):
    grupo = usuario_logueado(request)
    producto = Productos.objects.get(id = pk)
    context = {'object':producto, 'grupo':grupo}
    return render(request, 'products/detalle_producto.html', context=context)

def update_product(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        producto = Productos.objects.get(id = pk)
        form = Productos_form(request.POST or None, instance= producto)
        if form.is_valid():
            form.save()
            context = {'form':form, 'grupo':grupo}
            return HttpResponseRedirect('/productos/detail-producto/'+ pk)
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo} 
        return render(request, 'products/update_producto.html', context=context)
    else:
        return redirect('index')

def delete_product(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        producto = Productos.objects.get(id = pk)
        context = {'object':producto, 'grupo':grupo}
        if request.method == 'POST':
            Productos.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/productos')
        return render(request, 'products/delete_producto.html', context=context)       
    else:
        return redirect('index') 

# Marcas basado en funciones obteniendo el grupo del usuario
def list_marcas(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marcas = Marcas.objects.all()
        pag = request.GET.get('page', 1)
        paginator = Paginator(marcas, 6)
        try:
            resultados = paginator.page(pag)
        except PageNotAnInteger:
            resultados = paginator.page(1)
        except EmptyPage:
            resultados = paginator.page(paginator.num_pages)
        context = {'object_list':resultados, 'grupo':grupo}
        return render(request, 'distribuidores/marcas.html', context=context)
    else:
        return redirect('index')

def create_marca(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Marcas_form()
            context ={'form':form, 'grupo':grupo}
            return render(request, 'distribuidores/create_marca.html', context=context)
        else:
            form = Marcas_form(request.POST)
            if form.is_valid():
                new_marca = Marcas.objects.create(
                    nombre = form.cleaned_data['nombre'],
                    descripcion = form.cleaned_data['descripcion'],
                    active = form.cleaned_data['active']
                )
                context = {'new_marca':new_marca, 'grupo':grupo}
            else:
                f_error = form.errors
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}
            return render(request, 'distribuidores/create_marca.html', context=context)
    else:
        return redirect('index')

def update_marca(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Marcas.objects.get(id = pk)
        form = Marcas_form(request.POST or None, instance= marca)
        if form.is_valid():
            form.save()
            context = {'form':form, 'grupo':grupo}
            return HttpResponseRedirect('/productos/marcas')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'distribuidores/edit_marca.html', context=context)
    else:
        return redirect('index')

def delete_marca(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Marcas.objects.get(id = pk)
        context = {'object':marca, 'grupo':grupo}
        if request.method == 'POST':
            Marcas.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/productos/marcas')
        return render(request, 'distribuidores/delete_marca.html', context=context)       
    else:
        return redirect('index') 

# Distribuidores
def list_distribuidor(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        distribuidores = Distribuidores.objects.all()
        pag = request.GET.get('page', 1)
        paginator = Paginator(distribuidores, 6)
        try:
            resultados = paginator.page(pag)
        except PageNotAnInteger:
            resultados = paginator.page(1)
        except EmptyPage:
            resultados = paginator.page(paginator.num_pages)

        context = {'object_list':resultados, 'grupo':grupo}
        return render(request, 'distribuidores/distribuidores.html', context=context)
    else:
        return redirect('index')

def create_distribuidor(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Distribuidores_form()
            context ={'form':form, 'grupo':grupo}
            return render(request, 'distribuidores/create_distribuidor.html', context=context)
        else:
            form = Distribuidores_form(request.POST)
            if form.is_valid():
                new_distribuidor = Distribuidores.objects.create(
                    razon_social = form.cleaned_data['razon_social'],
                    direccion = form.cleaned_data['direccion'],
                    localidad = form.cleaned_data['localidad'],
                    pais = form.cleaned_data['pais'],
                    telefono = form.cleaned_data['telefono'],
                    mail = form.cleaned_data['mail'],
                    web = form.cleaned_data['web'],
                    cuit = form.cleaned_data['cuit'],
                    descripcion = form.cleaned_data['descripcion'],
                    active = form.cleaned_data['active']
                )
                context = {'new_distribuidor':new_distribuidor, 'grupo':grupo}
            else:
                f_error = form.errors
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}
            return render(request, 'distribuidores/create_distribuidor.html', context=context)
    else:
        return redirect('index')

def update_distribuidor(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Distribuidores.objects.get(id = pk)
        form = Distribuidores_form(request.POST or None, instance= marca)
        if form.is_valid():
            form.save()
            context = {'form':form, 'grupo':grupo}
            return HttpResponseRedirect('/productos/distribuidores')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'distribuidores/edit_distribuidor.html', context=context)
    else:
        return redirect('index')

def delete_distribuidor(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Distribuidores.objects.get(id = pk)
        context = {'object':marca, 'grupo':grupo}
        if request.method == 'POST':
            Distribuidores.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/productos/distribuidores')
        return render(request, 'distribuidores/delete_distribuidor.html', context=context)       
    else:
        return redirect('index') 

def distribuidor_marca(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Distribuidores_marcas_form()
            context = {'form':form, 'grupo':grupo}
            return render(request, 'distribuidores/create_distribuidor_marca.html', context=context)
        else:
            form = Distribuidores_marcas_form(request.POST)
            if form.is_valid():
                new_distribuidor_m = Distribuidores_marcas.objects.create(
                    marca = form.cleaned_data['marca'],
                    distribuidor = form.cleaned_data['distribuidor'],
                )
                context ={'new_distribuidor_m':new_distribuidor_m, 'grupo':grupo}
            else:
                    f_error = form.errors
                    for key in f_error:
                        error = f_error[key]
                    context = {'errors':error, 'form':form, 'grupo':grupo}
            return render(request, 'distribuidores/create_distribuidor_marca.html', context=context)
    else:
        return redirect('index')

# Categorias/Tipos
def list_tipo(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        tipos = Tipo.objects.all()
        pag = request.GET.get('page', 1)
        paginator = Paginator(tipos, 6)
        try:
            resultados = paginator.page(pag)
        except PageNotAnInteger:
            resultados = paginator.page(1)
        except EmptyPage:
            resultados = paginator.page(paginator.num_pages)

        context = {'object_list':resultados, 'grupo':grupo}
        return render(request, 'products/tipos.html', context=context)
    else:
        return redirect('index')  

def create_tipo(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Tipo_form()
            context ={'form':form, 'grupo':grupo}
            return render(request, 'products/create_tipo.html', context=context)
        else:
            form = Tipo_form(request.POST)
            if form.is_valid():
                new_tipo = Tipo.objects.create(
                    categoria = form.cleaned_data['categoria'],
                    descripcion = form.cleaned_data['descripcion'],
                    active = form.cleaned_data['active']
                )
                context = {'new_tipo':new_tipo, 'grupo':grupo}
            else:
                f_error = form.errors
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}
            return render(request, 'products/create_tipo.html', context=context)
    else:
        return redirect('index')

def update_tipo(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Tipo.objects.get(id = pk)
        form = Tipo_form(request.POST or None, instance= marca)
        if form.is_valid():
            form.save()
            context = {'form':form, 'grupo':grupo}
            return HttpResponseRedirect('/productos/tipos')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'products/edit_tipo.html', context=context)
    else:
        return redirect('index')

def delete_tipo(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        categoria = Tipo.objects.get(id = pk)
        context = {'object':categoria, 'grupo':grupo}
        if request.method == 'POST':
            Tipo.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/productos/tipos')
        return render(request, 'products/delete_tipo.html', context=context)       
    else:
        return redirect('index') 


#############################################################################################
# Lo que sigue a partir de acá está basado en clases, pero no pude obtener la información del usuario y que traiga los datos de la base.


# # Productos basado en clases sin el grupo del usuario
# class List_productos(ListView):
#     model = Productos
#     template_name = 'products/productos.html'
#     # context = 'object_list'
#     # print(f'Context List_products {context}')

#     # def get(self, *args, **kwargs):
#     #     user_id = self.request.user.pk
#     #     context = super().get(*args, **kwargs)
#     #     context['object_list'] = user_id
#     #     print(f'Context def {context}')
#     #     return context 

# class Create_product(LoginRequiredMixin, CreateView):
#     model = Productos
#     template_name = 'products/create_product.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('detail_producto', kwargs={'pk':self.object.pk})

# class Detail_product(DetailView):
#     model = Productos
#     template_name = 'products/detalle_producto.html'

# class Delete_product(LoginRequiredMixin, DeleteView):
#     model = Productos
#     template_name = 'products/delete_producto.html'

#     def form_valid(self, form):
#         success_url = self.get_success_url()
#         self.object = self.get_object()
#         self.object.active = False
#         self.object.save()
#         return HttpResponseRedirect(success_url)

#     def get_success_url(self):
#         return reverse('productos')

# class Update_product(LoginRequiredMixin, UpdateView):
#     model = Productos
#     template_name = 'products/update_producto.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('detail_producto', kwargs={'pk':self.object.pk})

# # Marcas basado en funciones obteniendo el grupo del usuario
# class List_marcas(LoginRequiredMixin, ListView):
#     model = Marcas
#     template_name = 'distribuidores/marcas.html'

# class Create_marca(LoginRequiredMixin, CreateView):
#     model = Marcas
#     template_name= 'distribuidores/create_marca.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('marcas')

# class Edit_marca(LoginRequiredMixin, UpdateView):
#     model = Marcas
#     template_name = 'distribuidores/edit_marca.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('marcas')

# class Delete_marca(LoginRequiredMixin, DeleteView):
#     model = Marcas
#     template_name = 'distribuidores/delete_marca.html'

#     def form_valid(self, form):
#         success_url = self.get_success_url()
#         self.object = self.get_object()
#         print(self.object.active)
#         self.object.active = False
#         print(self.object.active)
#         self.object.save()
#         return HttpResponseRedirect(success_url)

#     def get_success_url(self):
#         return reverse('marcas')

# class List_distribuidor(LoginRequiredMixin, ListView):
#     paginate_by = 6
#     model = Distribuidores
#     template_name = 'distribuidores/distribuidores.html'

# class Create_distribuidor(LoginRequiredMixin, CreateView):
#     model = Distribuidores
#     template_name= 'distribuidores/create_distribuidor.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('distribuidores')

# class Edit_distribuidor(LoginRequiredMixin, UpdateView):
#     model = Distribuidores
#     template_name = 'distribuidores/edit_distribuidor.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('distribuidores')

# class Delete_distribuidor(LoginRequiredMixin, DeleteView):
#     model = Distribuidores
#     template_name = 'distribuidores/delete_distribuidor.html'

#     def form_valid(self, form):
#         success_url = self.get_success_url()
#         self.object = self.get_object()
#         self.object.active = False
#         self.object.save()
#         return HttpResponseRedirect(success_url)

#     def get_success_url(self):
#         return reverse('distribuidores')

# class Create_distribuidor_marca(LoginRequiredMixin, CreateView):
#     model = Distribuidores_marcas
#     template_name= 'distribuidores/create_distribuidor_marca.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('index')

# class Create_tipo(LoginRequiredMixin, CreateView):
#     model = Tipo
#     template_name= 'products/create_tipo.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('tipos')

# class List_tipo(LoginRequiredMixin, ListView):
#     paginate_by = 6
#     model = Tipo
#     template_name = 'products/tipos.html'

# class Edit_tipo(LoginRequiredMixin, UpdateView):
#     model = Tipo
#     template_name= 'products/edit_tipo.html'
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('tipos')

# class Delete_tipo(LoginRequiredMixin, DeleteView):
#     model = Tipo
#     template_name = 'products/delete_tipo.html'

#     def form_valid(self, form):
#         success_url = self.get_success_url()
#         self.object = self.get_object()
#         print(self.object.active)
#         self.object.active = False
#         print(self.object.active)
#         self.object.save()
#         return HttpResponseRedirect(success_url)

#     def get_success_url(self):
#         return reverse('tipos')

