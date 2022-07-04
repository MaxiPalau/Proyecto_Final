from django.shortcuts import render
from site_extras.models import Inicio, About
from django.views.generic import ListView

class Leyendas_inicio(ListView):
    model = Inicio
    template_name = 'index.html'

class Detalle_about(ListView):
    model = About
    template_name = 'about.html'