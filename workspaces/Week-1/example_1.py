import math

import Phys601.math as phys_math


# measure the runtime for each of these functions

def mult(a,b):
    return a*b

def square(a):
    return a**2

def std_sin(x):
    return math.sin(x)

def custom_sin(x):
    return phys_math.sin(x)

def std_exp(x):
    return math.exp(x)

def custom_exp(x):
    return phys_math.exp(x)


# example calls
a1 = mult(2,3)
a2 = square(3)
a3 = custom_sin(1)
a4 = std_exp(1)
a5 = custom_exp(1)
