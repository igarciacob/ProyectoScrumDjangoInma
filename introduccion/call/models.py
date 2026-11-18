from django.db import models

# Create your models here.
class Persona (models.Model):
    nombre = models.CharField(max_length =50)
    primer_apellido =models.CharField(max_length = 100)
    segundo_apellido = models.CharField(max_length = 100)


class Jugador (models.Model):
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    rango = models.CharField(max_length = 30)
    partidas = models.IntegerField()
    victorias = models.IntegerField()
    nivel= models.IntegerField()
    puntuacion = models.FloatField()
    activo = models.BooleanField()



    def __str__(self):
        return f"{self.id}{self.nombre} {self.edad} {self.rango} {self.partidas}"