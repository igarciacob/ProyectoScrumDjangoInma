from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.nombre}"

class Sprint (models.Model):
    nombre = models.CharField(max_length=50,default="")
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.nombre}"



class Etiqueta (models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.id} {self.nombre}"

class Programador (models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    etiqueta = models.ManyToManyField(Etiqueta, blank=True)
    def __str__(self):
        return f"{self.id} {self.apellido1} {self.nombre}"

    class Meta:
        verbose_name = 'Programador'
        verbose_name_plural = 'Programadores'
class Tarea (models.Model):
    nombre = models.CharField(max_length=50)
    completado = models.BooleanField(default=False)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    sprint = models.ForeignKey(
        Sprint,
        on_delete=models.CASCADE, blank=True, null=True
    )
    programador= models.ForeignKey(
        Programador,
        on_delete=models.CASCADE,blank=True, null=True
    )
    etiqueta = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return f"{self.id} {self.nombre}"

