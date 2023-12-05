from django.shortcuts import render, redirect
from .models import Proyecto
from .forms import FormProyecto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listarProyectos(request):
    proyecto = Proyecto.objects.all()
    data = {'proye' : proyecto}
    return render(request, 'proyectos.html', data)

def agregaProyecto(request):
    form = FormProyecto()

    if (request.method == 'POST'):
        form = FormProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    
    data = {'form': form}
    return render(request, 'agregar.html', data)

def eliminarProyecto(request, id):
    proye = Proyecto.objects.get(id = id)
    proye.delete()
    return redirect('/proyectos')

def modificaProyecto(request, id):
    proye = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=proye)
    
    if (request.method == 'POST'):
        form = FormProyecto(request.POST, instance=proye)
        if (form.is_valid()):
            form.save()
        return index(request)
    
    data = {'form': form}
    return render(request, 'agregar.html', data)