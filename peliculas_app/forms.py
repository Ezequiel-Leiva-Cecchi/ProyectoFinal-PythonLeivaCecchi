from django.forms import ModelForm
from .models import Director, Genero, Pelicula
from django import forms
from django.utils import timezone

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if not titulo:
            raise forms.ValidationError('El título no puede estar vacío.')
        return titulo

    def clean_mini_resumen(self):
        mini_resumen = self.cleaned_data.get('mini_resumen', '').strip()
        if not mini_resumen:
            raise forms.ValidationError('El resumen no puede estar vacío.')
        return mini_resumen

    def clean_fecha_lanzamiento(self):
        fecha = self.cleaned_data.get('fecha_lanzamiento')
        if fecha and fecha > timezone.now().date():
            raise forms.ValidationError('La fecha de lanzamiento no puede ser futura.')
        return fecha

class BusquedaForm(forms.Form):
    titulo = forms.CharField(label="Buscar película", max_length=100)
