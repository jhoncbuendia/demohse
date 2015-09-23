from django.shortcuts import render

# Create your views here.

def perfiles(request):
	return render(request, 'vistasdemo/perfiles.html')

def contratista(request):
	return render(request, 'vistasdemo/contratista.html')	


def actividades(request):
	return render(request, 'vistasdemo/actividades.html')


def documentosrequeridos(request):
	return render(request, 'vistasdemo/documentosrequeridos.html')	

def cuadrilla(request):
	return render(request, 'vistasdemo/cuadrilla.html')	

def areas(request):
	return render(request, 'vistasdemo/areas.html')	


def permisostrabajo(request):
	return render(request, 'vistasdemo/permisostrabajo.html')	


def contratante(request):
	return render(request, 'vistasdemo/contratante.html')	