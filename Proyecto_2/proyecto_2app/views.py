from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'web\index.html')

def electronica(request):
    data = { "titulo": "Electronica"

    }
    return render(request, 'web/producto.html', data)

def ropa(request):
    data = {"titulo": "Ropa"

    }
    return render(request, 'web/producto.html', data)

def juguete(request):
    data = {"titulo": "Juguete"

    }
    return render(request, 'web/producto.html', data)