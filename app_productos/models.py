from django.db import models

# Create your models here.

class Productos(models.Model):
    
    nombre= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    Fecha_aniadido= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - ${self.descripcion}"

