from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Perfil


class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _("Usuario o contraseña incorrectos."),
        "inactive": _("Esta cuenta está inactiva."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Tu usuario",
                "autocomplete": "username",
                "autofocus": True,
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": "Tu contraseña",
                "autocomplete": "current-password",
            }
        )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("Esta cuenta está inactiva."),
                code="inactive",
            )


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo electrónico",
        error_messages={
            "required": "El correo electrónico es obligatorio.",
            "invalid": "Ingresá un correo electrónico válido.",
        },
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        error_messages = {
            "username": {
                "required": "El nombre de usuario es obligatorio.",
                "unique": "Este nombre de usuario ya está en uso.",
            },
            "password1": {
                "required": "La contraseña es obligatoria.",
            },
            "password2": {
                "required": "Debés confirmar la contraseña.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Elegí un nombre de usuario",
                "autocomplete": "username",
                "autofocus": True,
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "tu@email.com",
                "autocomplete": "email",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "Creá una contraseña",
                "autocomplete": "new-password",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "Repetí la contraseña",
                "autocomplete": "new-password",
            }
        )


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["avatar", "biografia", "fecha_nacimiento"]
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
        }
