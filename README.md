#  Mi Primera Página – Leiva Cecchi

Repositorio del proyecto final de la cursada de Python/Django, donde construí una web básica de películas. Este sitio permite a los usuarios registrarse, iniciar sesión, ver un catálogo de películas y buscar por nombre.

---

##  Tecnologías utilizadas

-  Python 3.10
-  Django 5.0.1
-  Bootstrap 5
-  HTML5 & CSS3
-  SQLite3 (base de datos por defecto en Django)

---

##  Funcionalidades principales

-  Registro de usuarios con validación.
-  Inicio y cierre de sesión.
-  Visualización de un catálogo de películas.
-  Búsqueda de películas por nombre.
-  Panel de administración para gestión de películas y usuarios.
-  Uso de formularios personalizados con Bootstrap.
-  Organización modular usando múltiples apps Django (`peliculas`, `usuarios`).

## Instalación y ejecución local

Seguí los pasos a continuación para ejecutar el proyecto localmente en tu máquina:

### 1. Clonar el repositorio
```bash
git clone https://github.com/Ezequiel-Leiva-Cecchi/MiPrimeraPaginaLeivaCecchi.git
cd MiPrimeraPaginaLeivaCecchi
```
2. Crear y activar un entorno virtual (opcional pero recomendado)
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Instalar las dependencias del proyecto
pip install -r requirements.txt
4. Aplicar las migraciones
python manage.py migrate
5. Crear un superusuario para acceder al panel de administración (opcional)
bash

python manage.py createsuperuser
6. Ejecutar el servidor local
python manage.py runserver
7. Acceder al sitio
Sitio web: http://127.0.0.1:8000

Panel de administración: http://127.0.0.1:8000/admin

