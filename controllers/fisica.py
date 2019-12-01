from sympy import *
from sympy.parsing.latex import parse_latex
from sympy.physics import units as u
from math import *


# constantes
e0 = 8.85*10**-12


def fisicaMethod(unidad, strMethod, params, pregunta):
    print("strmethod", strMethod);
    res = ""
    # unidad 1
    if (strMethod == "u1_1"):
        res =u1_1(params)
    elif(strMethod == "u1_2"):
        res = u1_2(params)
    elif(strMethod == "u1_3"):
        res = u1_3(params)
    elif(strMethod == "u1_4"):
        res = u1_4(params)
    elif(strMethod == "u1_5"):
        res = u1_5(params)
    elif(strMethod == "u1_6"):
        res = u1_6(params)
    elif(strMethod == "u1_7"):
        res = u1_7(params)
    # unidad 2
    elif (strMethod == "u2_1"):
        res =u2_1(params)
    elif(strMethod == "u2_2"):
        res = u2_2(params)
    elif(strMethod == "u2_3"):
        res = u2_3(params)
    elif(strMethod == "u2_4"):
        res = u2_4(params)
    elif(strMethod == "u2_5"):
        res = u2_5(params)
    elif(strMethod == "u2_6"):
        res = u2_6(params)
    elif(strMethod == "u2_7"):
        res = u2_7(params)
    # unidad 3
    elif (strMethod == "res_06_07"):
        res =res_06_07(params)
    elif (strMethod == "res_06_16"):
        res =res_06_16(params)
    elif (strMethod == "res_06_21"):
        res =res_06_21(params)
    elif (strMethod == "res_06_28"):
        res =res_06_28(params)
    elif (strMethod == "res_06_37"):
        res =res_06_37(params)
    elif (strMethod == "res_06_40"):
        res =res_06_40(params)

    return res

# unidad 1
def u1_1(params):
    l = float(params[0].res)
    a = float(params[1].res)
    foot = 3.28
    fl = l*foot
    fa = a*foot
    res = str(fl)+" ft  "+str(fa)+" ft"
    return res

def u1_2(params):
    c = float(params[0].res)
    d = float(params[1].res)
    i3 = 0.061 #cm3
    inc =0.03937 #mm 
    ic = c * i3
    ind = d * inc
    res = str(ic)+"in3 "+str(format(ind,'0.2f'))+"in "
    return res

def u1_3(params):
    dens = float(params[0].res)
    kgm3 = 1000 #gcm3
    kgm3dens = dens * 1000
    res = str(kgm3dens)+" kg/m3 "
    return res

def u1_4(params):
    v1 = float(params[0].res)
    v2 = float(params[1].res)
    anglex = 0
    angley = 90

    vx = v1 * cos(radians(anglex)) + v2 * cos(radians(angley))
    vy = v1 * sin(radians(anglex)) + v2 * sin(radians(angley))
    vt = sqrt(vx**2 + vy**2)
    res =  str(format(vt,'0.2f'))+" km "
    return res

def u1_5(params):
    v1 = float(params[0].res)
    v2 = float(params[2].res)
    anglex = float(params[1].res)
    angley = float(params[3].res)

    vx = v1 * cos(radians(anglex)) + v2 * cos(radians(angley))
    vy = v1 * sin(radians(anglex)) + v2 * sin(radians(angley))
    vt = sqrt(vx**2 + vy**2)
    res =  str(format(vt,'0.2f'))+" m"
    return res

def u1_6(params):
    v1 = float(params[1].res)
    v2 = float(params[2].res)
    angle1 = 0
    angle2 = float(params[0].res)

    vx = v1 * cos(radians(angle1)) + v2 * cos(radians(angle2))
    vy = v1 * sin(radians(angle1)) + v2 * sin(radians(angle2))
    vt = sqrt(vx**2 + vy**2)
    res =  str(format(vt,'0.2f'))+" N"
    return res

