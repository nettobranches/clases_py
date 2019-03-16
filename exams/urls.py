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
    path('calc/', views.calculo, name='calculo'),

    path('resultados/<int:timestamp>', views.resultados, name='resultados'),
]
