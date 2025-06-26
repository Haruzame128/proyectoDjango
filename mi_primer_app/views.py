from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

def saludo(request):
    return HttpResponse("¡Hola, mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crearFamiliar(request, nombre):
    if nombre is not None:
        nuevo_familiar = Familiar(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01", parentesco="Primo")
        nuevo_familiar.save()
        return render(request, 'mi_primer_app/crear-familiar.html', {'nombre': nombre})