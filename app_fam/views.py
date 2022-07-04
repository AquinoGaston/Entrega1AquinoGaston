
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.template import loader    
from app_fam.models import *
from app_fam.forms  import *
from app_fam.forms import Alta_mensaje

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages

 # Create your views here. 

def inicio (request):
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "padre.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "padre.html")

def about (request):
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "about.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "about.html")

@login_required
def alta_usuarios (request):

    if request.method == "POST":

        usuario = request.user

        mi_formulario = Alta_usuario (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            usuario = Usuario(nombre = datos['nombre'], dni = datos['dni'],descripcion = datos['descripcion'],id_usuario = usuario.id)
            usuario.save()

            usuario = Usuario.objects.all()
            return render(request, "usuarios.html",{"usuario":usuario, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    
    if len(Avatar.objects.filter(user=request.user)) > 0:  
        return render(request, "alta_usuarios.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})    
    return render(request, "alta_usuarios.html")

def usuarios (request):
    
    usuarios = Usuario.objects.all()
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request,"usuarios.html", {"usuario": usuarios, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request,"usuarios.html", {"usuario": usuarios})

@login_required
def alta_articulos(request):
 
    if request.method == "POST":

        usuario = request.user

        mi_formulario = Alta_articulos (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            articulo = Articulo(nom_art = datos['nom_art'], codigo = datos['codigo'],precio = datos['precio'],stock =datos ['stock'], categoria = datos ['categoria'] , id_usuario = usuario.id )
            articulo.save()


            articulo= Articulo.objects.all()   
            if len(Avatar.objects.filter(user=request.user)) > 0:         
                return render(request, "articulos.html",{"articulo":articulo, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})    
            return render(request, "articulos.html",{"articulo":articulo})
 
    if len(Avatar.objects.filter(user=request.user)) > 0:  
        return render(request, "alta_articulos.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})    
    return render(request, "alta_articulos.html")

def articulos (request):

    articulo= Articulo.objects.all()
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "articulos.html", {"articulo": articulo, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "articulos.html", {"articulo": articulo})

@login_required
def alta_vendedores(request):

    if request.method == "POST":

        usuario = request.user

        mi_formulario = Alta_vendedor (request.POST)

        if mi_formulario.is_valid():

            datos =  mi_formulario.cleaned_data
            vendedor =  Vendedor(nom_vendedor = datos['nom_vendedor'], cuit = datos['cuit'],direccion = datos['direccion'], emaeil =datos ['emaeil'],id_usuario = usuario.id)
            vendedor.save()

            vendedor= Vendedor.objects.all()
            if len(Avatar.objects.filter(user=request.user)) > 0:  
                return render(request, "vendedores.html", {"vendedor":vendedor,  "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
            return render(request, "vendedores.html", {"vendedor":vendedor})
    if len(Avatar.objects.filter(user=request.user)) > 0:  
        return render(request, "alta_vendedores.html", { "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url}) 
    return render(request, "alta_vendedores.html")
def vendedores (request):

    vendedor= Vendedor.objects.all()
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "vendedores.html", {"vendedor": vendedor, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "vendedores.html", {"vendedor": vendedor})

def buscar (request):
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "buscar.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "buscar.html")

def busqueda (request):

    if request.POST['nombre']:

        nombre = request.POST['nombre']

        dato = Usuario.objects.filter(nombre__icontains = nombre)
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request, "resultado_busqueda.html",{"datos":dato, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "resultado_busqueda.html",{"datos":dato})
    else:

        return HttpResponse("Campo vacio") 


def buscar_articulo (request):
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "buscar_articulo.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "buscar_articulo.html")

def busqueda_articulo (request):

    if request.POST['nom_art']:

        nom_art = request.POST['nom_art']

        dato = Articulo.objects.filter(nom_art__icontains = nom_art)
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request, "articulo_busqueda.html",{"datos":dato, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "articulo_busqueda.html",{"datos":dato})
    else:
        return HttpResponse("Campo vacio") 


def buscar_vendedor (request):
    if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "buscar_vendedor.html", {"image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
    return render(request, "buscar_vendedor.html")

def busqueda_vendedor(request):

    if request.POST['nom_vendedor']:

        nom_vendedor = request.POST['nom_vendedor']

        dato = Vendedor.objects.filter(nom_vendedor__icontains = nom_vendedor)
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request, "vendedor_busqueda.html",{"datos":dato, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "vendedor_busqueda.html",{"datos":dato})
    else:
        return HttpResponse("Campo vacio")         

@login_required
def eliminar_articulo(request, id):
    
    usuario = request.user
    arts = Articulo.objects.get(id=id)
    
    if usuario.id == arts.id_usuario:
        arts.delete()

        arts = Articulo.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"articulos.html", {"articulo":arts, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"articulos.html", {"articulo":arts})
    else:
        messages.success(request, "Alerta, no posee permisos sobre este articulo")
        arts = Articulo.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"articulos.html", {"articulo":arts, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"articulos.html", {"articulo":arts})
       
   
@login_required
def eliminar_usuario(request, id):
    
    usuario = request.user
    us = Usuario.objects.get(id=id)

    if usuario.id == us.id_usuario:
        us.delete()

        us = Usuario.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"usuarios.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"usuarios.html", {"usuario":us})
    else:

        messages.success(request, "Alerta, no posee permisos sobre este articulo")
        us = Usuario.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"usuarios.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"usuarios.html", {"usuario":us})


@login_required
def eliminar_vendedor(request, id):
    
    usuario = request.user
    ven = Vendedor.objects.get(id=id)
    
    if usuario.id == ven.id_usuario:

        ven.delete()

        ven = Vendedor.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"vendedores.html", {"vendedor":ven, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"vendedores.html", {"vendedor":ven})
    else:

        messages.success(request, "Alerta, no posee permisos sobre este articulo")
        ven = Vendedor.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"vendedores.html", {"vendedor":ven, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"vendedores.html", {"vendedor":ven})


@login_required
def editar_vendedor(request, id):

    usuario = request.user

    vend = Vendedor.objects.get(id=id)
    
    if usuario.id == vend.id_usuario: 

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
                if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
                    return render (request, "vendedores.html", {"vendedor":vend, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
                return render (request, "vendedores.html", {"vendedor":vend})
        else:
            miform = Alta_vendedor(initial={"nom_vendedor":vend.nom_vendedor, "direccion":vend.direccion,"cuit":vend.cuit,"emaeil":vend.emaeil})
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"editar_vendedor.html",{"miform":miform, "vendedor":vend, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"editar_vendedor.html",{"miform":miform})
    else:

        messages.success(request, "Alerta, no posee permisos sobre este articulo")
        ven = Vendedor.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"vendedores.html", {"vendedor":ven, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"vendedores.html", {"vendedor":ven})


@login_required
def editar_usuario(request, id):

    usuario = request.user

    us = Usuario.objects.get(id=id)
    
    if usuario.id == us.id_usuario:

        if request.method=="POST":
            miform = Alta_usuario(request.POST)
            if miform.is_valid():
                datos = miform.cleaned_data
                us.nombre = datos["nombre"]
                us.dni = datos["dni"]
                us.descripcion = datos["descripcion"]
                us.save()

                us = Usuario.objects.all()
                if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
                    return render (request, "usuarios.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
                return render (request, "usuarios.html", {"usuario":us})
        else:
            miform = Alta_usuario(initial={"nombre":us.nombre, "dni":us.dni,"descripcion":us.descripcion})

        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"editar_usuario.html",{"miform":miform, "usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"editar_usuario.html",{"miform":miform})
    else:

        messages.success(request, "Alerta, no posee permisos sobre este articulo")
        us = Usuario.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"usuarios.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"usuarios.html", {"usuario":us})

@login_required
def editar_articulo(request, id):
    
    usuario = request.user

    art = Articulo.objects.get(id=id)
    
    if usuario.id == art.id_usuario:

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
                if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
                    return render (request, "articulos.html", {"articulo":art, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
                return render (request, "articulos.html", {"articulo":art})
        else:
            miform = Alta_articulos(initial={"nom_art":art.nom_art, "codigo":art.codigo,"precio":art.precio,"stock":art.stock,"categoria":art.categoria})
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"editar_articulo.html",{"miform":miform, "articulo":art, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"editar_articulo.html",{"miform":miform})
    else:

        messages.success(request, "Alerta, no posee permisos sobre este articulo")
        arts = Articulo.objects.all()
        if request.user.is_authenticated and len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"articulos.html", {"articulo":arts, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"articulos.html", {"articulo":arts})

@login_required()
def perfil(request):

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
        return render(request, 'perfil.html', {"image_url": imagen})

    return render (request, 'perfil.html')

@login_required()
def cargar_avatar(request):   
    
    if request.method == "POST":

        form = AvatarForm(request.POST,request.FILES)

        if form.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = form.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=form.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("Perfil")
    else:
        form = AvatarForm()
        if len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request, "cargar_avatar.html", {"form": form, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "cargar_avatar.html", {"form": form})


#USUARIOS
@login_required
def comentar ( request, id ):

    usuario = request.user

    us = Usuario.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Alta_mensaje(request.POST)

        if mi_formulario.is_valid():
                        
            datos =  mi_formulario.cleaned_data
            mensaje = Mensaje( texto = datos['texto'], remitente = usuario.username, id_destino = us.id)
            mensaje.save()

            messages.success(request, "El mensaje se envio correctamente") 

            us = Usuario.objects.all()    
            if len(Avatar.objects.filter(user=request.user)) > 0:                 
                return render(request, "usuarios.html",{"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
            return render(request, "usuarios.html",{"usuario":us})
    if len(Avatar.objects.filter(user=request.user)) > 0:  
        return render(request, "mensajes.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})  
    return render(request, "mensajes.html", {"usuario":us})


def mensajes( request, id ):

    usuario = request.user
    us = Usuario.objects.get(id=id)

    if usuario.id == us.id_usuario:

        us = Usuario.objects.get(id=id)
        mensaje = Mensaje.objects.filter(id_destino=id)
        if len(Avatar.objects.filter(user=request.user)) > 0:  
            return render(request, "comentarios.html",{"mensaje":mensaje , "usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "comentarios.html",{"mensaje":mensaje , "usuario":us})
    else:

        messages.success(request, "Alerta, no posee permisos para ver los mensajes")
        us = Usuario.objects.all() 
        if len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"usuarios.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"usuarios.html", {"usuario":us})
#VENDEDORES

@login_required
def comentar_vendedor ( request, id ):

    usuario = request.user
  
    us = Vendedor.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Alta_mensaje(request.POST)

        if mi_formulario.is_valid():
                        
            datos =  mi_formulario.cleaned_data
            mensaje = MensajeVendedor( texto = datos['texto'], remitente = usuario.username, id_destino = us.id)
            mensaje.save()
            
            messages.success(request, "El mensaje se envio correctamente") 

            vend = Vendedor.objects.all()  
            if len(Avatar.objects.filter(user=request.user)) > 0:                 
                return render(request, "vendedores.html",{"vendedor":vend, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
            return render(request, "vendedores.html",{"vendedor":vend})
  
    if len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "mensajesVendedor.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})  
    return render(request, "mensajesVendedor.html", {"usuario":us})

def mensajes_vendedor( request, id ):

    usuario = request.user
    vend = Vendedor.objects.get(id=id)

    if usuario.id == vend.id_usuario:

        us = Vendedor.objects.get(id=id)
        mensaje = MensajeVendedor.objects.filter(id_destino=id)
    
        if len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request, "comentariosVendedor.html",{"mensaje":mensaje , "usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "comentariosVendedor.html",{"mensaje":mensaje , "usuario":us})

    else:

        messages.success(request, "Alerta, no posee permisos para ver los mensajes")
        vend = Vendedor.objects.all() 
        if len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"vendedores.html", {"vendedor":vend, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"vendedores.html", {"vendedor":vend})


#ARTICULOS
@login_required
def comentar_articulos ( request, id ):

    usuario = request.user

    us = Articulo.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Alta_mensaje(request.POST)

        if mi_formulario.is_valid():
                        
            datos =  mi_formulario.cleaned_data
            mensaje = MensajeArticulo( texto = datos['texto'], remitente = usuario.username, id_destino = us.id)
            mensaje.save()

            messages.success(request, "El mensaje se envio correctamente") 

            art = Articulo.objects.all()                   
            if len(Avatar.objects.filter(user=request.user)) > 0:
                return render(request, "articulos.html",{"articulo":art, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
            return render(request, "articulos.html",{"articulo":art})

    if len(Avatar.objects.filter(user=request.user)) > 0:
        return render(request, "mensajesArticulo.html", {"usuario":us, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})  
    return render(request, "mensajesArticulo.html", {"usuario":us})


def mensajes_articulos( request, id ):

    usuario = request.user
    art = Articulo.objects.get(id=id)

    if usuario.id == art.id_usuario:

        art = Articulo.objects.get(id=id)
        mensaje = MensajeArticulo.objects.filter(id_destino=id)
        if len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request, "comentariosVendedor.html",{"mensaje":mensaje , "articulo":art, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request, "comentariosVendedor.html",{"mensaje":mensaje , "articulo":art})
    else:

        messages.success(request, "Alerta, no posee permisos para ver los mensajes")
        art = Articulo.objects.all() 
        if len(Avatar.objects.filter(user=request.user)) > 0:
            return render(request,"articulos.html", {"articulo":art, "image_url": Avatar.objects.filter(user=request.user)[0].imagen.url})
        return render(request,"articulos.html", {"articulo":art})




    