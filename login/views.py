from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
   
from app_fam.models import *
from app_fam.forms  import *
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
            return HttpResponse( f"Form Incorrecto {form}" )
    

    

    form = AuthenticationForm()
    return render( request , "login.html" , { "form":form } )



