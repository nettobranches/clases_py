from django.contrib import admin

# Register your models here.
from .models import Pregunta, RespuestaOriginal, RespuestaAleatoria

admin.site.register(Pregunta)
admin.site.register(RespuestaOriginal)
admin.site.register(RespuestaAleatoria)
