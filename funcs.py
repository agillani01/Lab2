import math 


def f(x):
    f_Function = 7*x**2 + 2*x
    return f_Function 

def g(x,y):
    g_Function = ((x**2 + y**2) / (3*x))
    return g_Function

def hypotenuse(x,y):
    h_Function = math.sqrt(x**2 + y**2)
    return h_Function

def is_positive(a):
    return a>0