from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio , name ="Inicio"),   

    path('alta_usuarios', views.alta_usuarios, name="AgregarUsuario"),
    path('alta_articulos',views.alta_articulos, name="AgregarArticulo"),
    path('alta_vendedores',views.alta_vendedores, name="AgregarVendedor"),

    path('usuarios', views.usuarios, name="usuarios"),
    path('articulos', views.articulos, name="articulos"), 
    path('vendedores', views.vendedores, name="vendedores"), 

    path('buscar',views.buscar, name="buscar"),
    path('busqueda',views.busqueda),
    path('buscar_articulo',views.buscar_articulo),
    path('busqueda_articulo',views.busqueda_articulo),   
    path('buscar_vendedor',views.buscar_vendedor),
    path('busqueda_vendedor',views.busqueda_vendedor),

    path('eliminar_articulo/<int:id>', views.eliminar_articulo, name="EliminarArticulo"),
    path('eliminar_vendedor/<int:id>', views.eliminar_vendedor, name="EliminarVendedor"),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name="EliminarUsuario"),

    path('editar_articulo/<int:id>', views.editar_articulo, name="EditarArticulo"),
    path('editar_articulo/', views.editar_articulo, name="EditarArticulo"),
    path('editar_vendedor/<int:id>', views.editar_vendedor, name="EditarVendedor"),
    path('editar_vendedor/', views.editar_vendedor, name="EditarVendedor"),
    path('editar_usuario/<int:id>', views.editar_usuario, name="EditarUsuario"),
    path('editar_usuario/', views.editar_usuario, name="EditarUsuario"),
    path('login/' , include("login.urls"))

]