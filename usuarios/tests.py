from django.test import TestCase
from django.urls import reverse


class AuthPageTests(TestCase):
    def test_login_usa_layout_unificado_de_cinevault(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="auth-page"')
        self.assertContains(response, 'class="auth-card"')
        self.assertContains(response, "Tu próxima película te está esperando.")

    def test_registro_usa_el_mismo_sistema_visual(self):
        response = self.client.get(reverse("registro"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="auth-page"')
        self.assertContains(response, 'class="auth-card"')
        self.assertContains(response, "Crear mi cuenta")
