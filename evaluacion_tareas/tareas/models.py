from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    prioridad = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo