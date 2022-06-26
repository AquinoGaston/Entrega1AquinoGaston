from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.contrib.auth.decorators import login_required
from app_fam.models import *
from app_fam.forms  import *
from login.forms  import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login , authenticate

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
            return render( request, "login_error.html")
    

    form = AuthenticationForm()
    return render( request , "login.html" , { "form":form } )


def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"padre.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})


@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data 
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.first_name = informacion['first_name']
                  passw = informacion['password1']
                  usuario.set_password(passw)
               #   usuario.password2 = informacion['password2']
                  usuario.save()

                  return render(request, "padre.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name}) 

      #Voy al html que me permite editar
      return render(request, "editarperfil.html", {"miFormulario":miFormulario, "usuario":usuario})

