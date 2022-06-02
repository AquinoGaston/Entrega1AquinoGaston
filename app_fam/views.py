from django.http import HttpResponse
from django.shortcuts import render 
from django.template import loader    
from app_fam.models import *
from app_fam.forms  import *
 # Create your views here. 

def inicio (request):

    return render(request, "padre.html")

def alta_usuarios (request):

    if request.method == "POST":
        
        mi_formulario = Alta_usuario (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            usuario = Usuario(nombre = datos['nombre'], dni = datos['dni'],descripcion = datos['descripcion'])
            usuario.save()

            return render(request, "alta_usuarios.html")

    return render(request, "alta_usuarios.html")    


def usuarios (request):

    usuarios = Usuario.objects.all()
    datos = {"usuario": usuarios}
    plantilla = loader.get_template ("usuarios.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)


def alta_articulos(request):
 
    if request.method == "POST":
        
        mi_formulario = Alta_articulos (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            articulo = Articulo(nom_art = datos['nom_art'], codigo = datos['codigo'],precio = datos['precio'],stock =datos ['stock'], categoria = datos ['categoria'])
            articulo.save()

            return render(request, "alta_articulos.html")    

 

    return render(request, "alta_articulos.html")    
   

def articulos (request):

    articulo= Articulo.objects.all()
    datos = {"articulo": articulo}
    plantilla = loader.get_template ("articulos.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)
    

def alta_vendedores(request):
 
    if request.method == "POST":
        
        mi_formulario = Alta_vendedor (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            articulo =  Vendedor(nom_vendedor = datos['nom_vendedor'], cuit = datos['cuit'],direccion = datos['direccion'],emaeil =datos ['emaeil'])
            articulo.save()

            return render(request, "alta_vendedores.html")

    return render(request, "alta_vendedores.html") 

def vendedores (request):

    vendedor= Vendedor.objects.all()
    datos = {"vendedor": vendedor}
    plantilla = loader.get_template ("vendedores.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)







def buscar (request):

    return render(request, "buscar.html")


def busqueda (request):

    if request.POST['nombre']:

        nombre = request.POST['nombre']

        dato = Usuario.objects.filter(nombre__icontains = nombre)

        return render(request, "resultado_busqueda.html",{"datos":dato})

    else:

        return HttpResponse("Campo vacio") 


def buscar_articulo (request):

    return render(request, "buscar_articulo.html")


def busqueda_articulo (request):

    if request.POST['nom_art']:

        nom_art = request.POST['nom_art']

        dato = Articulo.objects.filter(nom_art__icontains = nom_art)

        return render(request, "articulo_busqueda.html",{"datos":dato})

    else:

        return HttpResponse("Campo vacio") 





def buscar_vendedor (request):

    return render(request, "buscar_vendedor.html")


def busqueda_vendedor(request):

    if request.POST['nom_vendedor']:

        nom_vendedor = request.POST['nom_vendedor']

        dato = Vendedor.objects.filter(nom_vendedor__icontains = nom_vendedor)

        return render(request, "vendedor_busqueda.html",{"datos":dato})

    else:

        return HttpResponse("Campo vacio")         