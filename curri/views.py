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
                                 # DATOS DEL EVENTO
class EventoListeView(ListView):
    model = Evento
    template_name = 'evento.html'
    context_object_name = 'eve'

class DetalleEveView(DetailView):
    model = Evento
    template_name = "detalleEvento.html"
    context_object_name = 'eve'

class NuevoEventoCreateView(CreateView):
    model = Evento
    template_name = "eventoNuevo.html"
    fields = '__all__'

class EditarEventoUpdateView(UpdateView):
    model = Evento
    template_name = 'editarEvento.html'
    context_object_name = 'eve'
    fields = '__all__'

class EliminarEventoDeleteView(DeleteView):
    model = Evento
    template_name = "eliminarEvento.html"
    context_object_name = 'eve'
    success_url = reverse_lazy('principal')

#####################################################################################
                                 # DATOS DEL CLIENTE 
class ClientesListeView(ListView):
    model = Cliente
    template_name = 'cliente.html'
    context_object_name = 'cliente'

class DetalleClienteView(DetailView):
    model = Cliente
    template_name = "detalleCliente.html"
    context_object_name = 'cliente'

class NuevoCreateView(CreateView):
    model = Cliente
    template_name = "clienteNuevo.html"
    fields = '__all__'

class EditarClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'editarCliente.html'
    context_object_name = 'cliente'
    fields = '__all__'

class EliminarClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "eliminarCliente.html"
    context_object_name = 'cliente'
    success_url = reverse_lazy('principal')















