from django.urls import path
from .views import inicio, saludo, saludo_con_template, crearFamiliar, crear_curso, buscar_cursos, cursos # type: ignore
urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta raíz que llama a la vista saludo
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crearFamiliar), # type: ignore
    path('crear-curso/', crear_curso, name='crear_curso'), # type: ignore
    path('cursos/buscar', buscar_cursos, name='buscar_cursos'), # type: ignore
    path('cursos/', cursos, name='cursos'), # type: ignore
]
