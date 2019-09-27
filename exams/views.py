from django.http import HttpResponse
from .models import Pregunta, RespuestaOriginal, RespuestaAleatoria, RespuestaOrden
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

def setRandom(pregunta_list, ts, materia, unidad):
    res_list = RespuestaOriginal.objects.filter(pregunta__unidad__numero = unidad, pregunta__unidad__materia__nombre = materia)

    for ritem in res_list:
        ni = RespuestaAleatoria(marca = str(ts), pregunta = ritem.pregunta, variable = ritem.variable, res = ritem.generate_res() )
        ni.save()

    p_list = []
    for pregunta in pregunta_list:
        tPregunta = pregunta.getRandom(ts)
        print("p", pregunta)
        p_list.append({'pregunta': tPregunta[0], 'imagen': pregunta.imagen })
    return p_list

def resultados(request, timestamp):
    meta = RespuestaAleatoria.objects.filter(marca = timestamp)
    print('meta',timestamp, meta[0].pregunta.unidad, "materia", meta[0].pregunta.unidad.materia.nombre, "unidad numero", meta[0].pregunta.unidad.numero)
    materia = meta[0].pregunta.unidad.materia.nombre
    unidad = meta[0].pregunta.unidad.numero
    # materia = "fisica"
    # unidad = "2"

    pregunta_list = Pregunta.objects.filter(unidad__numero = unidad, unidad__materia__nombre = materia)
    print('pregunta_list', pregunta_list)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    for pregunta in pregunta_list:
        # print("p:", pregunta.getRandom(timestamp))
        p_list.append({'pregunta': pregunta.getRandom(timestamp)})

    # return HttpResponse("timestamp: "+str(timestamp) )
    template = loader.get_template('exams/tpl_result.html')
    context = {
        'timestamp': timestamp,
        'materia': materia,
        'unidad': 'unidad '+unidad,
        'grupos': '',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def resultados_original(request, materia, unidad):
    print("materia", materia)

    #pregunta_list = Pregunta.objects.filter(materia = materia, unidad = unidad)
    pregunta_list = Pregunta.objects.filter(unidad__numero = unidad, unidad__materia__nombre = materia)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    for pregunta in pregunta_list:
        # print("p:", pregunta.getRandom(timestamp))
        p_list.append({'pregunta': pregunta.getOriginal(), 'imagen': pregunta.imagen })

    # return HttpResponse("timestamp: "+str(timestamp) )
    #print('p list', p_list)
    template = loader.get_template('exams/tpl_result.html')
    context = {
        'timestamp': 0,
        'materia': materia,
        'unidad': 'unidad '+ unidad,
        'grupos': '',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def preguntas_original(request, materia, unidad):
    print("materia", materia, unidad)

    pregunta_list = Pregunta.objects.filter(unidad__numero = unidad, unidad__materia__nombre = materia)
    #print('list', pregunta_list)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    for pregunta in pregunta_list:
        #print("p:", pregunta.getRandom(timestamp))
        p_list.append({'pregunta': pregunta.getOriginal()[0], 'imagen': pregunta.imagen })

    # return HttpResponse("timestamp: "+str(timestamp) )
    template = loader.get_template('exams/tpl_examen.html')
    context = {
        'timestamp': 0,
        'materia': materia,
        'unidad': 'unidad '+ unidad,
        'grupos': '',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def preguntas_generar(request, materia, unidad):
    pregunta_list = Pregunta.objects.filter(unidad__numero = unidad, unidad__materia__nombre = materia)

    ts = int(time.time())
    p_list = setRandom(pregunta_list, ts, materia, unidad)

    print("list", p_list)
    # print(res_list)
    template = loader.get_template('exams/tpl_examen.html')
    context = {
        'timestamp': ts,
        'materia': materia,
        'unidad': 'unidad'+unidad,
        'grupos': '',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def preguntas_ordinario(request, materia):
    pregunta_list = Pregunta.objects.filter(unidad__materia__nombre = materia).order_by('?')[:11]
    #print('list', pregunta_list)
    # print("unidad", meta.pregunta.unidad)
    p_list = []
    i = 0
    ts = int(time.time())
    for pregunta in pregunta_list:
        #print("p:", pregunta.getRandom(timestamp))
        i+=1
        resOrden = RespuestaOrden(timestamp = ts, orden = i, pregunta = pregunta)
        resOrden.save()
        p_list.append({'pregunta': pregunta.getOriginal()[0], 'imagen': pregunta.imagen })

    # return HttpResponse("timestamp: "+str(timestamp) )
    template = loader.get_template('exams/tpl_examen.html')
    context = {
        'timestamp': ts,
        'materia': materia,
        'unidad': 'ordinario',
        'grupos': '',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

def resultados_ordinario(request, timestamp):
    preguntaorden_list = RespuestaOrden.objects.filter(timestamp = timestamp).order_by('orden')

    p_list = []
    for preguntaorden in preguntaorden_list:
        # print("p:", pregunta.getRandom(timestamp))
        print(preguntaorden)
        p_list.append({'pregunta': preguntaorden.pregunta.getOriginal(), 'imagen': preguntaorden.pregunta.imagen })
    materia = ''

    template = loader.get_template('exams/tpl_result.html')
    context = {
        'timestamp': timestamp,
        'materia': materia,
        'unidad': 'ordinario',
        'grupos': '',
        'pregunta_list': p_list,
    }
    return HttpResponse(template.render(context, request))

