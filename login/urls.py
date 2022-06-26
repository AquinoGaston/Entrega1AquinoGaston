from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   #path('',views.inicio , name ="Inicio"),
   
   path('' , views.login_request, name = "Login" ),

   path('register/', views.register, name = 'Register'),
   path('editarPerfil/', views.editarPerfil, name="editarperfil"),
   path ('logout/', LogoutView.as_view(template_name = "logout.html"), name ="logout"),


]
