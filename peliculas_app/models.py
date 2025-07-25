from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


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
    imagen = models.ImageField(upload_to='posters/', blank=True, null=True)

    def clean(self):
        # Validar que el título no esté vacío
        if not self.titulo.strip():
            raise ValidationError({'titulo': 'El título no puede estar vacío.'})
        # Validar que el mini_resumen no esté vacío
        if not self.mini_resumen.strip():
            raise ValidationError({'mini_resumen': 'El resumen no puede estar vacío.'})
        # Validar que la fecha de lanzamiento no sea futura
        if self.fecha_lanzamiento > timezone.now().date():
            raise ValidationError({'fecha_lanzamiento': 'La fecha de lanzamiento no puede ser futura.'})

    def __str__(self):
        return self.titulo

