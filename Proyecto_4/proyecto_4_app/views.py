from django.shortcuts import render
from proyecto_4_app.models import Empleados

# Create your views here.

def traeEmpleados(request):
    emple = Empleados.objects.all()
    data = {'emplea': emple}
    return render(request, 'empleados.html', data)