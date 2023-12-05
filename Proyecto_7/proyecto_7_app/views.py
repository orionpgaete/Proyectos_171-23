from django.http import JsonResponse
from django.shortcuts import render
from proyecto_7_app import models

# Create your views here.

def empleadosview(request):
    emp = {
        'id' : 123,
        'nombre' : 'Juan Perez',
        'email' : 'junitope@inacap.cl',
        'sueldo' : '999999'
    }
    return JsonResponse(emp)

def empleadosview_db(request):
    emple = models.Empleados.objects.all()
    data = {'empleados': list(emple.values('nombre', 'sueldo'))}
    return JsonResponse(data)