def u1_7(params):
    v1 = float(params[0].res)
    angle1 = float(params[1].res)
    v2 = float(params[2].res)
    angle2 = float(params[3].res)
    v3 = float(params[4].res)
    angle3 = float(params[5].res)

    vx1 = v1 * cos(radians(angle1))
    vx2 = v2 * cos(radians(angle2))
    vx3 = v3 * cos(radians(angle3))
  
    vy1 = v1 * sin(radians(angle1))
    vy2 = v2 * sin(radians(angle2))
    vy3 = v3 * sin(radians(angle3))
 
    res =  " Vx1 = "+str(format(vx1,'0.2f'))+" Vy1 = "+str(format(vy1,'0.2f'))+ "Vx2 = "+str(format(vx2,'0.2f'))+" Vy2 = "+str(format(vy2,'0.2f'))+" Vx3 = "+str(format(vx3,'0.2f'))+" Vy3 = "+str(format(vy3,'0.2f'))
    return res


# unidad 2
def u2_1(params):
    w = 1
    angle = 1
    if(len(params) == 2):
        w = float(params[0].res)
        angle = float(params[1].res)
    n = w * cos(radians(angle))
    f = w * sin(radians(angle))
    res = " \\( \\begin{align*}"\
    " N = W_{x} &= w * \\cos(a) = " + str(w) + " * \\cos("+str(angle)+ ") = " + str(format(n,'0.2f')) +"N"\
    "\\\\"\
    " F = W_{y} &= w * \\sin(a) = " + str(w) + " * \\sin("+str(angle)+ ") = " + str(format(f,'0.2f')) +"N"\
    "\\end{align*}"\
    "\\)"
    return res

def u2_2(params):
    ty = 1
    angle = 1
    if( len(params) == 2 ):
        ty = float(params[0].res)/2
        angle = 90 - float(params[1].res)/2
    t = ty / sin(radians(angle))
    res = " \\( T = \\dfrac{ T_{y} }{sin{"+str(angle)+"º} } = "\
    " \\dfrac{ "+str(ty)+" }{sin{"+str(angle)+"º} } ="\
    ""+ str(format(t,'0.2f')) +"N \\)"
    return res

def u2_3(params):
    # f = float(params[0].res)
    # w = float(params[1].res)
    # n = float(params[2].res)
    f = 40.0
    w = 600.0
    n = 10.0
    ms = f/w
    mk = n/w
    res = " \\(  m_{s} = \\frac{"+str(f)+"}{"+str(w)+"} = " + str(format(ms,'0.4f')) +"\\; "\
    "m_{k} = \\frac{"+str(n)+"}{"+str(w)+"} = "+ str(format(mk,'0.4f')) +" \\)"
    return res

def u2_4(params):
    n = 1
    if( len(params) > 0):
        n = float(params[0].res)
    ms = 0.7
    mk = 0.4
    fs = ms*n
    fk = mk*n
    res = " \\( F_{s} = "+str(n)+"N * "+ str(format(fs,'0.1f')) +"N \\; F_{k}="+ str(n)+"N * "+str(format(fk,'0.1f')) +"N\\)"\
    " \\( F_{s} = "+ str(format(fs,'0.1f')) +"N \\; F_{k}="+ str(format(fk,'0.1f')) +"N\\)"
    return res

def u2_5(params):
    w = 60
    angle = 90 - 43
    wx = w * sin(radians(angle))
    n = w * cos(radians(angle))
    res = " \\( N = "+str(w)+"*\\sin("+str(angle)+") = "+str(format(n,'0.1f'))+"N \\, W_{x} = "+str(w)+"*cos("+str(angle)+") = "+str(format(wx,'0.1f'))+ "N \\)"
    return res

def u2_6(params):
    d = 1
    f = 1
    if( len(params) == 2):
        d = float(params[0].res)/100
        f = float(params[1].res)
    torque_90 = f * d * sin(radians(90))
    torque_60 = f * d * sin(radians(60))
    torque_30 = f * d * sin(radians(30))
    torque_0 = f * d * sin(radians(0))
    res = " \\( \\begin{align*}"\
    "t_{90º} &= "+ str(format(torque_90,'0.0f')) +"N m"\
    "\\\\"\
    "t_{60º} &= "+ str(format(torque_60,'0.0f')) +"N m"\
    "\\\\"\
    "t_{30º} &= "+ str(format(torque_30,'0.0f')) +"N m"\
    "\\\\"\
    "t_{0º} &= "+ str(format(torque_0,'0.0f')) +"N m"\
    "\\end{align*}"\
    "\\)"
    return res

def u2_7(params):
    sum_torque = 30*0 + 15*4 - 20*9
    res = " \\( t ="+str(format(sum_torque,'0.1f'))+ " N m \\)"
    return res

