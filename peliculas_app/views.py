from django.shortcuts import get_object_or_404, render
from .forms import BusquedaForm
from .models import Pelicula
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, "peliculas_app/index.html", {"peliculas": peliculas})


@login_required
def buscar_pelicula(request):
    resultados = []
    form = BusquedaForm(request.GET or None)
    if form.is_valid():
        titulo = form.cleaned_data["titulo"]
        resultados = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(
        request, "peliculas_app/buscar.html", {"form": form, "resultados": resultados}
    )


@login_required
def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    return render(
        request, "peliculas_app/detalle_pelicula.html", {"pelicula": pelicula}
    )
