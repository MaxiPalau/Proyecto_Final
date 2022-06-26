
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django_base.forms import Registro_usuario_form 

def index(request):
   return render(request, 'index.html', context = {})

def login_view(request):
   if request.method == 'POST':
      form = AuthenticationForm(request, data = request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(username=username, password=password)
         if user is not None:
            login(request, user)
            context = {'message':f'Ha iniciado sesión como {username}'}
            return render(request, 'index.html', context=context)
         else:
            form = AuthenticationForm()
            context = {'errors':'Nombre de usuario o contraseña incorrecto', 'form':form}
            return render(request, 'auth/login.html', context=context)
      else:
         f_error = form.errors
         for key in f_error:
            error = f_error[key]
         form = AuthenticationForm()
         context = {'errors':error, 'form':form}
         return render(request, 'auth/login.html', context=context) 

   else:
      form = AuthenticationForm()
      context = {'form':form}
      return render(request, 'auth/login.html', context=context)

def logout_view(request):
   logout(request)
   return redirect('index')

def register_view(request):
   boton = 0
   if request.method == 'POST':
      form = Registro_usuario_form(request.POST)
      
      if form.is_valid():
         form.save()
         mensaje = 'Usuario creado con éxito.'
         boton = 1
         context = {'message': mensaje, 'boton':boton}
         return render(request, 'auth/register.html', context=context)
      else:
         f_error = form.errors
         for key in f_error:
            error = f_error[key]
         form = Registro_usuario_form()
         context = {'errors':error, 'form':form, 'boton':boton}
         return render(request, 'auth/register.html', context=context) 
   else:
      form = Registro_usuario_form()
      context = {'form':form, 'boton':boton}
      return render(request, 'auth/register.html', context=context)
