from django.urls import path
from .views import (
    CvListView, 
    DetalleDetailView,
    cvCreateView,
    EditarCvUpdateView,
    EliminarCvDeleteView
    

) 
urlpatterns = [
    path('objeto/<int:pk>/eliminar', EliminarCvDeleteView.as_view(), name='eliminarCv'),
    path('objeto/<int:pk>/editar', EditarCvUpdateView.as_view(), name='editarCv'),
    path('objeto/Nuevo', cvCreateView.as_view(), name="cvNuevo"),
    path('objeto/<int:pk>/', DetalleDetailView.as_view(), name='detalleCv'),
    path('', CvListView.as_view(), name='principal'),
]