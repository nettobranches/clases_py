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
    pregunta_list.timestamp = timestamp
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

def calculo(request, unidad, respuesta, preguntas):
    # question = get_object_or_404(Pregunta, pk=question_id)

    # ro = pregunta_list[0].respuestaoriginal_set.all()
    # print(pregunta_list)
    # print("respuesta original",  pregunta_list[0].getOriginal() )


    # pregunta_list = Pregunta.objects.filter(materia="calculo", unidad= unidad).order_by('?')[:preguntas]
    pregunta_list = Pregunta.objects.filter(materia="calculo", unidad= unidad)[:preguntas]

    # p_list = setOriginal(pregunta_list)
    if( respuesta == 'o' ):
        ts = unidad
        p_list = setOriginal(pregunta_list)
    else:
        ts = int(time.time())
        p_list = setRandom(pregunta_list, ts)

    print("list", p_list)
    # print(res_list)
    template = loader.get_template('exams/tpl_examen.html')
    context = {
        'timestamp': ts,
        'materia': "calculo",
        'unidad': 'unidad II',
        'grupos': '2 QBT 3 ICM',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def setOriginal(pregunta_list):
    p_list = []
    for pregunta in pregunta_list:
        tPregunta = pregunta.getOriginal()
        print("p", tPregunta)
        p_list.append(tPregunta)
    return p_list

def setRandom(pregunta_list, ts):
    res_list = RespuestaOriginal.objects.all()

    for ritem in res_list:
        ni = RespuestaAleatoria(marca = str(ts), pregunta = ritem.pregunta, variable = ritem.variable, res = ritem.generate_res() )
        ni.save()

    p_list = []
    for pregunta in pregunta_list:
        tPregunta = pregunta.getRandom(ts)
        print("p", tPregunta)
        p_list.append(tPregunta[0])

    return p_list

def resultados(request, timestamp):
    meta = RespuestaAleatoria.objects.filter(marca = timestamp)
    materia = meta[0].pregunta.materia
    print("materia", materia)

    pregunta_list = Pregunta.objects.filter(materia=materia)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    for pregunta in pregunta_list:
        # print("p:", pregunta.getRandom(timestamp))
        p_list.append(pregunta.getRandom(timestamp))

    # return HttpResponse("timestamp: "+str(timestamp) )
    template = loader.get_template('exams/tpl_result.html')
    context = {
        'timestamp': timestamp,
        'materia': materia,
        'unidad': 'unidad I',
        'grupos': '1 QFB',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def resultados_original(request, materia, unidad):
    print("materia", materia)

    pregunta_list = Pregunta.objects.filter(materia = materia, unidad = unidad)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    for pregunta in pregunta_list:
        # print("p:", pregunta.getRandom(timestamp))
        p_list.append(pregunta.getOriginal())

    # return HttpResponse("timestamp: "+str(timestamp) )
    template = loader.get_template('exams/tpl_result.html')
    context = {
        'timestamp': 0,
        'materia': materia,
        'unidad': 'unidad '+ unidad,
        'grupos': '1 QFB',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def preguntas_original(request, materia, unidad):
    print("materia", materia)

    pregunta_list = Pregunta.objects.filter(materia = materia, unidad = unidad)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    for pregunta in pregunta_list:
        # print("p:", pregunta.getRandom(timestamp))
        p_list.append(pregunta.getOriginal()[0])

    # return HttpResponse("timestamp: "+str(timestamp) )
    template = loader.get_template('exams/tpl_examen.html')
    context = {
        'timestamp': 0,
        'materia': "Eléctromagnetismo y Óptica",
        'unidad': 'unidad '+ unidad,
        'grupos': '3 ICM',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def preguntas_generar(request, materia, unidad):
    # question = get_object_or_404(Pregunta, pk=question_id)

    # ro = pregunta_list[0].respuestaoriginal_set.all()
    # print(pregunta_list)
    # print("respuesta original",  pregunta_list[0].getOriginal() )
    respuesta = 'r'
    preguntas = 10

    # pregunta_list = Pregunta.objects.filter(materia="calculo", unidad= unidad).order_by('?')[:preguntas]
    pregunta_list = Pregunta.objects.filter(materia=materia, unidad= unidad)[:preguntas]

    # p_list = setOriginal(pregunta_list)
    if( respuesta == 'o' ):
        ts = unidad
        p_list = setOriginal(pregunta_list)
    else:
        ts = int(time.time())
        p_list = setRandom(pregunta_list, ts)

    print("list", p_list)
    # print(res_list)
    template = loader.get_template('exams/tpl_examen.html')
    context = {
        'timestamp': ts,
        'materia': "calculo",
        'unidad': 'unidad II',
        'grupos': '2 QBT 3 ICM',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))
