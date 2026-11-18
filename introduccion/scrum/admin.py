from django.contrib import admin
from .models import Tarea, Programador, Proyecto, Sprint, Etiqueta

# Register your models here.
admin.site.register(Tarea)
admin.site.register(Programador)
admin.site.register(Proyecto)
admin.site.register(Sprint)
admin.site.register(Etiqueta)
