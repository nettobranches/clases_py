
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
    elif (strMethod == "entero_x"):
        res = entero_x()
    elif (strMethod == "entero_xx"):
        res = entero_xx()
    elif (strMethod == "entero_xxx"):
        res = entero_xxx()
    elif (strMethod == "entero_xxxx"):
        res = entero_xxxx()
    elif (strMethod == "angulo_45"):
        res = angulo_45()
    elif (strMethod == "angulo_90"):
        res = angulo_90()
    elif (strMethod == "minutos"):
        res = minutos()
    elif (strMethod == "decimal"):
        res = decimal()
    elif (strMethod == "decimal_d"):
        res = decimal_d()
    elif (strMethod == "decimal_c"):
        res = decimal_c()
    elif (strMethod == "decimal_m"):
        res = decimal_m()
    elif (strMethod == "calculo_entero"):
        res = calculo_entero()
    elif (strMethod == "calculo_raiz"):
        res = calculo_raiz()
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

def calculo_fraccion():
    rndTipo = random.randint(0,3)

    if( rndTipo == 0 ):
        val = entero_x()
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
    denominador = numerador = random.randint( 2, 9 )
    while numerador == denominador and numerador < denominador:
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

def entero_x():
    rval = random.randint( 1, 9 )
    return str(rval)

def entero_xx():
    rval = random.randint( 10, 99 )
    return str(rval)

def entero_xxx():
    rval = random.randint( 100, 999 )
    return str(rval)

def entero_xxxx():
    rval = random.randint( 1000, 9999 )
    return str(rval)

def angulo_45():
    rval = random.randint( 1, 45 )
    return str(rval)

def angulo_90():
    rval = random.randint( 1, 90 )
    return str(rval)

def minutos():
    rval = random.randint( 1, 60 )
    return str(rval)

def decimal():
    rval = random.randint( 1, 99 )
    return str( float(rval)/100 )

def decimal_d():
    rval = random.randint( 1, 9 )
    return str( float(rval)/10 )

def decimal_c():
    rval = random.randint( 1, 9 )
    return str( float(rval)/100 )

def decimal_m():
    rval = random.randint( 1, 99 )
    return str( float(rval)/1000 )

def calculo_entero():
    rndTipo = random.randint(0,3)

    if( rndTipo == 0 ):
        val = entero_x()
    elif(rndTipo == 1):
        val = constantes()
    else:
        val = ""

    return val

def calculo_raiz():
    rval = random.randint( 1, 9 )**2
    return str(rval)
