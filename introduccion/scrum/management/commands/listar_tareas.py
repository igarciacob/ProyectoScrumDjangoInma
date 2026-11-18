from django.core.management import BaseCommand
from ...models import Tarea
from scrum.models import Tarea


class Command(BaseCommand):

    def handle(self, *args, **options):

        tarea = Tarea.objects.all()
        for tarea in tarea:
            print(f"{tarea.id} {tarea.nombre}")
        self.stdout.write(self.style.SUCCESS("ESTE COMANDO LISTA TODAS LAS TAREAS"))

