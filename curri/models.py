from django.db import models
#from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.conf import settings

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=200)
  
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalleEvento',args=[self.id])


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200)

    Evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE

    )
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalleCliente',args=[self.id])


class Cv(models.Model):
    nombre = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
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