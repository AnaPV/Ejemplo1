from django.urls import path
from .views import *

urlpatterns = [
	
    path('about/',vista_about, name = 'vista_about'),
    path('empresa/', vista_empresas, name= 'vista_empresas'),
    path('metodos/', vista_metodos, name = 'vista_metodos'),
    path('contacto/', vista_contacto, name = 'vista_contacto'),
    path('formulario/', vista_formulario, name = 'vista_formulario'),
    path('productos/', vista_lista_producto, name = 'vista_lista_producto'),
    path('marcas/', vista_lista_marca, name= 'vista_lista_marca'),
    path('categorias/', vista_lista_categoria, name= 'vista_lista_categoria'),
    path('agregar_producto/', vista_agregar_producto, name='vista_agregar_producto'),
    path('agregar_marca/', vista_agregar_marca, name='vista_agregar_marca'),  
      
    path('ver_producto/<int:id_prod>/', vista_ver_producto, name='vista_ver_producto'),
    path('ver_marca/<int:id_marc>/', vista_ver_marca, name='vista_ver_marca'),
    
    path('editar_producto/<int:id_prod>/', vista_editar_producto, name='vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto, name='vista_eliminar_producto'),
    path('administracion/', vista_administracion, name='vista_administracion'),
]
