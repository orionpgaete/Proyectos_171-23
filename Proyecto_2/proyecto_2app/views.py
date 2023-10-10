from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'web\index.html')

def electronica(request):
    data = { "titulo": "Electronica",
            "producto1": "Mouse Inalambrico",
            "producto2": "Luz Led",
            "producto3": "Tester Digital",
            "foto1": "electronica1.jpg",
            "foto2": "electronica2.jpg",
            "foto3": "electronica3.jpg"
    }
    return render(request, 'web/producto.html', data)

def ropa(request):
    data = {"titulo": "Ropa"

    }
    return render(request, 'web/producto.html', data)

def juguete(request):
    data = {"titulo": "Juguete",
            "producto1": "Juego Didactico",
            "producto2": "Autos",
            "producto3": "Muñeca Grande",
            "foto1": "juguete1.jpg",
            "foto2": "juguete2.jpg",
            "foto3": "juguete3.jpg"

    }
    return render(request, 'web/producto.html', data)