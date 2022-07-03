from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django_base.functions import usuario_logueado, paginator
from categorias.models import Tipo
from categorias.forms import Tipo_form

# Create your views here.
# Categorias/Tipos
def list_tipo(request):
    if request.user.is_authenticated:
        tipos = Tipo.objects.all()
        context = paginator(request, tipos, 6)
        return render(request, 'categorias/tipos.html', context=context)
    else:
        return redirect('index')  

def create_tipo(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Tipo_form()
            context ={'form':form, 'grupo':grupo}
            return render(request, 'categorias/create_tipo.html', context=context)
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
            return render(request, 'categorias/create_tipo.html', context=context)
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
            return HttpResponseRedirect('/categorias/tipos')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'categorias/update_tipo.html', context=context)
    else:
        return redirect('index')

def delete_tipo(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        categoria = Tipo.objects.get(id = pk)
        context = {'object':categoria, 'grupo':grupo}
        if request.method == 'POST':
            Tipo.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/categorias/tipos')
        return render(request, 'categorias/delete_tipo.html', context=context)       
    else:
        return redirect('index') 