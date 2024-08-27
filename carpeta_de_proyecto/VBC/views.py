from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Appcoder.models import Estudiante
from django.urls import reverse_lazy


class EstudianteListView(ListView):
    model = Estudiante
    context_object_name= "Estudiantes"
    template_name= "VBC/lista_estudiantes.html"

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "VBC/estudiante_borrar.html"
    success_url = reverse_lazy("ListarEstudiantes")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = "vbc/actualizar_estudiante.html"
    success_url = reverse_lazy("ListarEstudiantes")
    fields= ["nombre", "apellido"]

