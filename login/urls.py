from django.urls import path
from . import views


urlpatterns = [
   #path('',views.inicio , name ="Inicio"),
   
   path('' , views.login_request )
      

]
