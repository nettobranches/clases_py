from controllers.calculo import calculoMethod

def doMethod(materia, unidad, metodo, params):
    res = ""
    print(materia, unidad, metodo, params)
    if(materia == "calculo"):
        res = calculoMethod(unidad, metodo, params)
    return res
