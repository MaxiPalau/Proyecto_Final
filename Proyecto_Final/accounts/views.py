from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from accounts.forms import Registro_usuario_form, User_edit_form, Profile_form, Update_profile_form
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
            #return render(request, 'index.html', context=context)
            return redirect('index')
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

@login_required
def profile_view(request):
   try:
      grupo = usuario_logueado(request)
      username  = request.user.username
      id_usuario = list(User.objects.filter(username__icontains = username).values_list('id', flat=True))
      profile =  User_profile.objects.get(username_id = id_usuario[0])
      value = True 
      context = {'object':profile, 'grupo':grupo, 'value':value}
      return render(request, 'accounts/profile.html', context=context) 
   except ObjectDoesNotExist:
      error = 'El usuario no posee perfil'
      value = False
      context = {'errors':error, 'grupo':grupo, 'value':value}
      return render(request, 'accounts/profile.html', context=context)

@login_required
def create_profile(request):
   grupo = usuario_logueado(request)
   if request.method == 'GET':
      try:
         boton = True
         username  = request.user.username
         id_usuario = list(User.objects.filter(username__icontains = username).values_list('id', flat=True))
         profile =  User_profile.objects.get(username_id = id_usuario[0])
         form = Profile_form(initial={
               'descripcion':profile.descripcion,
               'link':profile.link,
               'image':profile.image
               })
         context ={'form':form, 'grupo':grupo, 'boton':boton}
      except ObjectDoesNotExist:
         form = Profile_form()
         boton = False
         context ={'form':form, 'grupo':grupo, 'boton':boton}
   else:
      form = Profile_form(request.POST, request.FILES)
      if form.is_valid():
         usuario = User.objects.get(username=request.user)
         new_profile = User_profile.objects.create(
            username = usuario,
            descripcion = form.cleaned_data['descripcion'],
            link = form.cleaned_data['link'],
            image = request.FILES['image'],
         )
         new_profile.save()
         context = {'new_profile':new_profile, 'grupo':grupo}
         return HttpResponseRedirect('/accounts/profile/')
      else:
         f_error = form.errors        
         if f_error.__len__() == 0:
            context = {'form':form, 'grupo':grupo}
         else:
            for key in f_error:
               error = f_error[key]
            context = {'errors':error, 'form':form, 'grupo':grupo}        
   return render(request, 'accounts/create_profile.html', context=context)

@login_required
def update_profile(request, pk):
   grupo = usuario_logueado(request)
   user = request.user
   perfil = User_profile.objects.get(id = pk)
   if request.method == 'POST':
      form_user = User_edit_form(request.POST)
      form_profile = Update_profile_form(request.POST, request.FILES)
      if form_user.is_valid() and form_profile.is_valid():
         datos_user = form_user.cleaned_data
         user.email = datos_user['email']
         user.password1 = datos_user['password1']
         user.password2 = datos_user['password2']
         user.first_name = datos_user['first_name']
         user.last_name = datos_user['last_name']
         user.save()
         datos_profile = form_profile.cleaned_data
         perfil.descripcion = datos_profile['descripcion']
         perfil.link = datos_profile['link']
         perfil.image = request.FILES['image']
         perfil.save()
         return HttpResponseRedirect('/accounts/profile/')
      else:
         f_error_user = form_user.errors
         f_error_perfil = form_profile.errors
         for key in f_error_user:
            error_user = f_error_user[key]
         for key in f_error_perfil:
            error_perfil = f_error_perfil[key]
         context = {'error_user':error_user, 'error_perfil':error_perfil,'form_user':form_user, 'form_profile':form_profile, 'grupo':grupo}
         return render(request, 'accounts/update_profile.html', context=context)
   else:
      form_user = User_edit_form(
         initial={
         'email':user.email, 
         'first_name':user.first_name,
         'last_name':user.last_name
         }
         )
      form_profile = Update_profile_form(
         initial={
            'descripcion':perfil.descripcion,
            'link':perfil.link,
            'image':perfil.image
            }
         )
   context = {'form_user':form_user, 'grupo':grupo, 'user':user, 'form_profile':form_profile}
   return render(request, 'accounts/update_profile.html', context=context)