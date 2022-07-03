from django.shortcuts import render
from django.http import HttpResponse

from app_fam.models import *
from app_fam.forms  import *
from django.template import loader
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

                avatares = Avatar.objects.filter(user=request.user.id)

                return render( request , "LoginInicio.html", {"url":avatares[0].imagen.url, "mensaje": f"Bienvenido { usuario }" }) 
                #, {"mensaje": f"Bienvenido { usuario }" } )

            else:
                return HttpResponse( f"Usuario Incorrecto" )

        else: 


            return render(request, "login_error.html" )

    form = AuthenticationForm()
    return render( request , "login.html" , { "form":form } )



def register (request):

    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "LoginInicio.html")

    else:
        form = UserRegisterForm()

    return render (request, "registro.html", {"form":form})
    
    

@login_required
def editarPerfil (request):

    usuario = request.user

    if request.method == 'POST':
        
        miformulario = UserEditForm (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request , "padre.html")
    else:

        miformulario = UserEditForm(initial = {'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})

    return render (request,"editar_perfil.html",{'miformulario':miformulario , 'usuario':usuario} )    

