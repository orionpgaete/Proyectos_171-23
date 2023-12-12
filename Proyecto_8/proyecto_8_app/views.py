from django.shortcuts import render
from .serializers import EstudianteSerializer
from .models import Estudiante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# FUNCTION BASED VIEWS

@api_view(['GET', 'POST'])
def estudiante_list(request):
    if request.method == 'GET':
        estude = Estudiante.objects.all()
        serial = EstudianteSerializer(estude, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = EstudianteSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def estudiante 
    