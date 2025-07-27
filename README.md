# 🎬 Mi Primera Página – Leiva Cecchi

**Proyecto Final de Python/Django - Plataforma de Películas**

Una aplicación web completa desarrollada con Django que permite a los usuarios explorar, buscar y gestionar un catálogo de películas. Incluye sistema de usuarios, mensajería interna, y un panel de administración completo.

![Django](https://img.shields.io/badge/Django-5.2.3-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Funcionalidades](#-funcionalidades)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [API y Endpoints](#-api-y-endpoints)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## ✨ Características

### 🎯 Funcionalidades Principales
- **Sistema de Usuarios Completo**: Registro, login, logout y gestión de perfiles
- **Catálogo de Películas**: Visualización de películas con detalles completos
- **Sistema de Búsqueda**: Búsqueda avanzada por título de película
- **Sistema de Mensajería**: Chat interno entre usuarios registrados
- **Panel de Administración**: Gestión completa de películas, usuarios y mensajes
- **Gestión de Archivos**: Subida y gestión de posters de películas y avatares
- **Diseño Responsivo**: Interfaz adaptada para dispositivos móviles y desktop

### 🎨 Características de Diseño
- **Interfaz Moderna**: Diseño limpio y profesional con Bootstrap 5
- **Navegación Intuitiva**: Menú de navegación fácil de usar
- **Formularios Estilizados**: Formularios con validación y diseño atractivo
- **Tarjetas de Películas**: Presentación visual atractiva del catálogo
- **Sistema de Mensajes**: Interfaz de chat moderna y funcional

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.10**: Lenguaje principal del proyecto
- **Django 5.2.3**: Framework web principal
- **SQLite3**: Base de datos relacional
- **Pillow 11.3.0**: Procesamiento de imágenes
- **django-import-export 4.3.8**: Importación/exportación de datos

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos personalizados y responsivos
- **Bootstrap 5**: Framework CSS para diseño responsivo
- **JavaScript**: Interactividad del lado del cliente

### Herramientas de Desarrollo
- **Git**: Control de versiones
- **Virtual Environment**: Aislamiento de dependencias
- **Django Admin**: Panel de administración integrado

---

## 📁 Estructura del Proyecto

```
ProyectoFinalLeivaCecchi/
│
├── 📁 media/                          # Archivos multimedia subidos por usuarios
│   ├── 📁 avatars/                    # Imágenes de perfil de usuarios
│   └── 📁 posters/                    # Posters de películas
│
├── 📁 mensajes/                       # App de sistema de mensajería
│   ├── 📁 migrations/                 # Migraciones de base de datos
│   ├── 📁 templates/mensajes/         # Plantillas de mensajería
│   │   ├── bandeja_entrada.html
│   │   ├── detalle_mensaje.html
│   │   └── enviar_mensaje.html
│   ├── admin.py                       # Configuración del admin
│   ├── forms.py                       # Formularios de mensajería
│   ├── models.py                      # Modelo de Mensaje
│   ├── urls.py                        # URLs de mensajería
│   └── views.py                       # Vistas de mensajería
│
├── 📁 peliculas_app/                  # App principal de películas
│   ├── 📁 migrations/                 # Migraciones de base de datos
│   ├── 📁 templates/peliculas_app/    # Plantillas de películas
│   │   ├── about.html                 # Página Acerca de
│   │   ├── buscar.html                # Página de búsqueda
│   │   ├── detalle_pelicula.html      # Detalle de película
│   │   ├── index.html                 # Página principal
│   │   ├── pelicula_confirm_delete.html
│   │   └── pelicula_form.html         # Formulario de película
│   ├── admin.py                       # Configuración del admin
│   ├── forms.py                       # Formularios de películas
│   ├── models.py                      # Modelos: Pelicula, Director, Genero
│   ├── urls.py                        # URLs de películas
│   └── views.py                       # Vistas de películas
│
├── 📁 static/                         # Archivos estáticos
│   ├── 📁 assets/                     # Recursos generales
│   │   ├── favicon.ico
│   │   └── 📁 img/                     # Imágenes de fondo
│   ├── 📁 css/                        # Hojas de estilo
│   │   ├── cards.css                   # Estilos para tarjetas
│   │   ├── helpers.css                 # Clases de utilidad
│   │   ├── login.css                   # Estilos de login
│   │   ├── mensajes.css                # Estilos de mensajería
│   │   └── registro.css                # Estilos de registro
│   └── 📁 js/                         # JavaScript
│       └── scripts.js                  # Scripts principales
│
├── 📁 templates/                      # Plantillas base
│   └── padre.html                     # Plantilla base principal
│
├── 📁 usuarios/                       # App de gestión de usuarios
│   ├── 📁 migrations/                 # Migraciones de base de datos
│   ├── 📁 templates/usuarios/         # Plantillas de usuarios
│   │   ├── login.html                 # Página de login
│   │   └── 📁 usuarios_app/           # Plantillas adicionales
│   │       ├── editar_perfil.html
│   │       ├── password_change.html
│   │       ├── password_change_done.html
│   │       ├── perfil.html
│   │       └── registro.html
│   ├── admin.py                       # Configuración del admin
│   ├── forms.py                       # Formularios de usuarios
│   ├── models.py                      # Modelo de Perfil
│   ├── signals.py                     # Señales de Django
│   ├── urls.py                        # URLs de usuarios
│   └── views.py                       # Vistas de usuarios
│
├── 📁 TuPrimeraPaginaLeivaCecchi/    # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py                        # Configuración ASGI
│   ├── settings.py                    # Configuración principal
│   ├── urls.py                        # URLs principales
│   └── wsgi.py                        # Configuración WSGI
│
├── 📁 venv/                           # Entorno virtual (no incluido en repo)
├── 📄 .gitignore                      # Archivos ignorados por Git
├── 📄 db.sqlite3                      # Base de datos SQLite
├── 📄 manage.py                       # Script de gestión Django
├── 📄 peliculas.csv                   # Datos de películas precargados
├── 📄 generos.csv                     # Datos de géneros precargados
├── 📄 directores.csv                  # Datos de directores precargados
├── 📄 requirements.txt                # Dependencias del proyecto
└── 📄 README.md                       # Este archivo
```

---

## 🚀 Instalación

### Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Pasos de Instalación

#### 1. Clonar el Repositorio
```bash
git clone https://github.com/Ezequiel-Leiva-Cecchi/MiPrimeraPaginaLeivaCecchi.git
cd MiPrimeraPaginaLeivaCecchi
```

#### 2. Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

#### 4. Configurar Base de Datos
```bash
# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser
```

#### 5. Cargar Datos Iniciales (Opcional)
```bash
# Los archivos CSV están incluidos para facilitar las pruebas
# Puedes importarlos desde el panel de administración
```

#### 6. Ejecutar el Servidor
```bash
python manage.py runserver
```

#### 7. Acceder a la Aplicación
- **Sitio Web**: http://127.0.0.1:8000
- **Panel de Administración**: http://127.0.0.1:8000/admin

---

## 📖 Uso

### Para Usuarios Regulares

1. **Registro**: Crea una cuenta nueva en la página de registro
2. **Login**: Inicia sesión con tus credenciales
3. **Explorar**: Navega por el catálogo de películas
4. **Buscar**: Utiliza la función de búsqueda para encontrar películas específicas
5. **Mensajería**: Envía y recibe mensajes con otros usuarios
6. **Perfil**: Edita tu información personal y avatar

### Para Administradores

1. **Panel Admin**: Accede a http://127.0.0.1:8000/admin
2. **Gestión de Películas**: Añade, edita o elimina películas
3. **Gestión de Usuarios**: Administra usuarios y sus perfiles
4. **Gestión de Mensajes**: Supervisa el sistema de mensajería
5. **Importar Datos**: Utiliza los archivos CSV para cargar datos masivos

---

## 🔧 Funcionalidades Detalladas

### 🎬 Gestión de Películas
- **CRUD Completo**: Crear, leer, actualizar y eliminar películas
- **Búsqueda Avanzada**: Filtrado por título con resultados en tiempo real
- **Gestión de Imágenes**: Subida y gestión de posters de películas
- **Relaciones**: Conexión con directores y géneros
- **Validaciones**: Verificación de datos antes de guardar

### 👥 Sistema de Usuarios
- **Autenticación**: Sistema completo de login/logout
- **Registro**: Formulario de registro con validaciones
- **Perfiles**: Información personalizada de cada usuario
- **Avatares**: Subida y gestión de imágenes de perfil
- **Cambio de Contraseña**: Funcionalidad integrada de Django

### 💬 Sistema de Mensajería
- **Bandeja de Entrada**: Visualización de mensajes recibidos
- **Envío de Mensajes**: Formulario para enviar mensajes a otros usuarios
- **Estado de Lectura**: Seguimiento de mensajes leídos/no leídos
- **Historial**: Acceso a conversaciones anteriores

### 🎨 Interfaz de Usuario
- **Diseño Responsivo**: Adaptación a diferentes tamaños de pantalla
- **Navegación Intuitiva**: Menú de navegación claro y accesible
- **Formularios Estilizados**: Interfaz moderna para entrada de datos
- **Feedback Visual**: Mensajes de confirmación y error

---

## 📸 Capturas de Pantalla

### Página Principal
![Página Principal](static/assets/img/home-bg.jpg)

### Catálogo de Películas
- Vista de tarjetas con posters
- Información detallada de cada película
- Navegación intuitiva

### Sistema de Búsqueda
- Búsqueda en tiempo real
- Resultados filtrados
- Interfaz limpia y funcional

### Panel de Administración
- Gestión completa de datos
- Interfaz intuitiva de Django Admin
- Funcionalidades avanzadas de gestión

---

## 🔌 API y Endpoints

### URLs Principales
- `/` - Página principal
- `/peliculas/` - Lista de películas
- `/peliculas/<id>/` - Detalle de película
- `/buscar/` - Búsqueda de películas
- `/registro/` - Registro de usuarios
- `/login/` - Inicio de sesión
- `/perfil/` - Perfil de usuario
- `/mensajes/` - Sistema de mensajería
- `/admin/` - Panel de administración

### Modelos de Datos

#### Película
```python
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    mini_resumen = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Genero)
    imagen = models.ImageField(upload_to='posters/', blank=True, null=True)
```

#### Usuario
```python
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
```

#### Mensaje
```python
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
```

---

## 🤝 Contribución

### Cómo Contribuir

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### Estándares de Código

- Usar **PEP 8** para estilo de código Python
- Comentar funciones y clases importantes
- Mantener consistencia en el nombramiento
- Seguir las convenciones de Django

### Reportar Bugs

- Usar el sistema de **Issues** de GitHub
- Incluir pasos para reproducir el problema
- Especificar el entorno y versión de Python/Django

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**Ezequiel Leiva Cecchi**
- GitHub: [@Ezequiel-Leiva-Cecchi](https://github.com/Ezequiel-Leiva-Cecchi)
- Proyecto: Mi Primera Página - Leiva Cecchi

---

## 🙏 Agradecimientos

- **Django Community** por el excelente framework
- **Bootstrap** por los componentes de UI
- **Python Software Foundation** por el lenguaje
- **Profesores y compañeros** de la cursada de Python/Django

---

## 📞 Contacto

Si tienes alguna pregunta o sugerencia sobre el proyecto:

- 📧 Email: [Tu email aquí]
- 💬 GitHub Issues: [Crear un issue](https://github.com/Ezequiel-Leiva-Cecchi/MiPrimeraPaginaLeivaCecchi/issues)

---

**⭐ ¡No olvides darle una estrella al proyecto si te gustó!**


