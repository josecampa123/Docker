from django.urls import path
from .views import(
    CvListView,
    DetalleDetailView, 
    cvCreateView, 
    EditarCvUpdateView,
    EliminarCvDeleteView,
    EventoListeView,
    DetalleEveView,
    ClientesListeView,
    DetalleClienteView,  
) 
 


urlpatterns = [
    path('objeto/<int:pk>/eliminar', EliminarCvDeleteView.as_view(), name='eliminarCv'),
    path('objeto/<int:pk>/editar', EditarCvUpdateView.as_view(), name='editarCv'),
    path('objeto/Nuevo', cvCreateView.as_view(), name="cvNuevo"),
    path('objeto/<int:pk>/', DetalleDetailView.as_view(), name='detalleCv'),
    path('cliente/<int:pk>/', DetalleClienteView.as_view(), name='detalleCliente'),
    path('eve/<int:pk>/', DetalleEveView.as_view(), name='detalleEvento'),
    path('', CvListView.as_view(), name='principal'),
    path('eve', EventoListeView.as_view(), name='evento'),
    path('cliente', ClientesListeView.as_view(), name='cliente'),
]