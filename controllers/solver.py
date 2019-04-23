from controllers.calculo import calculoMethod
from controllers.emyo import emyoMethod
from controllers.random_values import randomMethod

def doMethod(materia, unidad, metodo, params, pregunta):
    res = ""
    print(materia, unidad, metodo, params)
    if(materia == "calculo"):
        res = calculoMethod(unidad, metodo, params, pregunta)
    elif(materia == "emyo"):
        res = emyoMethod(unidad, metodo, params, pregunta)
    return res

def doRandomMethod(str_method):
    print("random method", str_method)
    return randomMethod(str_method)
