from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django_base.functions import usuario_logueado, paginator
from distribuidores.models import Distribuidores
from distribuidores.forms import Distribuidores_form

# Create your views here.
# Distribuidores
def list_distribuidor(request):
    if request.user.is_authenticated:
        distribuidores = Distribuidores.objects.all()
        context = paginator(request, distribuidores, 6)
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
            return HttpResponseRedirect('/distribuidores/distribuidores')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'distribuidores/update_distribuidor.html', context=context)
    else:
        return redirect('index')

def delete_distribuidor(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        marca = Distribuidores.objects.get(id = pk)
        context = {'object':marca, 'grupo':grupo}
        if request.method == 'POST':
            Distribuidores.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/distribuidores/distribuidores')
        return render(request, 'distribuidores/delete_distribuidor.html', context=context)       
    else:
        return redirect('index') 