from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import PerfilForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("index")
    else:
        form = RegistroForm()
    return render(request, "usuarios_app/registro.html", {"form": form})


@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    return render(request, "usuarios_app/perfil.html", {"perfil": perfil})


@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, "usuarios_app/editar_perfil.html", {"form": form})
