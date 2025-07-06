from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Director, Genero, Pelicula

@admin.register(Director)
class DirectorAdmin(ImportExportModelAdmin):
    pass

@admin.register(Genero)
class GeneroAdmin(ImportExportModelAdmin):
    pass

@admin.register(Pelicula)
class PeliculaAdmin(ImportExportModelAdmin):
    pass
