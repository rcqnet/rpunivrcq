from django.shortcuts import render,redirect
from .models import Curso
# Create your views here.

def home(request):
    cursoListado = Curso.objects.all()
    return render(request,'gestionCursos.html',{'cursos':cursoListado})

def registrar_curso(request):
    nombre = request.POST['txtNombre']
    credito = request.POST['numCreditos']
    
    curso = Curso.objects.create(nombre=nombre,credito=credito)
    
    return redirect('/')

def edicionCurso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    id = request.POST['intCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCreditos']
    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.credito = credito
    curso.save()
    return redirect('/')

def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    
    return redirect('/')
