from django.http import HttpResponse
from django.shortcuts import render
from proyecto_3_app.models import Productos

# Create your views here.

def busqueda(request):
    return render(request, "busqueda.html")

def buscar(request):
    if request.GET["prd"]:
        producto = request.GET["prd"]
        prod = Productos.objects.filter(nombre__icontains=producto)
        return render(request, "resultado.html", {"produ":prod, "query":producto})
    else:
        mensaje="NO ha introducido nada"
    return HttpResponse(mensaje)