from sympy import *
from sympy.parsing.latex import parse_latex
from sympy.physics import units as u


# constantes
e0 = 8.85*10**-12


def emyoMethod(unidad, strMethod, params, pregunta):
    print("strmethod", strMethod);
    res = ""
    if (strMethod == "carga_cv"):
        res =carga_cv(params)
    elif(strMethod == "capacitancia_qv"):
        res = capacitancia_qv(params)
    elif(strMethod == "capacitancia_e0ea"):
        res = capacitancia_e0ea(params)
    elif(strMethod == "capacitancia_serie3"):
        res = capacitancia_serie3(params)
    elif(strMethod == "energiapotencial_cv"):
        res = energiapotencial_cv(params)
    elif(strMethod == "cap_serie_paralelo"):
        res = cap_serie_paralelo(params)

    return res

# unidad 1
def carga_cv(params):
    c = float(params[0].res)*10**-6
    v = float(params[1].res)
    q = c*v
    res = " \\( \\begin{align*}"\
    " q &= c \\cdot v "\
    "\\\\"\
    " q &= " + str(c) + " \\cdot " + str(v) + " = "+str(q) +"C"\
    "\\end{align*}"\
    "\\)"
    return res

def capacitancia_qv(params):
    v = float(params[0].res)
    q = float(params[1].res)*10**-6
    c = q/v
    res = " \\( \\begin{align*}"\
    "c &= \\dfrac{ q }{ v } "\
    "\\\\"\
    "c &= \\dfrac{"+ str(q) +"}{"+ str(v) +"} =" + str(c) +"F"\
    "\\end{align*}"\
    "\\)"
    return res

def capacitancia_e0ea(params):
    d = float(params[0].res)*10**-3
    A = float(params[1].res)
    c = e0*A/d
    res = " \\( \\begin{align*}"\
    "c &= e_{0} \\cdot \\dfrac{ A }{ d }"\
    "\\\\"\
    "c &= 1 \\cdot \\dfrac{"+ str(A) +"}{"+ str(d) +"} = "+ str(c) +"F"\
    "\\end{align*}"\
    "\\)"
    return res

def capacitancia_serie3(params):
    c1 = float(params[0].res)
    c2 = float(params[1].res)
    c3 = float(params[1].res)
    ct = 1/( 1/c1 + 1/c2 + 1/c3 )
    # return " \\( \dfrac{ 1 }{ ct } = \dfrac{ 1 }{ c_{1} } +\dfrac{ 1 }{ c_{2} } + \dfrac{ 1 }{ c_{3} } = "+ str(ct) + "\\)"
    res = " \\( \\begin{align*}"\
    "\dfrac{ 1 }{ ct } &= \dfrac{ 1 }{ c_{1} } +\dfrac{ 1 }{ c_{2} } + \dfrac{ 1 }{ c_{3} }"\
    "\\\\"\
    "\dfrac{ 1 }{ ct } &= \dfrac{ 1 }{"+str(c1)+"} +\dfrac{ 1 }{"+str(c2)+"} + \dfrac{ 1 }{"+str(c3)+"} = "+ str(ct) +"F"\
    "\\end{align*}"\
    "\\)"
    return res

def energiapotencial_cv(params):
    c = float(params[0].res)*10**-6
    v = float(params[1].res)
    pe = (1/2)*c*v**2
    res = " \\( \\begin{align*}"\
    "pe &= \dfrac{ 1 }{ 2 } \cdot c \cdot v^2"\
    "\\\\"\
    "pe &= \dfrac{ 1 }{ 2 } \cdot "+str(c)+" \cdot "+str(v)+"^2 ="+ str(pe) + "F"\
    "\\end{align*}"\
    "\\)"
    return res

def cap_serie_paralelo(params):
    c1 = float(params[0].res)*10**-6
    c2 = float(params[1].res)*10**-6
    c3 = float(params[2].res)*10**-6
    ct_paralelo = c1 + c2
    ct_serie = 1/( 1/ct_paralelo + 1/c3 )
    res = " \\( \\begin{align*}"\
    "c_{1,2} &= c_{1} + c_{2}"\
    "\\\\"\
    "c_{1,2} &="+ str(c1) +"+"+ str(c2) +" = "+ str(ct_paralelo) + "F"\
    "\\\\"\
    "\\dfrac{ 1 }{ ct } &= \\dfrac{ 1 }{ c_{1,2} } + \\dfrac{ 1 }{ c_{3} }"\
    "\\\\"\
    "\\dfrac{ 1 }{ ct } &= \\dfrac{ 1 }{"+str(ct_paralelo)+"} + \\dfrac{ 1 }{"+ str(c3) +"} = "+ str(ct_serie) +"F"\
    "\\end{align*}"\
    "\\)"
    return res
