from django import forms

class CursoForm(forms.Form):
    nombre  = forms.CharField(max_length=100, label='Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción del Curso')
    duracion_semanas = forms.IntegerField(min_value=1, initial=4, label='Duración en Semanas')
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de Inicio')
    activo = forms.BooleanField(required=False, label='Activo')
    