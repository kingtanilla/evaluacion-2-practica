from django.contrib import admin
from .models import Tarea

# Register your models here.

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_creacion', 'fecha_limite')
    list_filter = ('vigente', 'prioridad', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')