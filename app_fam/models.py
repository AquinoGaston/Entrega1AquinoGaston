from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo (models.Model):

    nom_art = models.CharField (max_length= 40)
    codigo = models.CharField (max_length= 40)
    precio =  models.IntegerField ()
    stock = models.IntegerField()
    categoria = models.CharField (max_length= 40)
    id_usuario = models.IntegerField()

class Usuario (models.Model):

    nombre = models.CharField (max_length= 40)
    dni =  models.IntegerField ()
    descripcion = models.CharField (max_length= 40)
    id_usuario = models.IntegerField()
    
    

class Vendedor (models.Model):

    nom_vendedor= models.CharField (max_length= 40)
    cuit =  models.IntegerField ()
    direccion = models.CharField (max_length= 40)   
    emaeil = models.EmailField() 
    id_usuario = models.IntegerField()


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)


class Mensaje(models.Model):

    texto = models.CharField(max_length=200)
    remitente = models.CharField(max_length=40)
    id_destino = models.IntegerField()

class MensajeVendedor(models.Model):

    texto = models.CharField(max_length=200)
    remitente = models.CharField(max_length=40)
    id_destino = models.IntegerField()

class MensajeArticulo(models.Model):

    texto = models.CharField(max_length=200)
    remitente = models.CharField(max_length=40)
    id_destino = models.IntegerField()
    