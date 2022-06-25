from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 
from app_fam.models import *
from login.forms  import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

  
def login_request( request ):

    if request.method == "POST":

        form = AuthenticationForm( request , data= request.POST )

        if form.is_valid():
            
            usuario = form.cleaned_data.get( "username" )
            contra = form.cleaned_data.get( "password" ) 

            user = authenticate( username = usuario , password = contra )

            if user is not None :

                login( request , user )

                return render( request , "LoginInicio.html" , {"mensaje": f"Bienvenido usuario { usuario }" } )

            else:
                return HttpResponse( f"Usuario Incorrecto" )

        else: 
            return HttpResponse( f"Form Incorrecto {form}" )
    
    form = AuthenticationForm()
    return render( request , "login.html" , { "form":form } )


def register (request):

    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)

        if form.is_valid:
            form.save()
            return HttpResponse ("Usuario Creado")

    else:
        form = UserCreationForm()

    return render (request, "registro.html", {"form":form})    

@login_required
def editarPerfil (request):

    usuario = request.user

    if request.method == 'POST':
        
        miformulario = UserEditForm (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request , "padre.html")
    else:

        miformulario = UserEditForm(initial = {'email':usuario.email})

    return render (request,"editar_perfil.html",{'miformulario':miformulario , 'usuario':usuario} )    




