from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.template import loader 
from django.contrib.auth.decorators import login_required
from app_fam.models import *
from app_fam.forms  import *
from login.forms  import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login , authenticate

=======
from django.template import loader
 
from app_fam.models import *
from login.forms  import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
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
<<<<<<< HEAD
            return render( request, "login_error.html")
    

=======
            return HttpResponse( f"Form Incorrecto {form}" )
    
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
    form = AuthenticationForm()
    return render( request , "login.html" , { "form":form } )


<<<<<<< HEAD
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
=======
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



>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6

