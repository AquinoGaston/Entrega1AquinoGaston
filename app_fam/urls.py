from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio , name ="Inicio"),   

    path('alta_usuarios', views.alta_usuarios),
    path('alta_articulos',views.alta_articulos),
    path('alta_vendedores',views.alta_vendedores),
    path('usuarios', views.usuarios),
    path('articulos', views.articulos), 
    path('vendedores', views.vendedores), 

    path('buscar',views.buscar),
    path('busqueda',views.busqueda),
    path('buscar_articulo',views.buscar_articulo),
    path('busqueda_articulo',views.busqueda_articulo),   
    path('buscar_vendedor',views.buscar_vendedor),
    path('busqueda_vendedor',views.busqueda_vendedor)

]