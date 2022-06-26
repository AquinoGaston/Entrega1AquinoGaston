
from django.http import HttpResponse
from django.shortcuts import render 
from django.template import loader    
from app_fam.models import *
from app_fam.forms  import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

 # Create your views here. 

def inicio (request):

    return render(request, "padre.html")

def about (request):

    return render(request, "about.html")


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
    return render(request,"usuarios.html",datos)


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
    return render(request, "articulos.html",datos)
  

def alta_vendedores(request):
 
    if request.method == "POST":
        
        mi_formulario = Alta_vendedor (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            articulo =  Vendedor(nom_vendedor = datos['nom_vendedor'], cuit = datos['cuit'],direccion = datos['direccion'],Email =datos ['Email'])
            articulo.save()

            return render(request, "alta_vendedores.html")

    return render(request, "alta_vendedores.html") 

def vendedores (request):

    vendedor= Vendedor.objects.all()
    datos = {"vendedor": vendedor}
    return render(request, "vendedores.html", datos)


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

def eliminar_articulo(request, id):
    arts = Articulo.objects.get(id=id)
    arts.delete()

    arts = Articulo.objects.all()
    return render(request,"articulos.html", {"articulo":arts})

def eliminar_usuario(request, id):
    us = Usuario.objects.get(id=id)
    us.delete()

    us = Usuario.objects.all()
    return render(request,"usuarios.html", {"usuario":us})

def eliminar_vendedor(request, id):
    ven = Vendedor.objects.get(id=id)
    ven.delete()

    ven = Vendedor.objects.all()
    return render(request,"vendedores.html", {"vendedor":ven})

def editar_vendedor(request, id):
    vend = Vendedor.objects.get(id=id)
    
    if request.method=="POST":
        miform = Alta_vendedor(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            vend.nom_vendedor = datos["nom_vendedor"]
            vend.direccion = datos["direccion"]
            vend.cuit = datos["cuit"]
            vend.emaeil = datos["emaeil"]
            vend.save()

            vend = Vendedor.objects.all()
            return render (request, "vendedores.html", {"vendedor":vend})

    else:
        miform = Alta_vendedor(initial={"nom_vendedor":vend.nom_vendedor, "direccion":vend.direccion,"cuit":vend.cuit,"emaeil":vend.emaeil})

    return render(request,"editar_vendedor.html",{"miform":miform, "vendedor":vend})



def editar_usuario(request, id):
    us = Usuario.objects.get(id=id)
    
    if request.method=="POST":
        miform = Alta_usuario(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            us.nombre = datos["nombre"]
            us.dni = datos["dni"]
            us.descripcion = datos["descripcion"]
            us.save()

            us = Usuario.objects.all()
            return render (request, "usuarios.html", {"usuario":us})

    else:
        miform = Alta_usuario(initial={"nombre":us.nombre, "dni":us.dni,"descripcion":us.descripcion})

    return render(request,"editar_usuario.html",{"miform":miform, "usuario":us})

def editar_articulo(request, id):
    art = Articulo.objects.get(id=id)
    
    if request.method=="POST":
        miform = Alta_articulos(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            art.nom_art = datos["nom_art"]
            art.codigo = datos["codigo"]
            art.precio = datos["precio"]
            art.stock = datos["stock"]
            art.categoria = datos["categoria"]
            art.save()

            art = Articulo.objects.all()
            return render (request, "articulos.html", {"articulo":art})

    else:
        miform = Alta_articulos(initial={"nom_art":art.nom_art, "codigo":art.codigo,"precio":art.precio,"stock":art.stock,"categoria":art.categoria})

    return render(request,"editar_articulo.html",{"miform":miform, "articulo":art})


