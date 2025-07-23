from django.urls import path
from . import views
from .views import MensajeDetalleView

urlpatterns = [
    path('bandeja/', views.bandeja_entrada, name='bandeja_entrada'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('detalle/<int:pk>/', MensajeDetalleView.as_view(), name='detalle_mensaje'),
] 