from django.shortcuts import render
from productos.models import Productos
from productos.forms import Productos_form

# Create your views here.
def productos(request):
    producto = Productos.objects.all()
    print(producto) 
    context = {'producto':producto}
    return render(request, 'productos.html', context=context)

def search_product_view(request):
    print(request.GET)
    productos = Productos.objects.filter(modelo__contains = request.GET['search'])
    context = {'productos':productos}
    return render(request, 'search_product.html', context = context)
    #return render(request, 'search_product.html')

def create_product_view(request):
    if request.method == 'GET':
        form = Productos_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Productos_form(request.POST)
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
                imagen = form.cleaned_data['imagen'],
            )
            context ={'new_product':new_product}
        return render(request, 'create_product.html', context=context)