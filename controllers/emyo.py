from sympy import *
from sympy.parsing.latex import parse_latex
from sympy.physics import units as u


# constantes
e0 = 8.85*10**-12
k = 9*10**9


def emyoMethod(unidad, strMethod, params, pregunta):
    print("strmethod", strMethod);
    res = ""
    # unidad 1
    if (strMethod == "ley_coulomb_r"):
        res = ley_coulomb_r(params)
    elif (strMethod == "ley_coulomb_q"):
        res = ley_coulomb_q(params)
    elif (strMethod == "intensidad_campo_electrico_e"):
        res = intensidad_campo_electrico_e(params)
    elif (strMethod == "intensidad_campo_electrico_sum_e"):
        res = intensidad_campo_electrico_sum_e(params)
    elif (strMethod == "energia_potencial_r"):
        res = energia_potencial_r(params)
    elif (strMethod == "diferencia_potencial_v"):
        res = diferencia_potencial_v(params)
    # unidad 2
    elif (strMethod == "carga_cv"):
        res = carga_cv(params)
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
    # unidad 3
    elif(strMethod == "n_electrones"):
        res = n_electrones(params)
    elif(strMethod == "corriente_rv"):
        res = corriente_rv(params)
    elif(strMethod == "corriente_potencia"):
        res = corriente_potencia(params)
    elif(strMethod == "corriente_resistencia"):
        res = corriente_resistencia(params)
    elif(strMethod == "resistencia_serie"):
        res = resistencia_serie(params)
    elif(strMethod == "resistencia_paralelo"):
        res = resistencia_paralelo(params)
    elif(strMethod == "resistencia_mixta"):
        res = resistencia_mixta(params)
    elif(strMethod == "kirchoff_ley2"):
        res = kirchoff_ley2(params)

    return res

# unidad 1    
def ley_coulomb_r(params):
    q = float(params[0].res)*10**-6
    f = float(params[1].res)
    r = sqrt(k*q*q/f)
    res = " \\( \\begin{align*}"\
    " r &= \\sqrt{ \\dfrac{ k \\cdot Q \\cdot q }{ F }  } "\
    "\\\\"\
    " r &= \\sqrt{ \\dfrac{ " + str(format(k,'0.2E')) + " \\cdot " + str(format(q,'0.2E')) + " \\cdot " + str(format(q,'0.2E')) + " }{ " + str(f) + " }  } = "+str(format(r,'0.6f')) +" m"\
    "\\end{align*}"\
    "\\)"
    return res

def ley_coulomb_q(params):
    r = float(params[0].res)*10**-3
    f = float(params[1].res)
    q = sqrt(f*r**2/k)
    res = " \\( \\begin{align*}"\
    " q &= \\sqrt{ \\dfrac{ F \\cdot r^2 }{ k }  } "\
    "\\\\"\
    " q &= \\sqrt{ \\dfrac{ " + str(f) + " \\cdot " + str(format(r,'0.2f')) + "^2 }{ " + str(format(k,'0.2E')) + " }  }  = "+str(format(q,'0.2E')) +" C"\
    "\\end{align*}"\
    "\\)"
    return res

def intensidad_campo_electrico_e(params):
    q = float(params[0].res)*10**-6
    f = float(params[1].res)*10**-5
    e = f/q
    res = " \\( \\begin{align*}"\
    " E &= \\dfrac{ F }{ q } "\
    "\\\\"\
    " E &= \\dfrac{ " + str(format(f,'0.2E')) + " }{ " + str(format(q,'0.2E')) + " } = "+str(format(e,'0.2f')) +" N/C"\
    "\\end{align*}"\
    "\\)"
    return res

