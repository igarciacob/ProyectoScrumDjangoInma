from django.urls import path
from . import views

urlpatterns =[
    path('bienvenida/', views.bienvenida,name='bienvenida'),
    path('listartareas/', views.listar_tareas, name='tareas'),
    path('listartarea/<int:id>/',views.listar_tarea, name='tarea'),
    path('listartareamejorado/<int:id>/', views.listar_tarea_mejorado, name='listarTareaMejorado'),
    path('listartareascompletadas',views.listas_tareas_completadas, name='listasTareasCompletadas'),
    path('creartarea',views.crear_tarea, name='crearTarea'),
    path('crearprogramador',views.crear_programador, name='crearProgramador'),
]