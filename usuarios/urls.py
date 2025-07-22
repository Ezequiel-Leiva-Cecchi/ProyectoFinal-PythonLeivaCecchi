from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    
    path("login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
    
    path("perfil/", views.ver_perfil, name="perfil"),
    
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]
