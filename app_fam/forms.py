from django import forms

class Alta_usuario (forms.Form):

    nombre = forms.CharField (max_length= 40)
    dni =  forms.IntegerField ()
    descripcion = forms.CharField (max_length= 40)

class Alta_articulos(forms.Form):

    nom_art = forms.CharField (max_length= 40)
    codigo = forms.CharField (max_length= 40)
    precio =  forms.IntegerField ()
    stock = forms.IntegerField()
    categoria = forms.CharField (max_length= 40)    

class Alta_vendedor (forms.Form):

    nom_vendedor= forms.CharField (max_length= 40)
    cuit =  forms.IntegerField ()
    direccion = forms.CharField (max_length= 40)   
    emaeil = forms.EmailField() 