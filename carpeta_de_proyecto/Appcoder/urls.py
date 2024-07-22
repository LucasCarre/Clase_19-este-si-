from django.urls import path
from Appcoder import views

urlpatterns = [
    path('In/', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
]
