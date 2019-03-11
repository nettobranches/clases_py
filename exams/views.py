from django.http import HttpResponse
from .models import Pregunta, RespuestaOriginal, RespuestaAleatoria
from django.template import loader
from django.shortcuts import get_object_or_404, render
import random, time

def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    template = loader.get_template('exams/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request):
    # question = get_object_or_404(Pregunta, pk=question_id)

    # ro = pregunta_list[0].respuestaoriginal_set.all()
    # print(pregunta_list)
    # print("respuesta original",  pregunta_list[0].getOriginal() )

    res_list = RespuestaOriginal.objects.all()
    ts = int(time.time())

    for ritem in res_list:
        ni = RespuestaAleatoria(marca = str(ts), pregunta = ritem.pregunta, variable = ritem.variable, res = random.randint( ritem.limite_inicial, ritem.limite_final ))
        ni.save()

    pregunta_list = Pregunta.objects.all()
    # print(res_list)
    template = loader.get_template('exams/detail.html')
    context = {
        'timestamp': ts,
        'materia': "fisica",
        'unidad': 'unidad I',
        'grupos': '1 QFB',
        'pregunta_list': pregunta_list,
    }
    return HttpResponse(template.render(context, request))

def get_timestamp(request, timestamp):

    pregunta_list = Pregunta.objects.all()
    # print(res_list)
    template = loader.get_template('exams/detail.html')
    context = {
        'timestamp': timestamp,
        'materia': "fisica",
        'unidad': 'unidad I',
        'grupos': '1 QFB',
        'pregunta_list': pregunta_list,
    }
    return HttpResponse(template.render(context, request))
