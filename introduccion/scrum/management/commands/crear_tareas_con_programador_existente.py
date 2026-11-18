from django.core.management import BaseCommand
from ...models import Tarea
from scrum.models import Tarea,Etiqueta, Programador


class Command(BaseCommand):

    def handle(self, *args, **options):
        programador = Programador.objects.get(id=1)
        tarea = Tarea(nombre="Tarea con programador existente",programador=programador)
        tarea.save()
        self.stdout.write(self.style.SUCCESS("Tarea con programador existente creada correctamente"))