from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    
    path("login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
    
    path("perfil/", views.ver_perfil, name="perfil"),
    
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
    path("password_change/", PasswordChangeView.as_view(template_name="usuarios_app/password_change.html"), name="password_change"),
    path("password_change/done/", PasswordChangeDoneView.as_view(template_name="usuarios_app/password_change_done.html"), name="password_change_done"),
]
