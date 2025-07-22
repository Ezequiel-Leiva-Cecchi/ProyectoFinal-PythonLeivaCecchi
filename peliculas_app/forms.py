from django.forms import ModelForm
from .models import Director, Genero, Pelicula
from django import forms

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

class BusquedaForm(forms.Form):
    titulo = forms.CharField(label="Buscar película", max_length=100)
