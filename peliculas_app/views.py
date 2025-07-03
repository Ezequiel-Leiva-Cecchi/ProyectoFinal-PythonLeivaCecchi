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
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'peliculas/registro.html', {'form': form})


def index(request):
    return render(request, 'peliculas/index.html')


def buscar_pelicula(request):
    resultados = []
    form = BusquedaForm(request.GET or None)
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        resultados = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, 'peliculas/buscar.html', {'form': form, 'resultados': resultados})
