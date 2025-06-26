from django.urls import path
from .views import saludo, saludo_con_template, crearFamiliar

urlpatterns = [
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crearFamiliar), # type: ignore
]
