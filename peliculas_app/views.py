from django.shortcuts import render, redirect
from .forms import BusquedaForm, RegistroForm
from .models import Pelicula
from django.contrib.auth import login


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('peliculas_app/index')
    else:
        form = RegistroForm()
    return render(request, 'peliculas_app/registro.html', {'form': form})


def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas_app/index.html', {'peliculas': peliculas})

def buscar_pelicula(request):
    resultados = []
    form = BusquedaForm(request.GET or None)
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        resultados = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, 'peliculas_app/buscar.html', {'form': form, 'resultados': resultados})
