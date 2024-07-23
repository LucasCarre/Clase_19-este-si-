from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "Appcoder/pag_index.html")

def cursos(request):
    return render(request, "Appcoder/cursos.html")

def profesores(request):
    return render(request, 'Appcoder/profesores.html')

def estudiantes(request):
    return render(request, 'Appcoder/estudiantes.html')

def entregables(request):
    return render(request, 'Appcoder/entregables.html')