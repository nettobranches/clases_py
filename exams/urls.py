from django.urls import path

from . import views

urlpatterns = [
    # ex: /exams/
    path('', views.index, name='index'),
    # ex: /exams/5/
    path('fisica/', views.detail, name='detail'),
]
