from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.templatetags.static import static
from django.utils import timezone


POSTERS_CATALOGO = {
    ("jurassic park", 1993): "Jurassic_Park_1993_768_x_1152_by_John_Guydo.jpeg",
    ("salvar al soldado ryan", 1998): "salvar_al_sodadoRyan.jpeg",
    ("inception", 2010): "Inception_2010.jpeg",
    ("dunkerque", 2017): "Dunkirk.jpeg",
    ("dunkirk", 2017): "Dunkirk.jpeg",
    ("pulp fiction", 1994): "pulp_fiction.jpeg",
    ("kill bill: volumen 1", 2003): "Kill_Bill__Volume_1_by_Paul_Mann.jpeg",
    ("kill bill volumen 1", 2003): "Kill_Bill__Volume_1_by_Paul_Mann.jpeg",
    ("kill bill vol. 1", 2003): "Kill_Bill__Volume_1_by_Paul_Mann.jpeg",
    ("kill bill: vol. 1", 2003): "Kill_Bill__Volume_1_by_Paul_Mann.jpeg",
}


class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    mini_resumen = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Genero)
    imagen = models.ImageField(upload_to="posters/", blank=True, null=True)

    class Meta:
        ordering = ("-fecha_lanzamiento", "titulo")

    def clean(self):
        if not self.titulo.strip():
            raise ValidationError({"titulo": "El título no puede estar vacío."})
        if not self.mini_resumen.strip():
            raise ValidationError({"mini_resumen": "El resumen no puede estar vacío."})
        if self.fecha_lanzamiento > timezone.now().date():
            raise ValidationError(
                {"fecha_lanzamiento": "La fecha de lanzamiento no puede ser futura."}
            )

    def __str__(self):
        return self.titulo

    @property
    def anio(self):
        return self.fecha_lanzamiento.year

    @property
    def poster_url(self):
        """Prioriza archivos versionados y evita mostrar imágenes rotas."""
        if self.imagen:
            filename = Path(self.imagen.name).name
            static_poster = settings.BASE_DIR / "static" / "posters" / filename
            if static_poster.exists():
                return static(f"posters/{filename}")

            try:
                if self.imagen.storage.exists(self.imagen.name):
                    return self.imagen.url
            except (OSError, ValueError, NotImplementedError):
                pass

        # Compatibilidad con registros importados desde el CSV original,
        # donde la columna de imagen estaba vacía.
        fallback = POSTERS_CATALOGO.get((self.titulo.strip().casefold(), self.anio))
        if fallback:
            fallback_path = settings.BASE_DIR / "static" / "posters" / fallback
            if fallback_path.exists():
                return static(f"posters/{fallback}")

        return ""


class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resenas")
    pelicula = models.ForeignKey(
        Pelicula, on_delete=models.CASCADE, related_name="resenas"
    )
    puntuacion = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField(max_length=800, blank=True)
    creada = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("usuario", "pelicula"), name="resena_unica_por_usuario"
            )
        ]
        ordering = ("-actualizada",)

    def __str__(self):
        return f"{self.pelicula} · {self.puntuacion}/5"


class EnLista(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lista_cine"
    )
    pelicula = models.ForeignKey(
        Pelicula, on_delete=models.CASCADE, related_name="en_listas"
    )
    agregada = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("usuario", "pelicula"), name="pelicula_unica_en_lista"
            )
        ]
        ordering = ("-agregada",)

    def __str__(self):
        return f"{self.usuario} → {self.pelicula}"
