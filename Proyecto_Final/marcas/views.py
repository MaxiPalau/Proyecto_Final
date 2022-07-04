from django.shortcuts import render,redirect
from django_base.functions import usuario_logueado, paginator
from django.http import HttpResponseRedirect
from marcas.models import Marcas
from marcas.forms import Marcas_form

# Create your views here.
# Marcas basado en funciones obteniendo el grupo del usuario
def list_marcas(request):
    if request.user.is_authenticated:
        marcas = Marcas.objects.all().order_by('id')
        context = paginator(request, marcas, 6)
        return render(request, 'marcas/marcas.html', context=context)
    else:
        return redirect('index')

def create_marca(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Marcas_form()
            context ={'form':form, 'grupo':grupo}
            return render(request, 'marcas/create_marca.html', context=context)
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
            return render(request, 'marcas/create_marca.html', context=context)
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
            return HttpResponseRedirect('/marcas/marcas')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'marcas/update_marca.html', context=context)
    else:
        return redirect('index')

def delete_marca(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Marcas.objects.get(id = pk)
        context = {'object':marca, 'grupo':grupo}
        if request.method == 'POST':
            Marcas.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/marcas/marcas')
        return render(request, 'marcas/delete_marca.html', context=context)       
    else:
        return redirect('index') 
