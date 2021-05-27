from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Cv, Evento, Cliente
from django.urls import reverse_lazy

class CvListView(ListView):
    model = Cv
    template_name = 'principal.html'
    context_object_name = 'jose'

class DetalleDetailView(DetailView):
    model = Cv
    template_name = "detalleCv.html"
    context_object_name = 'objeto'

class cvCreateView(CreateView):
    model = Cv
    template_name = "cvNuevo.html"
    fields = '__all__'

class EditarCvUpdateView(UpdateView):
    model = Cv
    template_name = 'editarCv.html'
    context_object_name = 'objeto'
    fields = ['nombre','apellido']

class EliminarCvDeleteView(DeleteView):
    model = Cv
    template_name = "eliminarCv.html"
    context_object_name = 'objeto'
    success_url = reverse_lazy('principal')

###############################################################################
class EventoListeView(ListView):
    model = Evento
    template_name = 'evento.html'
    context_object_name = 'eve'

class DetalleEveView(DetailView):
    model = Evento
    template_name = "detalleEvento.html"
    context_object_name = 'eve'

#####################################################################################
class ClientesListeView(ListView):
    model = Cliente
    template_name = 'cliente.html'
    context_object_name = 'cliente'

class DetalleClienteView(DetailView):
    model = Cliente
    template_name = "detalleCliente.html"
    context_object_name = 'cliente'















