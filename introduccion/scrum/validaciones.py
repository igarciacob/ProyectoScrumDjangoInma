from .models import *
from django.http import JsonResponse
def validar_tarea(tarea_json):
    if tarea_json.sprint_id is not None and not Sprint.objects.filter(id=tarea_json.sprint_id).exists():
        return JsonResponse({'error':' El sprint indicado no existe'}, status=400)
    if tarea_json.prog_id is not None and not Programador.objects.filter(id=tarea_json.prog_id).exists():
        return JsonResponse({'error': ' El programador indicado no existe'}, status=400)