def intensidad_campo_electrico_sum_e(params):
    r = float(params[0].res)*10**-3/2
    q1 = -float(params[1].res)*10**-6
    q2 = float(params[2].res)*10**-6
    e1 = k*q1/r**2
    e2 = k*q2/r**2
    er = e1 + e2
    res = " \\( \\begin{align*}"\
    " E1 &= \\dfrac{ k \\cdot q1 }{ r^2 } "\
    "\\\\"\
    " E2 &= \\dfrac{ k \\cdot q2 }{ r^2 } "\
    "\\\\"\
    " E &= E1 + E2 "\
    "\\\\"\
    " E1 &= \\dfrac{ " + str(format(k,'0.2E')) + " \\cdot " + str(format(q1,'0.2E')) + " }{ " + str(format(r,'0.3f')) + "^2 } = "+str(format(e1,'0.2E')) +" C"\
    "\\\\"\
    " E2 &= \\dfrac{ " + str(format(k,'0.2E')) + " \\cdot " + str(format(q2,'0.2E')) + " }{ " + str(format(r,'0.3f')) + "^2 } = "+str(format(e2,'0.2E')) +" C"\
    "\\\\"\
    " E &= " + str(format(e1,'0.2E')) + " + " + str(format(e2,'0.2E')) + " = "+str(format(er,'0.2E')) +" C"\
    "\\end{align*}"\
    "\\)"
    return res

def energia_potencial_r(params):
    Q = -float(params[0].res)*10**-6
    q = -float(params[1].res)*10**-9
    pe = float(params[2].res)*10**-5
    r=k*Q*q/pe
    res = " \\( \\begin{align*}"\
    " r &= \\dfrac{ k \\cdot Q \\cdot q }{ p.e } "\
    "\\\\"\
    " r &= \\dfrac{ " + str(format(k,'0.2E')) + " \\cdot " + str(format(Q,'0.2E')) + " \\cdot " + str(format(q,'0.2E')) + " }{ " + str(format(pe,'0.2E')) + " } = "+str(format(r,'0.2f')) +" m"\
    "\\end{align*}"\
    "\\)"
    return res

def diferencia_potencial_v(params):
    q1 = 45*10**-9
    
    q2 = -float(params[1].res)*10**-9
    r2 = float(params[2].res)*10**-3
    r1 = abs( float(params[0].res)*10**-3 - float(params[2].res)*10**-3 )

    v1 = k*q1/r1
    v2 = k*q2/r2
    v = v1+v2
    res = " \\( \\begin{align*}"\
    " V &= \\dfrac{ k \\cdot Q }{ r } "\
    "\\\\"\
    " V1 &= \\dfrac{ " + str(format(k,'0.2E')) + " \\cdot " + str(format(q1,'0.2E')) + " }{ " + str(format(r1,'0.2E')) + " } = "+str(format(v1,'0.6f')) +" v"\
    "\\\\"\
    " V2 &= \\dfrac{ " + str(format(k,'0.2E')) + " \\cdot " + str(format(q2,'0.2E')) + " }{ " + str(format(r2,'0.2E')) + " } = "+str(format(v2,'0.6f')) +" v"\
    "\\\\"\
    " V &= " + str(format(v1,'0.2E')) + " + " + str(format(v2,'0.2E')) + " = " + str(format(v,'0.2E')) +" v"\
    "\\end{align*}"\
    "\\)"
    return res

# unidad 2
def carga_cv(params):
    c = float(params[0].res)*10**-6
    v = float(params[1].res)
    q = c*v
    res = " \\( \\begin{align*}"\
    " q &= c \\cdot v "\
    "\\\\"\
    " q &= " + str(format(c,'0.6f')) + " \\cdot " + str(v) + " = "+str(format(q,'0.6f')) +"C"\
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
    "c &= \\dfrac{"+ str(q) +"}{"+ str(v) +"} =" + str(format(c,'0.2E')) +"F"\
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
    "c &= "+str(format(e0,'0.2E'))+" \\cdot \\dfrac{"+ str(A) +"}{"+ str(d) +"} = "+ str(format(c,'0.2E')) +"F"\
    "\\end{align*}"\
    "\\)"
    return res

