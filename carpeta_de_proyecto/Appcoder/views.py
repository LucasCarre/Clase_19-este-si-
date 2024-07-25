from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Curso
from Appcoder.forms import CursoFormulario, BuscaCursoForm

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

def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "AppCoder/index.html")

    return render(request,"AppCoder/curso_formulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "AppCoder/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "AppCoder/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "AppCoder/buscar_form_con_api.html", {"mi_formulario": mi_formulario})