from django import forms
from .models import *
class contacto_form(forms.Form):
	correo  = forms.EmailField(widget=forms.TextInput())
	subjetc = forms.CharField(widget=forms.TextInput())
	texto   = forms.CharField(widget=forms.Textarea())

class datos_form(forms.Form):
	
	Nombres       = forms.CharField(widget=forms.TextInput())
	Edad 	      = forms.IntegerField(widget=forms.NumberInput())
	Fecha_Nac     = forms.SplitDateTimeField(widget=forms.SelectDateWidget())
	Celular       = forms.IntegerField(max_value=10, widget=forms.TextInput())
	Forever_alone = forms.BooleanField()
	#Sexo  = MultipleChoiceField(choices=tupla)
	Usuario       = forms.CharField(widget=forms.TextInput())
	Contraseña    = forms.CharField(widget=forms.PasswordInput())
	Correo        = forms.EmailField(widget=forms.EmailInput())
	
class agregar_producto_form(forms.ModelForm):
	class Meta:
		model  = Producto
		fields = '__all__'

class agregar_marca_form(forms.ModelForm):
	class Meta:
		model  = Marca
		fields = '__all__'