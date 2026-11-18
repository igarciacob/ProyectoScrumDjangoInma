from django.core.management import BaseCommand
from ...models import Tarea
from scrum.models import Tarea,Etiqueta, Programador


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            # creacion de etiqueta
            etiqueta = Etiqueta(nombre="Etiqueta 1")
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"La etiqueta se ha creado correctamenta"))
            #creamos un programador
            programador = Programador(nombre="Inma",apellido1="Garcia")
            programador.save()
            self.stdout.write(self.style.SUCCESS(f"El programador se ha creado correctamenta"))
            # creamos de tarea
            tarea=Tarea.objects.get(nombre="Tarea para Inma",programador=programador)
            tarea.save()
            tarea.etiqueta.add(etiqueta)
            self.stdout.write(self.style.SUCCESS(f"La tarea con nmbre {tarea.nombre} se ha creado correctamenta"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"{e}"))

