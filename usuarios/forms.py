from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        # Permitir el login solo si el usuario está activo
        if not user.is_active:
            raise forms.ValidationError(
                _('Esta cuenta está inactiva.'),
                code='inactive',
            )
    
    error_messages = {
        'invalid_login': _('Usuario o contraseña incorrectos.'),
        'inactive': _('Esta cuenta está inactiva.'),
    }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', error_messages={
        'required': 'El correo electrónico es obligatorio.',
        'invalid': 'Ingrese un correo electrónico válido.'
    })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        error_messages = {
            'username': {
                'required': 'El nombre de usuario es obligatorio.',
                'unique': 'Este nombre de usuario ya está en uso.',
            },
            'password1': {
                'required': 'La contraseña es obligatoria.',
            },
            'password2': {
                'required': 'Debe confirmar la contraseña.',
            },
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