def capacitancia_serie3(params):
    c1 = float(params[0].res)
    c2 = float(params[1].res)
    c3 = float(params[2].res)
    ct = 1/( 1/c1 + 1/c2 + 1/c3 )
    # return " \\( \dfrac{ 1 }{ ct } = \dfrac{ 1 }{ c_{1} } +\dfrac{ 1 }{ c_{2} } + \dfrac{ 1 }{ c_{3} } = "+ str(ct) + "\\)"
    res = " \\( \\begin{align*}"\
    "\dfrac{ 1 }{ ct } &= \dfrac{ 1 }{ c_{1} } +\dfrac{ 1 }{ c_{2} } + \dfrac{ 1 }{ c_{3} }"\
    "\\\\"\
    "\dfrac{ 1 }{ ct } &= \dfrac{ 1 }{"+str(c1)+"} +\dfrac{ 1 }{"+str(c2)+"} + \dfrac{ 1 }{"+str(c3)+"} = "+ str(format(ct,'0.2E')) +"F"\
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
    "pe &= \dfrac{ 1 }{ 2 } \cdot "+str(format(c,"0.6f"))+" \cdot "+str(v)+"^2 ="+ str(pe) + "W"\
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
    "c_{1,2} &="+ str(format(c1,"0.6f")) +"+"+ str(format(c2,"0.6f")) +" = "+ str(format(ct_paralelo,'0.6f')) + "F"\
    "\\\\"\
    "\\dfrac{ 1 }{ ct } &= \\dfrac{ 1 }{ c_{1,2} } + \\dfrac{ 1 }{ c_{3} }"\
    "\\\\"\
    "\\dfrac{ 1 }{ ct } &= \\dfrac{ 1 }{"+str(format(ct_paralelo,'0.6f'))+"} + \\dfrac{ 1 }{"+ str(format(c3,"0.6f")) +"} = "+ str(format(ct_serie,'0.2E')) +"F"\
    "\\end{align*}"\
    "\\)"
    return res

# unidad 3

def n_electrones(params):
    i = float(params[0].res)
    t = 1
    q = i*t/(1.6*10**-19)
    res = " \\( \\begin{align*}"\
    " q &= I \\cdot t \\cdot \\dfrac{ 1 }{ 1.6x10^-19 } "\
    "\\\\"\
    " q &= " + str(format(i,'0.6f')) + " \\cdot " + str(t) + " \\dfrac{ 1 }{ 1.6x10^-19 } = "+str(format(q,'0.2E')) +" electrones"\
    "\\end{align*}"\
    "\\)"
    return res

def corriente_rv(params):
    r = float(params[0].res)
    v = float(params[1].res)
    i = v / r
    res = " \\( \\begin{align*}"\
    " I &= \\dfrac{ V }{ R } "\
    "\\\\"\
    " I &= \\dfrac{" + str(v) + " }{ " + str(r) + "} = "+str(format(i,'0.2f')) +"A"\
    "\\end{align*}"\
    "\\)"
    return res

def corriente_potencia(params):
    r = float(params[0].res)
    v = float(params[1].res)
    p = v**2/r
    res = " \\( \\begin{align*}"\
    " P &= \\dfrac{ V^2 }{ R } "\
    "\\\\"\
    " P &= \\dfrac{" + str(format(v,'0.2f')) + "^2 }{ " + str(r) + "} = "+str(format(p,'0.2f')) +"W"\
    "\\end{align*}"\
    "\\)"
    return corriente_rv(params)+res

def corriente_resistencia(params):
    return corriente_pv(params)+resistencia_vi(params)

def corriente_pv(params):
    v = float(params[0].res)
    p = float(params[1].res)*1000
    i = p/v
    res = " \\( \\begin{align*}"\
    " I &= \\dfrac{ P }{ V } "\
    "\\\\"\
    " I &= \\dfrac{" + str(format(p,'0.2f')) + " }{ " + str(v) + "} = "+str(format(i,'0.2f')) +"A"\
    "\\end{align*}"\
    "\\)"
    return res

def resistencia_vi(params):
    v = float(params[0].res)
    p = float(params[1].res)*1000
    i = p/v
    r = v/i
    res = " \\( \\begin{align*}"\
    " R &= \\dfrac{ V }{ I } "\
    "\\\\"\
    " R &= \\dfrac{" + str(format(v,'0.2f')) + " }{ " + str(i) + "} = "+str(format(r,'0.2f')) +"\\Omega"\
    "\\end{align*}"\
    "\\)"
    return res

