from django.urls import path
from .views import RegistrarView#, contraseña

urlpatterns = [
   # path('nombre/', contraseña, name='contraseña'),
    path('registrar/', RegistrarView.as_view(), name='registrar'),
]