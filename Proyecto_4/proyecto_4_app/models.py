from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    fono = models.CharField(max_length=20)