def resistencia_serie(params):
    r1 = float(params[0].res)
    r2 = float(params[1].res)
    rt = r1 + r2
    res = " \\( \\begin{align*}"\
    " R_{t} &= R_{1} + R_{2} "\
    "\\\\"\
    " R_{t} &= " + str(format(r1,'0.2f')) + " + " + str(r2) + "  = "+str(format(rt,'0.2f')) +" electrones"\
    "\\end{align*}"\
    "\\)"
    return res

def resistencia_paralelo(params):
    r1 = float(params[0].res)
    r2 = float(params[1].res)
    rt = 1/(1/r1 + 1/r2)
    res = " \\( \\begin{align*}"\
    " \\dfrac{ 1 }{ R_{t} } &= \\dfrac{ 1 }{ R_{1} } + \\dfrac{ 1 }{ R_{2} } "\
    "\\\\"\
    " \\dfrac{ 1 }{ R_{t} } &= \\dfrac{ 1 }{" + str(format(r1,'0.2f')) + " } + \\dfrac{ 1 }{ " + str(r2) + "} = "+str(format(rt,'0.2f')) +"\\Omega"\
    "\\end{align*}"\
    "\\)"
    return res

def resistencia_mixta(params):
    r1 = float(params[0].res)
    r2 = float(params[1].res)
    r3 = float(params[2].res)
    r4 = float(params[3].res)
    r5 = float(params[4].res)

    r12 = r1 + r2

    r123 = 1/( 1/r12 + 1/r3 )

    r1234 = r123 + r4

    rt = 1/( 1/r1234 + 1/r5 )

    res = " \\( \\begin{align*}"\
    " R_{1,2} &= R_{1} + R_{2} "\
    "\\\\"\
    " \\dfrac{ 1 }{ R_{1,2,3} } &= \\dfrac{ 1 }{ R_{1,2} } + \\dfrac{ 1 }{ R_{3} } "\
    "\\\\"\
    " R_{1,2,3,4} &= R_{1,2,3} + R_{4} "\
    "\\\\"\
    " \\dfrac{ 1 }{ R_{t} } &= \\dfrac{ 1 }{ R_{1,2,3,4} } + \\dfrac{ 1 }{ R_{5} } "\
    "\\end{align*}"\
    "\\)"\
    " \\( \\begin{align*}"\
    " R_{1,2} &= " + str(format(r1,'0.2f')) + " + " + str(r2) + " = "+str(format(r12,'0.2f')) +"\\Omega"\
    "\\\\"\
    " \\dfrac{ 1 }{ R_{1,2,3} } &= \\dfrac{ 1 }{" + str(format(r12,'0.2f')) + " } + \\dfrac{ 1 }{ " + str(r3) + "} = "+str(format(r123,'0.2f')) +"\\Omega"\
    "\\\\"\
    " R_{1,2,3,4} &= " + str(format(r123,'0.2f')) + " + " + str(r4) + " = "+str(format(r1234,'0.2f')) +"\\Omega"\
    "\\\\"\
    " \\dfrac{ 1 }{ R_{t} } &= \\dfrac{ 1 }{" + str(format(r1234,'0.2f')) + " } + \\dfrac{ 1 }{ " + str(r5) + "} = "+str(format(rt,'0.2f')) +"\\Omega"\
    "\\end{align*}"\
    "\\)"
    return res

def kirchoff_ley2(params):
    v1 = float(params[0].res)
    v2 = float(params[1].res)
    r1 = float(params[2].res)
    r2 = float(params[3].res)

    vt = v1 -v2

    rt = r1 + r2

    i = vt / rt

    res = " \\( \\begin{align*}"\
    " ee &= " + str(format(v1,'0.2f')) + " - " + str(v2) + " = "+str(format(vt,'0.2f')) +"\\Omega"\
    "\\end{align*}"\
    "\\)"\
    " \\( \\begin{align*}"\
    " eir &= I " + str(format(r1,'0.2f')) + " + I " + str(r2) + " = "+str(format(rt,'0.2f')) +"\\Omega"\
    "\\end{align*}"\
    "\\)"\
    " \\( \\begin{align*}"\
    " I &= \\dfrac{" + str(format(vt,'0.2f')) + " }{ " + str(rt) + "} = "+str(format(i,'0.2f')) +"A"\
    "\\end{align*}"\
    "\\)"
    return res
