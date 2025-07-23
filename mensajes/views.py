from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_envio')
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})

class MensajeDetalleView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mensajes/detalle_mensaje.html'
    context_object_name = 'mensaje'

    def get_queryset(self):
        return Mensaje.objects.filter(receptor=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.leido:
            obj.leido = True
            obj.save()
        return obj
