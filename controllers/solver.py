from controllers.calculo import calculoMethod
from controllers.emyo import emyoMethod
from controllers.fisica import fisicaMethod
from controllers.random_values import randomMethod

def doMethod(materia, unidad, metodo, params, pregunta):
    res = ""
    print(materia, unidad, metodo, params)
    if(materia == "calculo"):
        res = calculoMethod(unidad, metodo, params, pregunta)
    elif(materia == "emyo"):
        res = emyoMethod(unidad, metodo, params, pregunta)
    elif(materia == "fisica"):
        res = fisicaMethod(unidad, metodo, params, pregunta)
    return res

def doRandomMethod(str_method):
    print("random method", str_method)
    return randomMethod(str_method)

def replaceVars(materia, strRes, ro ):
    if(ro.mostrar == False and ro.res == "1" or ro.res == "0" ):
        value = ""
    else:
        value = ro.res

    return strRes.replace(str(ro.variable), str(value) )

def replaceVars2(materia, strRes, ro ):

    value = ro.res

    return strRes.replace(str(ro.variable), str(value) )
