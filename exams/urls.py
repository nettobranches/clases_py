from django.urls import path

from . import views

urlpatterns = [
    # ex: /exams/
    path('', views.index, name='index'),
    # ex: /exams/5/
    path('fisica/', views.detail, name='detail'),
    # ex: /exams/5/
    path('fisica/<int:timestamp>', views.get_timestamp, name='get_timestamp'),
    # ex: /exams/5/
    path('calc/<str:unidad>/<str:respuesta>/<int:preguntas>', views.calculo, name='calculo'),

    path('resultados/original/<str:materia>/<str:unidad>', views.resultados_original, name='resultados_original'),

    path('preguntas/original/<str:materia>/<str:unidad>', views.preguntas_original, name='preguntas_original'),

    path('preguntas/generar/<str:materia>/<str:unidad>', views.preguntas_generar, name='preguntas_generar'),

    path('preguntas/ordinario/<str:materia>', views.preguntas_ordinario, name='preguntas_ordinario'),

    path('resultados/ordinario/<str:timestamp>', views.resultados_ordinario, name='resultados_ordinario'),

    path('resultados/<int:timestamp>', views.resultados, name='resultados'),
]
