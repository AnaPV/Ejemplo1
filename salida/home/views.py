from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def vista_about(request):
	return render(request, 'about.html')

def vista_empresas(request):
	empresas = [ "SAMSUMG","LG","HUAWEI","MOTOROLA"]
	#diccionario = {'nombre' :empresas}
	return render(request,'empresas.html', locals())

def vista_metodos(request):
	return render(request,'metodos.html')

def vista_contacto(request):
	info_ingresada = False
	email	= ""
	subjetc = ""
	texto 	= ""
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			info_ingresada = True
			email 	= formulario.cleaned_data['correo']
			subjetc = formulario.cleaned_data['subjetc']
			text 	= formulario.cleaned_data['texto']
			return render(request,'contacto.html',locals())
	else:
		formulario = contacto_form()
	return render(request,'contacto.html',locals())

def vista_formulario(request):
	info_ingresado= False
	nombres = ""
	edad = ""
	fecha_nac = ""
	celular = ""
	foreverAlone = ""
	sexo = ""
	usuario = ""
	contraseña = ""
	correo = ""
	if request.method=="POST":
		formulario1= datos_from(request.POST)
		if	formulario1.is_valid:
			info_ingresado= True
			nombres = formulario.cleaned_data['Nombres']
			edad = formulario.cleaned_data['Edad']
			fecha_nac = formulario.cleaned_data['Fecha_Nac']
			celular = formulario.cleaned_data['Celular']
			foreverAlone = formulario.cleaned_data['Forever_alone']
			sexo = formulario.cleaned_data[' Sexo']
			usuario = formulario.cleaned_data['Usuario']
			contraseña = formulario.cleaned_data['Contraseña']
			correo = formulario.cleaned_data['Correo']
			return render(request,'formulario1.html',locals())
	else:
		formulario1= datos_form()
	return render(request,'formulario1.html',locals())


def vista_lista_producto(request):
	Lista = Producto.objects.all()
	Lista = Producto.objects.order_by('id')

	return render(request, 'lista_p.html', locals())

def vista_lista_marca(request):
	Marc  = Marca.objects.all()
	Marc  = Marca.objects.order_by('nombre')

	return render(request, 'lista_m.html', locals())

def vista_lista_categoria(request):
	Cate  = Categoria.objects.all()
	Cate  = Categoria.objects.order_by('nombre')

	return render(request, 'lista_c.html', locals())

def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/productos/')

	else:
		formulario = agregar_producto_form()
	return render(request, 'agregar_producto.html', locals())

def vista_agregar_marca(request):
	if request.method == 'POST':
		formulario = agregar_marca_form(request.POST, request.FILES)
		if formulario.is_valid():
			marc = formulario.save(commit = False)
			marc.save()
			formulario.save_m2m()
			return redirect('/marcas/')
	else:
		formulario = agregar_marca_form()
	return render(request, 'agregar_marca.html', locals())

#<a href="{ url}"></a>
#url(r*'detalle/(P<prod>?/') 

def vista_ver_producto(request, id_prod):
	p = Producto.objects.get(id=id_prod)
	return render(request, 'ver_producto.html', locals())

def vista_ver_marca(request, id_marc):
	m = Marca.objects.get(id=id_marc)
	return render(request, 'ver_marca.html', locals())



def vista_administracion(request):                                           
	return render(request, 'administracion.html', locals())


def vista_editar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect('/productos/')
	else:
		formulario = agregar_producto_form(instance= prod)
	return render(request, 'agregar_producto.html', locals())

def vista_eliminar_producto(request, id_prod):
	prod = Producto.objects.get(id= id_prod)
	prod.delete()
	return redirect ('/productos/')



