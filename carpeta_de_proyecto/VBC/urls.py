from django.urls import path
from VBC import views

urlpatterns = [
    path('estudiante/listar', views.EstudianteListView.as_view(), name='ListarEstudiantes'),
    path('estudiante/<pk>/borrar', views.EstudianteDeleteView.as_view(), name='EstudianteBorrar'),
    path('estudiante/<pk>/actualizar', views.EstudianteUpdateView.as_view(), name='EstudianteActualizar'),
]
