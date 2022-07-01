from django.db import models

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