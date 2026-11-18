from django.db import models

# Create your models here.
class Bloque(models.Model):
    nombre = models.CharField('Nombre', max_length=48)
