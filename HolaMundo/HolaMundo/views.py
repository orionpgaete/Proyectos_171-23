import datetime
from django.http import HttpResponse


#aca agregamos las vistas que vamos a utilizar


def hola(request):
    return HttpResponse("<h1>Bienvenidos al mega curso de DJango</h1>")

def chaoo(request):
    return HttpResponse("Hasta luego...")

def saludo2(request):
    docu = """
            <html>
                <body>
                    <h1>Hola de nuevo uso de variables</h1>
                </body>
            </html>"""
    return HttpResponse(docu)

def hora(request):
    horayfecha=datetime.datetime.now()

    docu = """
            <html>
                <body>
                    <h1>La fecha y hora actual es: %s</h1>
                </body>
            </html>""" % horayfecha
    return HttpResponse(docu)

def calculo(request, anio, edad):
    #edad = 18
    periodo = anio - 2023
    edadfutura = edad + periodo
    docu = """
            <html>
                <body>
                    <h1>En el año %s tendras %s años</h1>
                </body>
            </html>""" % (anio, edadfutura)
    return HttpResponse(docu)

