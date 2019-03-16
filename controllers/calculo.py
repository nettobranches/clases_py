from sympy import *

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

def getMethod(strMethod, params):
    print("strmethod", strMethod);
    res = ""
    if (strMethod == "int_u_n"):
        res =int_u_n(params)
    elif(strMethod == "int_u_n"):
        res =int_u_n(params)

    return res

def int_u_n(params):

    print(params[0])
    exp = params[0].res
    return str(latex(integrate(x**exp, x)))

# def int_over_root_binom(params):
#     return str(latex(integrate(1/sqrt(2-x), x)))
#
# def int_over_root_binom(params):
#     return str(latex(integrate(1/sqrt(2-x), x)))
#
# def int_over_root_binom(params):
#     return str(latex(integrate(1/sqrt(2-x), x)))
#
# def int_over_root_binom(params):
#     return str(latex(integrate(1/sqrt(2-x), x)))
#
# def int_over_root_binom(params):
#     return str(latex(integrate(1/sqrt(2-x), x)))
