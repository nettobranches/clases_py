from sympy import *

x, y, z, t = symbols('x y z t')
k, m, n, a, b = symbols('k m n a b', integer=True)
f, g, h = symbols('f g h', cls=Function)

def calculoMethod(unidad, strMethod, params):
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

    return res
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
    return " \\( "+ str(latex(integrate(x*sqrt(x**2), x))) + "\\)"
def int_var_por_binom_2(params):
    return " \\( "+ str(latex(integrate(x*(1+2*x)**2, x))) + "\\)"
def int_a2x2_over_root(params):
    return " \\( "+ str(latex(integrate(a**2*x**2/sqrt(x**3+a), x))) + "\\)"
def int_binom_over_x(params):
    return " \\( "+ str(latex(integrate((6*x**3-3*sqrt(x))/x, x))) + "\\)"
