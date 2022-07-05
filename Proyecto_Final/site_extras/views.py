from django.shortcuts import render
from site_extras.models import Inicio, About
from productos.models import Productos
from distribuidores.models import Distribuidores
from marcas.models import Marcas
from categorias.models import Tipo
from accounts.models import User_profile
from django.contrib.auth.models import User, Group
from django.views.generic import ListView
from django_base.functions import usuario_logueado


def Leyendas_inicio(request):
    grupo = usuario_logueado(request)
    model = Inicio.objects.all()
    context = {'object_list':model, 'grupo':grupo}
    return render(request, 'index.html', context = context)


def Detalle_about(request):
    grupo = usuario_logueado(request)
    model = About.objects.all()
    context = {'object_list':model, 'grupo':grupo}
    return render(request, 'about.html', context = context)
  

def Detalle_site(request):
    grupo = usuario_logueado(request)
    producto_map = Productos.objects.all()
    distribuidores_map = Distribuidores.objects.all()
    marcas_map = Marcas.objects.all()
    tipo_map = Tipo.objects.all()
    user_profile_map = User_profile.objects.all()
    user_map = User.objects.all()
    group_map = Group.objects.all()
    context = {"producto_map":producto_map, "distribuidores_map": distribuidores_map, "marcas_map": marcas_map, "tipo_map": tipo_map, "user_profile_map": user_profile_map, "user_map": user_map, "group_map": group_map, 'grupo':grupo}
    return render(request, 'map.html', context = context)



