from django.shortcuts import render

# Create your views here.

def renderweb(request):
    data = {"nombre":"Pedro"}
    return render(request, 'plantilla/pagina.html', data)

def infousuario(request):
    data = {"id": "123", "nombre": "Pedro Gaete", "email": "pedro@gmail.com"}
    return render(request, 'plantilla/userinfotemplate.html', data)
