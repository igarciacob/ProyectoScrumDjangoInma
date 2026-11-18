from django.db.models import Model
from django.test import TestCase
from .models import Sprint,Programador, Tarea
from datetime import date

# Create your tests here.
class TareaTest(TestCase):

    def setUp(self):
        # Estos objetos estarán disponibles en cada test
        self.programador = Programador.objects.create(
            nombre="Sprint 1"
        )

        self.sprint = Sprint.objects.create(
            fecha_inicio=date(2026, 11, 9)
        )

    def test_num_sprints(self):
        sprint = Sprint.objects.count()
        self.assertCountEqual(sprint, 1)
    def test_suma(self): #tiene que e
        resultado = 2 + 3

        self.assertEqual(resultado, 5)

    def test_resta(self):
        resultado = 3 - 3
        self.assertEqual(resultado, 0)

    def test_comparacion(self):
        nombre1 = "Francisco"
        nombre2= "Francisco"
        if nombre1 != nombre2:
            comprobacion = False
        self.assertTrue(comprobacion)

    def test_crear_tarea_api(self):
        datos = {
            "nombre": "Desarrollar el login",
            "fecha_inicio": "2026-10-28",
            "fecha_fin": None,
            "completa": False,
            "sprint_id": self.sprint.id,
            "programador_id": self.programador.id,
            "etiquetas": ["Backend", "SQL"]
        }

        respuesta = self.client.post(
            "/api/creartarea/",
            data=datos,
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Tarea.objects.count(), 1)