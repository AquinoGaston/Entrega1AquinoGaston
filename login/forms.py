<<<<<<< HEAD
<<<<<<< HEAD
=======
from cProfile import label
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
=======
from cProfile import label
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

<<<<<<< HEAD
<<<<<<< HEAD
class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'imagen_avatar'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    first_name = forms.CharField(label='Nombre')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

=======
=======
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
class UserEditForm(UserCreationForm):
    
    email = forms.EmailField( label = "Modificar")
    password1: forms.CharField(label= "Contraseña" , widget = forms.PasswordInput)
    password2: forms.CharField(label= "Repetir Contraseña" , widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}
<<<<<<< HEAD
        
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
=======
        
>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
