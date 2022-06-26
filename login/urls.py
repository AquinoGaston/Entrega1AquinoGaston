from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
<<<<<<< HEAD
=======

>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6

urlpatterns = [
   #path('',views.inicio , name ="Inicio"),
   
   path('' , views.login_request, name = "Login" ),
<<<<<<< HEAD
   path('register/', views.register, name = 'Register'),
   path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
   path ('logout/', LogoutView.as_view(template_name = "logout.html"), name ="logout"),
=======
   path ("logout", LogoutView.as_view(template_name = "logout.html"), name ="logout"),
   path ("register", views.register , name =  "Register"),
   path ("editarPerfil" , views.editarPerfil , name = "editarperfil")

>>>>>>> 6bd9fbe92cfbd1239e51d52ee83e3d369be30fa6
]
