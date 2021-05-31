from django.urls import path
from .views import(
    #DATOS CARRUCEÑ
    CvListView,
    DetalleDetailView, 
    cvCreateView, 
    EditarCvUpdateView,
    EliminarCvDeleteView,
    # DATOS EVENTO
    EventoListeView,
    DetalleEveView,
    NuevoEventoCreateView,
    EditarEventoUpdateView,
    EliminarEventoDeleteView,

    # DATOS CLIENTES
    ClientesListeView,
    DetalleClienteView,  
    NuevoCreateView,
    EditarClienteUpdateView,
    EliminarClienteDeleteView,
   
) 
 


urlpatterns = [
    path('objeto/<int:pk>/eliminar', EliminarCvDeleteView.as_view(), name='eliminarCv'),
    path('eve/<int:pk>/eliminar', EliminarEventoDeleteView.as_view(), name='eliminarEvento'),
    path('cliente/<int:pk>/eliminar', EliminarClienteDeleteView.as_view(), name='eliminarCliente'),

    path('objeto/<int:pk>/editar', EditarCvUpdateView.as_view(), name='editarCv'),
    path('eve/<int:pk>/editar', EditarEventoUpdateView.as_view(), name='editarEvento'),
    path('cliente/<int:pk>/editar', EditarClienteUpdateView.as_view(), name='editarCliente'),
    
    path('objeto/Nuevo', cvCreateView.as_view(), name="cvNuevo"),
    path('eve/Nuevo', NuevoEventoCreateView.as_view(), name="eventoNuevo"),
    path('cliente/Nuevo', NuevoCreateView.as_view(), name="clienteNuevo"),

    path('objeto/<int:pk>/', DetalleDetailView.as_view(), name='detalleCv'),
    path('eve/<int:pk>/', DetalleEveView.as_view(), name='detalleEvento'),
    path('cliente/<int:pk>/', DetalleClienteView.as_view(), name='detalleCliente'),

    path('', CvListView.as_view(), name='principal'),
    path('eve', EventoListeView.as_view(), name='evento'),
    path('cliente', ClientesListeView.as_view(), name='cliente'),
]