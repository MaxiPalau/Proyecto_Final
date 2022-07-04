from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from accounts.forms import Registro_usuario_form, Profile_form
from django_base.functions import usuario_logueado
from accounts.models import User_profile



def login_view(request):
   if request.method == 'POST':
      form = AuthenticationForm(request, data = request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(username=username, password=password)
         if user is not None:
            login(request, user)
            grupo = usuario_logueado(request)           
            context = {'message':f'Ha iniciado sesión como {username}', 'grupo':grupo}
            return render(request, 'index.html', context=context)
         else:
            form = AuthenticationForm()
            context = {'errors':'Nombre de usuario o contraseña incorrecto', 'form':form}
            return render(request, 'accounts/login.html', context=context)
      else:
         f_error = form.errors
         for key in f_error:
            error = f_error[key]
         form = AuthenticationForm()
         context = {'errors':error, 'form':form}
         return render(request, 'accounts/login.html', context=context) 

   else:
      form = AuthenticationForm()
      context = {'form':form}
      return render(request, 'accounts/login.html', context=context)

def logout_view(request):
   logout(request)
   return redirect('index')

def register_view(request):
   boton = 0
   if request.method == 'POST':
      form = Registro_usuario_form(request.POST)
      
      if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         mensaje = f'Usuario {username} creado con éxito.'
         boton = 1
         context = {'message': mensaje, 'boton':boton}
         return render(request, 'accounts/register.html', context=context)
      else:
         f_error = form.errors
         for key in f_error:
            error = f_error[key]
         form = Registro_usuario_form()
         context = {'errors':error, 'form':form, 'boton':boton}
         return render(request, 'accounts/register.html', context=context) 
   else:
      form = Registro_usuario_form()
      context = {'form':form, 'boton':boton}
      return render(request, 'accounts/register.html', context=context)

def profile_view(request):
   if request.user.is_authenticated:
      try:
         grupo = usuario_logueado(request)
         username  = request.user.username
         id_usuario = list(User.objects.filter(username__icontains = username).values_list('id', flat=True))
         profile =  User_profile.objects.get(username_id = id_usuario[0])
         value = True 
         context = {'object':profile, 'grupo':grupo, 'value':value}
         render(request, 'accounts/profile.html', context=context)
         return render(request, 'accounts/profile.html', context=context) 
      except ObjectDoesNotExist:
         error = 'El usuario no posee perfil'
         value = False
         context = {'errors':error, 'grupo':grupo, 'value':value}
         return render(request, 'accounts/profile.html', context=context) 
   else:
      return redirect('index')

def create_profile(request):
   grupo = usuario_logueado(request)
   if request.user.is_authenticated:
      if request.method == 'GET':
         # username  = request.user.username
         # id_usuario = list(User.objects.filter(username__icontains = username).values_list('id', flat=True))
         form = Profile_form()
         context ={'form':form, 'grupo':grupo}
      # username  = request.user.username
      # id_usuario = list(User.objects.filter(username__icontains = username).values_list('id', flat=True))
      # profile =  User_profile.objects.get(username_id = id_usuario[0]) 
      # # perfil = User_profile.objects.get(id = pk)
      # form = Profile_form(request.GET or None, instance= profile)
      else:
         form = Profile_form(request.POST, request.FILES)
         username  = request.user.username
         id_usuario = list(User.objects.filter(username__icontains = username).values_list('id', flat=True))
         form.username = id_usuario
         print(f'ID USUARIO: {id_usuario}')
         for item, v in form.fields:
            print(item, v)
         print(form.fields.username)
         print(form.cleaned_data['first name'])
         print(form.cleaned_data['last name'])
         print(form.cleaned_data['email'])
         print(form.cleaned_data['phone'])
         print(request.FILES['image'])
         if form.is_valid():
            print('FORMULARIO VALIDO')
            new_profile = User_profile.objects.create(
               username = form.cleaned_data['username'],
               first_name = form.cleaned_data['first name'],
               last_name = form.cleaned_data['last name'],
               email = form.cleaned_data['email'],
               phone = form.cleaned_data['phone'],
               image = request.FILES['image'],
            )
            new_profile.save()
            context = {'new_profile':new_profile, 'grupo':grupo}
            return HttpResponseRedirect('/accounts/profile/')
         else:
            print('entro al else del eror')
            f_error = form.errors        
            if f_error.__len__() == 0:
               context = {'form':form, 'grupo':grupo}
            else:
               for key in f_error:
                  error = f_error[key]
               context = {'errors':error, 'form':form, 'grupo':grupo}        
      return render(request, 'accounts/create_profile.html', context=context)
   else:
      return redirect('index')
   # grupo = usuario_logueado(request)
   # if request.user.is_authenticated:
   #    if request.method == 'GET':
   #       form = Profile_form()
   #       context ={'form':form, 'grupo':grupo}
   #       return render(request, 'accounts/create_profile.html', context=context)
   #    else:
   #       form = Profile_form(request.POST)
   #       if form.is_valid():
   #             new_profile = Profile_form.objects.create(
   #                username = form.cleaned_data['username'],
   #                first_name = form.cleaned_data['first_name'],
   #                last_name = form.cleaned_data['last_name'],
   #                email = form.cleaned_data['email'],
   #                phone = form.cleaned_data['phone'],
   #                image = request.FILES['image'],
   #             )
   #             context = {'new_profile':new_profile, 'grupo':grupo}
   #       else:
   #          f_error = form.errors
   #          for key in f_error:
   #             error = f_error[key]
   #             context = {'errors':error, 'form':form, 'grupo':grupo}
   #       return render(request, 'accounts/create_profile.html', context=context)
   # else:
   #    return redirect('index')

def update_profile(request, pk):
   grupo = usuario_logueado(request)
   if request.user.is_authenticated:
      perfil = User_profile.objects.get(id = pk)
      form = Profile_form(request.POST or None, instance= perfil)
      if form.is_valid():
         form.save()
         context = {'form':form, 'grupo':grupo}
         return HttpResponseRedirect('/accounts/profile/')
      else:
         f_error = form.errors        
         if f_error.__len__() == 0:
            context = {'form':form, 'grupo':grupo}
         else:
            for key in f_error:
               error = f_error[key]
            context = {'errors':error, 'form':form, 'grupo':grupo}        
      return render(request, 'accounts/update_profile.html', context=context)
   else:
      return redirect('index')
