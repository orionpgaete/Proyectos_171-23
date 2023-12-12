# serializers.py

from rest_framework import serializers
from proyecto_8_app import models

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estudiante
        fields = '__all__'