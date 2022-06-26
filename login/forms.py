from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField(label = 'Email')
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña') 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2' ] 
        #Saca los mensajes de ayuda
      #  help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label = 'Email')
    first_name: forms.CharField(label= 'Nombre')
    last_name: forms.CharField(label= 'Apellido')
    password1: forms.CharField(label= 'Contraseña')
    password2: forms.CharField(label= 'Repetir Contraseña')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1','password2']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
