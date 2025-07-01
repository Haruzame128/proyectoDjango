from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Familiar, Curso

from .forms import CursoForm

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def saludo(request):
    return HttpResponse("¡Hola, mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crearFamiliar(request, nombre):
    if nombre is not None:
        nuevo_familiar = Familiar(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01", parentesco="Primo")
        nuevo_familiar.save()
        return render(request, 'mi_primer_app/crear-familiar.html', {'nombre': nombre})
    
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = CursoForm()
        return render(request, 'mi_primer_app/crear-curso.html', {'form': form})