from django.contrib import admin
from .models import Cliente, Cv, Evento

admin.site.register(Cv)
admin.site.register(Evento)
admin.site.register(Cliente)
# Register your models here.
