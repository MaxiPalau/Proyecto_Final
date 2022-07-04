from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django_base.functions import usuario_logueado, paginator
from dist_marca.models import Distribuidores_marcas
from dist_marca.forms import Distribuidores_marcas_form


# Create your views here.
# Distribuidores x marcas

def list_distribuidor_marca(request):
    if request.user.is_authenticated:
        distribuidores_m = Distribuidores_marcas.objects.all().order_by('id')
        context = paginator(request, distribuidores_m, 6)
        return render(request, 'dist_marca/list_dist_marca.html', context=context)
    else:
        return redirect('index')

def create_distribuidor_marca(request):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Distribuidores_marcas_form()
            context = {'form':form, 'grupo':grupo}
            return render(request, 'dist_marca/create_dist_marca.html', context=context)
        else:
            form = Distribuidores_marcas_form(request.POST)
            if form.is_valid():
                new_distribuidor_m = Distribuidores_marcas.objects.create(
                    marca = form.cleaned_data['marca'],
                    distribuidor = form.cleaned_data['distribuidor'],
                    active = form.cleaned_data['active'] 
                )
                context ={'new_distribuidor_m':new_distribuidor_m, 'grupo':grupo}
            else:
                    f_error = form.errors
                    for key in f_error:
                        error = f_error[key]
                    context = {'errors':error, 'form':form, 'grupo':grupo}
            return render(request, 'dist_marca/create_dist_marca.html', context=context)
    else:
        return redirect('index')

def update_distribuidor_marca(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        dist_marca = Distribuidores_marcas.objects.get(id = pk)
        form = Distribuidores_marcas_form(request.POST or None, instance= dist_marca)
        if form.is_valid():
            form.save()
            context = {'form':form, 'grupo':grupo}
            return HttpResponseRedirect('/dist_marca/dist-marca')
        else:
            f_error = form.errors        
            if f_error.__len__() == 0:
                context = {'form':form, 'grupo':grupo}
            else:
                for key in f_error:
                    error = f_error[key]
                context = {'errors':error, 'form':form, 'grupo':grupo}        
        return render(request, 'dist_marca/update_dist_marca.html', context=context)
    else:
        return redirect('index')
        
def delete_distribuidor_marca(request, pk):
    grupo = usuario_logueado(request)
    if request.user.is_authenticated:
        dist_marca = Distribuidores_marcas.objects.get(id = pk)
        context = {'object':dist_marca, 'grupo':grupo}
        if request.method == 'POST':
            Distribuidores_marcas.objects.filter(id = pk).update(active = False)
            return HttpResponseRedirect('/dist_marca/dist-marca')
        return render(request, 'dist_marca/delete_dist_marca.html', context=context)       
    else:
        return redirect('index') 
