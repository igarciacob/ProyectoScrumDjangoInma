from django.core.management import BaseCommand
from faker import Faker
from datetime import datetime
from ...models import Tarea ,Etiqueta, Programador, Sprint, Proyecto
#from scrum.models import Tarea,Etiqueta, Programador, Sprint, Proyecto
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker('es-ES')

        #creamos el proyecto
        proyecto = Proyecto(nombre="Proyecto 1",fecha_inicio=datetime.now())
        proyecto.save()
        self.stdout.write(self.style.SUCCESS('El proyecto: ' + proyecto.nombre + ' creado con exito'))
        #creamos los programadores
        for i in range(10):
            programador = Programador(nombre = faker.first_name(), apellido1 = faker.last_name())
            programador.save()
            #self.stdout.write(self.style.SUCCESS('El programador:  '+programador.nombre + 'creado con exito'))
        #creamos los sprint
        for i in range(4):
            project= random.choice(Proyecto.objects.all())
            sprint = Sprint(nombre=f"Sprint {i +1}", fecha_inicio=datetime.now(), proyecto=project)
            sprint.save()
        #creamos las tareas
        for i in range (30):
            sprint = random.choice(Sprint.objects.all())
            programador = random.choice(Programador.objects.all())
            tarea= Tarea (nombre= f"Tarea {i + 1}", completado=False, fecha_inicio=datetime.now(),sprint=sprint,programador=programador)
            tarea.save()