def res_06_07(params):
    v = 1
    hrs = 1
    mn = 1
    if( len(params) > 0 ):
        v = float(params[0].res)
        hrs = float(params[1].res)
        mn = float(params[2].res)/float(60)
    # print( "min",params[2].res, float(params[2].res)/float(60) )
    t = hrs + mn
    x = v*t
    res = " \\( s = "+str(v)+" * "+str(t)+" ="+ str(format(x,'0.1f')) +" mi \\)"
    return res

def res_06_16(params):
    x = 1
    vf = 1
    if(len(params) > 0):
        x = float(params[0].res)/12
        vf = float(params[1].res)
    vi = 0
    a = (vf**2 - vi**2)/(2*x)
    t = 2*x/(vi + vf)
    res = " \\( \\begin{align*}"\
    "a &= \\dfrac{"+str(vf)+"^2 - "+str(vi)+"^2}{ 2*"+str(x)+"} = "+ str(format(a,'0.2E')) +" ft/s^2"\
    "\\\\"\
    "t &= "+ str(format(t,'0.4f')) +"s"\
    "\\end{align*}"\
    "\\)"
    return res

def res_06_21(params):
    x = 1
    if(len(params) == 1):
        x = float(params[0].res)
    g = -9.8
    v0 = 0
    # t = sqrt(x*2/g)
    t = sqrt( -x * 2 /-9.8)
    vf = v0 + g*t
    res = " \\( \\begin{align*}"\
    "t &= \\sqrt{-"+str(x)+"m * \\dfrac{2}{"+str(g)+"m/s^2 }} = " + str(format(t,'0.2f')) +" s"\
    "\\\\"\
    "v_{f} &= 0 + "+str(g)+"m/s^2 x "+str(format(t,'0.2f'))+"s  = "+ str(format(vf,'0.1f')) +"m/s"\
    "\\end{align*}"\
    "\\)"
    return res

def res_06_28(params):
    v0x = 1
    t = 1
    if(len(params) > 0):
        v0x = float(params[0].res)
        t = float(params[1].res)
    v0y = 0
    g = -9.8
    x = v0x*t
    y = v0y + 1/2 * g * t**2
    res = " \\( "+"\\)"
    res = " \\( \\begin{align*}"\
    "x &= "+str(v0x)+"m/s * "+str(t)+"s = "+ str(x) +" m"\
    "\\\\"\
    "y &= "+str(v0y)+" + \\dfrac{"+str(g)+"m/s^2 * ("+str(t)+"s)^2}{2} = "+ str(format(y,'0.4f')) +"m"\
    "\\end{align*}"\
    "\\)"
    return res

def res_06_37(params):
    v = 1
    angle = 37
    t = 2
    g=-32
    if(len(params) > 0):
        v = float(params[0].res)
        # angle = float(params[1].res)
    # v = 120
    v0x = v * cos(radians(angle))
    v0y = v * sin(radians(angle))

    x = v0x * t
    y = v0y*t + 1/2*g*t**2

    res = " \\( \\begin{align*}"\
    "x &= "+str(v)+"m/s * \\cos("+str(angle)+") * "+str(t)+"s = "+ str(x) +" ft"\
    "\\\\"\
    "y &= "+str(v)+"m/s * \\sin("+str(angle)+") * "+str(t)+"s + \\dfrac{1}{2} * "+str(g)+"m/s^2 * ("+str(t)+"s)^2 = "+ str(format(y,'0.4f')) +" ft"\
    "\\end{align*}"\
    "\\)"
    return res


def res_06_40(params):
    v = 1
    angle = 32
    g = -9.8
    if(len(params) > 0):
        v = float(params[0].res)
    # v=35
    v0y = v * sin(radians(angle))
    vfy = 0

    t = -v0y/g
    y = v0y*t + 1/2*g*t**2
    
    res = " \\( "+"\\)"
    res = " \\( \\begin{align*}"\
    "t &= \\dfrac{-"+str(v0y)+"m/s}{ "+str(g)+"m/s^2} = "+ str(t) +" s"\
    "\\\\"\
    "y &= "+str(v0y)+"m/s * "+str(t)+"s" + "\\dfrac{1}{2}"+str(g)+"m/s^2 * ("+str(t)+"s)^2 = "+ str(format(y,'0.4f')) +"m"\
    "\\end{align*}"\
    "\\)"
    return res
