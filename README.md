# Mi Primera Página – Leiva Cecchi

Repositorio del proyecto de la cursada de Python/Django, donde construí una web básica de películas con registro de usuarios, login, catálogo y búsqueda.

## Funcionalidades
-  Registro de usuarios con validación (contraseña, email, etc.)
-  Login y logout con manejo seguro 
-  Página principal (`index`) con lista de películas (título, fecha, poster, géneros, resumen)
-  Búsqueda de películas por título
-  Vista individual de película con detalles ampliados
-  Carga de posters con `ImageField` y tratamiento en backend
-  Administrador de Django para gestionar directores, géneros y películas
-  Protección de vistas importantes usando `@login_required`
---
## Software utilizado
- Python 3.13
- Django 5.2.x
- SQLite (base de datos por defecto)
- Pillow (para manejo de imágenes)
- import-export (para cargar datos vía CSV)
---
## Instalación y uso
1. **Clonar el repo**
   ```bash
   git clone https://github.com/Ezequiel-Leiva-Cecchi/MiPrimeraPaginaLeivaCecchi.git
   cd MiPrimeraPaginaLeivaCecchi
