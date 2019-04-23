from sympy import *
from sympy.parsing.latex import parse_latex
x, y, z, t = symbols('x y z t')
k, m, n, a, b = symbols('k m n a b', integer=True)
f, g, h = symbols('f g h', cls=Function)

def calculoMethod(unidad, strMethod, params, pregunta):
    print("strmethod", strMethod);
    res = ""
    if (strMethod == "int_u_n"):
        res =int_u_n(params)
    elif(strMethod == "int_over_root_binom"):
        res =int_over_root_binom(params)
    elif(strMethod == "int_over_u_n"):
        res =int_over_u_n(params)
    elif(strMethod == "int_u_n_over_root_binom"):
        res =int_u_n_over_root_binom(params)
    elif(strMethod == "int_over_root"):
        res =int_over_root(params)
    elif(strMethod == "int_var_por_root"):
        res =int_var_por_root(params)
    elif(strMethod == "int_var_por_binom_2"):
        res =int_var_por_binom_2(params)
    elif(strMethod == "int_a2x2_over_root"):
        res =int_a2x2_over_root(params)
    elif(strMethod == "int_binom_over_x"):
        res =int_binom_over_x(params)
    elif(strMethod == "integrate"):
        res =integrar(params, pregunta)
    elif(strMethod == "u2_1"):
        res =u2_1(params, pregunta)
    elif(strMethod == "u2_2"):
        res =u2_2(params, pregunta)
    elif(strMethod == "u2_3"):
        res =u2_3(params, pregunta)
    elif(strMethod == "u2_4"):
        res =u2_4(params, pregunta)
    elif(strMethod == "u2_5"):
        res =u2_5(params, pregunta)
    elif(strMethod == "u2_6"):
        res =u2_6(params, pregunta)
    elif(strMethod == "u2_7"):
        res =u2_7(params, pregunta)
    elif(strMethod == "u2_8"):
        res =u2_8(params, pregunta)
    elif(strMethod == "u2_9"):
        res =u2_9(params, pregunta)
    else:
        res =integrar(params, pregunta)
    return res

def u2_1(params, pregunta):
    na = int(params[0].res)
    nb = int(params[1].res)
    return " \\( "+ str(latex(integrate( (nb*x**2)*cos(na*x**3 ), x)))+ "\\)"

def u2_2(params, pregunta):
    na = latex(params[0].res)
    return " \\( "+ str(latex(integrate( sec(na*x)*tan(na*x), x)))+ "\\)"

def u2_3(params, pregunta):
    na = int(params[0].res)
    return " \\( "+ str(latex( -log(cos(exp(x))) ))+ "\\)"

def u2_4(params, pregunta):
    na = int(params[0].res)
    return " \\( "+ str(latex( tan(x)+1/(cos(x)) ))+ "\\)"

def u2_5(params, pregunta):
    return " \\( "+ str(latex((1/-a)*cot(a*x-b)) )+ "\\)"

def u2_6(params, pregunta):
    return " \\( "+ str(latex(integrate( 1/(sqrt(16-x**2)), x)))+ "\\)"

def u2_7(params, pregunta):
    na = int(params[0].res)
    return " \\( "+ str(latex( log(x + sqrt(x**2+na)) ))+ "\\)"

def u2_8(params, pregunta):
    na = int(params[0].res)
    return " \\( "+ str(latex( 4/(2*sqrt(na))*log((x-sqrt(na))/(x+sqrt(na))) ))+ "\\)"
    # return " \\( "+ str(latex( integrate(1/(x**2-25) ) ))+ "\\)"

def u2_9(params, pregunta):
    na = int(params[0].res)
    nb = int(params[1].res)
    # return " \\( "+ str(latex(integrate( na*(cos(x)/sqrt(nb-sin(x)**2)), x)))+ "\\)"
    return " \\( "+ str(latex( asin( cos(x)/sqrt(na))  ))+ "\\)"



def integrar(params, pregunta):
    # print('pregunta', pregunta)

    # f_pregunta = pregunta.replace("\\(", "" )
    # f_pregunta = f_pregunta.replace("\\)", "" )
    # f_pregunta = f_pregunta.replace("\\int", "" )
    # f_pregunta = f_pregunta.replace("dx", "" )
    # print("pregunta", f_pregunta)
    # return " \\( "+ str(latex(integrate( parse_latex(f_pregunta), x ))) + "\\)"
    return " \\( "+ str(latex(integrate( parse_latex(r"x^2"), x ))) + "\\)"
# unidad 1
def int_u_n(params):
    exp = params[0].res
    return " \\( "+ str(latex(integrate(x**exp, x))) + "\\)"

def int_over_root_binom(params):
    num = params[0].res
    return " \\( "+ str(latex(integrate(1/sqrt(num-x), x)))+ "\\)"

def int_over_u_n(params):
    exp = params[0].res
    return " \\( "+ str(latex(integrate(1/x**exp, x))) + "\\)"

def int_u_n_over_root_binom(params):
    num = params[0].res
    return " \\( "+str(latex(integrate( x**2/sqrt(x**3-num) , x))) + "\\)"
def int_over_root(params):
    return " \\( "+ str(latex(integrate(1/sqrt(a*x), x))) + "\\)"
def int_var_por_root(params):
    return " \\( "+ str(latex(integrate(x*sqrt(a*x**2+b), x))) + "\\)"
def int_var_por_binom_2(params):
    return " \\( "+ str(latex(integrate(x*(1+2*x)**2, x))) + "\\)"
def int_a2x2_over_root(params):
    return " \\( "+ str(latex(integrate(a**2*x**2/sqrt(x**3+a), x))) + "\\)"
def int_binom_over_x(params):
    return " \\( "+ str(latex(integrate((6*x**3-3*sqrt(x))/x, x))) + "\\)"
