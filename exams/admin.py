from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Pregunta)
admin.site.register(RespuestaOriginal)
admin.site.register(RespuestaAleatoria)
admin.site.register(Materia)
admin.site.register(Unidad)
admin.site.register(RespuestaOrden)
