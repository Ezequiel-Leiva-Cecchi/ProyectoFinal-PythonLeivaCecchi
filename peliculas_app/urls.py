from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PeliculaCreateView, PeliculaUpdateView, PeliculaDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar_pelicula, name='buscar_pelicula'),
    path('pelicula/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('about/', views.about, name='about'),
    path('pelicula/nueva/', PeliculaCreateView.as_view(), name='pelicula_crear'),
    path('pelicula/<int:pk>/editar/', PeliculaUpdateView.as_view(), name='pelicula_editar'),
    path('pelicula/<int:pk>/borrar/', PeliculaDeleteView.as_view(), name='pelicula_borrar'),
]
