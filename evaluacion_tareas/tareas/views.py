from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea
from .forms import TareaForm  # ← Importar el formulario

class TareaLista(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'

class TareaDetalle(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'

class TareaCrear(CreateView):
    model = Tarea
    form_class = TareaForm  # ← Usar el formulario personalizado
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:tarea_list')

class TareaEditar(UpdateView):
    model = Tarea
    form_class = TareaForm  # ← Usar el formulario personalizado
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:tarea_list')

class TareaEliminar(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas:tarea_list')