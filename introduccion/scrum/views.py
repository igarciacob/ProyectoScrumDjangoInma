from json import JSONDecodeError
from typing import List
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt

from scrum.models import Tarea, Programador, Sprint, Etiqueta


# Create your views here.
def bienvenida (request):
    return HttpResponse("Bienvenido a mi aplicación Django")

def listar_tareas(request):
    if request.method != "GET":
        return JsonResponse({"error":"Esta petición solo funciona con get"},status=405)

    tareas = Tarea.objects.all().values()
    return JsonResponse(list(tareas), safe=False)

def listar_tarea(request, id):
     if request.method != "GET":
         return JsonResponse(
             {"error":"Esta petición solo funciona con get"},
         status = 405
         )
     tarea = Tarea.objects.get(id=id)
     datos = {
         'nombre': tarea.nombre,
         'fecha_inicio': tarea.fecha_inicio,
         'fecha_fin': tarea.fecha_fin,
         'completado': tarea.completado,
         'programador': tarea.programador_id,
     }
     return JsonResponse(datos,safe=False)

def listar_tarea_mejorado(request,id):
     if request.method != "GET":
         return JsonResponse(
             {"error":"esta petición solo funciona con get"}, status=405
         )
     tarea = Tarea.objects.filter(id=id).values().first()
     if tarea is None:
         return JsonResponse(
             {"error": "Tarea no encontrada"}, status=404
         )
     return JsonResponse(tarea)

def listas_tareas_completadas(request):
     if request.method != "GET":
         return JsonResponse(
             {"error" : "esta petición solo funciona con get"},
         status=405)
     tareas = Tarea.objects.filter(completado=True).values()

     return JsonResponse(list(tareas), safe=False)

@csrf_exempt
def crear_tarea(request):

     if (request.method != 'POST'):
         return JsonResponse({"error": "Tipo de petición no es correcta"}, status=405)

     try:
         tarea_json =json.loads(request.body)
     except JSONDecodeError as e:
         return JsonResponse({"error": 'El JSON no está bien formado'}, status=400)


     msgError = validacion(tarea_json.get('sprint_id'),tarea_json.get('programador_id'))
     if msgError != '':
         return JsonResponse({'error': msgError}, status=400)


     tarea =Tarea.objects.create(
         nombre=tarea_json.get('nombre'),#.get para que no falle si no viene el dato
         fecha_inicio=tarea_json.get('fecha_inicio'),
         fecha_fin=tarea_json.get('fecha_fin'),
         completado=tarea_json.get('completado',False),
         sprint_id=tarea_json.get('sprint_id'),
         programador_id=tarea_json.get('programador_id')
     )
     tarea.save()
     # si en la tarea vienen etiquetas qu no existen hay que crearlas
     labels = tarea_json.get('etiqueta', [])
     for label in labels:
         # if not Etiqueta.objects.filter(nombre=label.nombre).exists():
         etiqueta_model,creada = Etiqueta.objects.get_or_create(nombre=label)
         tarea.etiqueta.add(etiqueta_model)
         if not creada:
             print("se ha creado la etiqueta")
         else:
             print("Etiqueta nueva")
     return JsonResponse({
        "exito": "Tarea creada correctamente",
        "id": tarea.id
    },
    status=201)

def validacion (sprint_id,prog_id):
    descrError=''

    if sprint_id is not None and not Sprint.objects.filter(id=sprint_id).exists():
        descrError ='El sprint indicado no existe\n'
    if prog_id is not None and not Programador.objects.filter(id=prog_id).exists():
        descrError +='El programador indicado no existe'
    return descrError
@csrf_exempt
def crear_programador(request):
    if (request.method != 'POST'):
        return JsonResponse({"error": "Tipo de petición no es correcta"}, status=405)
    try:
        prog_json =json.loads(request.body)
    except JSONDecodeError as e:
        return JsonResponse({"error": 'El JSON no está bien formado'}, status=400)
    prog =Programador.objects.create(
         nombre=prog_json.get('nombre'),#.get para que no falle si no viene el dato
         apellido1=prog_json.get('apellido1')
    )
    prog.save()
    labels = prog_json.get('etiqueta', [])
    crear_etiquetas(labels,prog)
    return JsonResponse({
        "exito": "Programador creado correctamente",
        "id": prog.id
    },
        status=201)
def crear_etiquetas(etiquetas,objeto):

    for etiqueta in etiquetas:
        etiqueta_model,creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
        objeto.etiqueta.add(etiqueta_model)
    if not creada:
        print("se ha creado la etiqueta")
    else:
        print("Etiqueta nueva")


