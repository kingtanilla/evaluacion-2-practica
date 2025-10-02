from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título de la tarea'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción detallada'
            }),
            'prioridad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10,
                'placeholder': 'Prioridad (1-10)'
            }),
            'vigente': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'fecha_limite': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'prioridad': 'Prioridad (1-10)',
            'vigente': '¿Está vigente?',
            'fecha_limite': 'Fecha límite'
        }
    
    def clean_prioridad(self):
        prioridad = self.cleaned_data.get('prioridad')
        if prioridad < 1 or prioridad > 10:
            raise forms.ValidationError('La prioridad debe estar entre 1 y 10')
        return prioridad