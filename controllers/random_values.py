
import random

def randomMethod(strMethod):
    print("strmethod", strMethod);
    res = ""
    if (strMethod == "gt_one"):
        res =gt_one()
    elif (strMethod == "set_fracc"):
        res =set_fracc()
    elif (strMethod == "pares"):
        res =pares()
    elif (strMethod == "raices"):
        res =raices()
    else:
        res =default()

    return res

def default():
    val = gt_one()

    return val

def default_all():
    rndTipo = random.randint(0,2)

    if( rndTipo == 0 ):
        val = gt_one()
    elif(rndTipo == 1):
        val = set_fracc()
    elif(rndTipo == 2):
        val = constantes()

    return val

def default_empty():
    rndTipo = random.randint(0,3)

    if( rndTipo == 0 ):
        val = gt_one()
    elif(rndTipo == 1):
        val = set_fracc()
    elif(rndTipo == 2):
        val = constantes()
    else:
        val = ""

    return val


def gt_one():
    rval = random.randint( 2, 9 )
    return str(rval)

def set_fracc():
    numerador = random.randint( 2, 9 )
    denominador = random.randint( 2, 9 )
    return "\\frac{" + str(numerador) + "}{" + str(denominador) +"}"

def pares():
    lPares = [2, 4, 6]
    return  lPares[random.randint(0,2)]

def raices():
    rval = random.randint( 2, 9 )
    return str( rval**2 )

def constantes():
    lConst = ["a", "b", "c", "m", "n"]
    return  lConst[random.randint(0,4)]
