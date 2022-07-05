from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django_base.functions import usuario_logueado, paginator
from productos.models import Productos, Estados
from productos.forms import Productos_form
from marcas.models import Marcas
from categorias.models import Tipo

# Create your views here.
# Productos basado en funciones obteniendo el grupo del usuario
def list_productos(request):
    producto = Productos.objects.all().order_by('id')
    context = paginator(request, producto, 6)
    return render(request, 'products/productos.html', context=context)

def search_product(request):
    grupo = usuario_logueado(request)   
    productos = Productos.objects.filter(nombre__icontains = request.GET['search']).order_by('id')
    marcas = Marcas.objects.filter(nombre__icontains = request.GET['search']).values('id')
    tipos = Tipo.objects.filter(categoria__icontains = request.GET['search']).values('id')
    if productos.exists():
        context = {'object_list':productos, 'grupo':grupo}
        # context = paginator(request, productos, 6)
    elif marcas.exists():
        productos = Productos.objects.filter(marca__in = marcas).order_by('id')
        context = {'object_list':productos, 'grupo':grupo}
        # context = paginator(request, productos, 6)

    elif tipos.exists():
        productos = Productos.objects.filter(tipo__in = tipos).order_by('id')
        context = {'object_list':productos, 'grupo':grupo}
        # context = paginator(request, productos, 6)
    else:
        # grupo = usuario_logueado(request)
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
        form = Productos_form(request.POST or None, request.FILES or None, instance= producto)
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

def compra_product(request,pk):
    grupo = usuario_logueado(request)
    producto = Productos.objects.get(id = pk)
    context = {'object':producto, 'grupo':grupo}
    return render(request, 'products/compra.html', context=context)