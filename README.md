#  Mi Primera Página – Leiva Cecchi

Repositorio del proyecto final de la cursada de Python/Django, donde construí una web básica de películas. Este sitio permite a los usuarios registrarse, iniciar sesión, ver un catálogo de películas y buscar por nombre.

---

## Estructura del projecto:
```bash
MiPrimeraPaginaLeivaCecchi/
│
├── media/                         # Imágenes subidas por el admin (posters)
│
├── peliculas_app/                # App principal del proyecto
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   └── peliculas_app/        # Plantillas específicas de la app
│   │       ├── buscar.html
│   │       ├── detalle_pelicula.html
│   │       ├── index.html
│   │       ├── login.html
│   │       └── registro.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── padre.html                # Plantilla base para herencia
│
├── TuPrimeraPaginaLeivaCecchi/  # Configuración del proyecto
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/                         # Entorno virtual (no se incluye en el repo)
│
├── .gitignore                    # Archivos/Carpetas ignoradas por git
├── db.sqlite3                    # Base de datos local (opcional en el repo)
├── manage.py                     # Script principal para comandos Django
├── peliculas.csv                 # Archivo CSV de carga de películas (ver más abajo)
├── requirements.txt             # Dependencias necesarias
└── README.md                     # Documentación del proyecto
```


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
### 2. Crear y activar un entorno virtual (opcional pero recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
### 3. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```
### 4. Aplicar las migraciones
```bash
python manage.py migrate
```
### 5. Crear un superusuario para acceder al panel de administración
```bash
python manage.py createsuperuser
```
### 6. Ejecutar el servidor local
```bash
python manage.py runserver
```
### 7. Acceder al sitio
Sitio web: http://127.0.0.1:8000
Panel de administración: http://127.0.0.1:8000/admin

---

## Notas adicionales

- El archivo `peliculas.csv` está incluido para facilitar la carga masiva de películas desde el panel de administración.
- La carpeta `media/` también fue incluida para que se vean correctamente los posters ya cargados al clonar y ejecutar el proyecto.

