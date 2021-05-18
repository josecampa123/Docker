from django.db import models
from django.urls import reverse

class Cv(models.Model):
    nombre = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    apellido = models.CharField(max_length=200)
    fechaNaciemnto = models.DateField()
    telefono = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    formacion = models.TextField()
    experiencia = models.TextField()

    def __str__(self):
        return self.nombre.username

    def get_absolute_url(self):
        return reverse("detalleCv", args=[self.id])