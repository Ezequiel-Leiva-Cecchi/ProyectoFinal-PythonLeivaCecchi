from django.db import models


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

    def __str__(self):
        return self.titulo

