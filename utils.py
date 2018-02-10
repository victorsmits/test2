# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

import math 
from collections import namedtuple

def fact(n):
    if n<0:
        raise ValueError
    if n<2:
        return 1
    else:
        return n*fact(n-1)
    
def roots(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    if a == 0:
        print("veuilliez donner une equaiton du second degré")

    if delta < 0:
        return ("","")

    if delta > 0:
        x1 = float((- b - math.sqrt(delta)) / (2*a))
        x2 = float((- b + math.sqrt(delta)) / (2*a))

        return ("{}","{}".format(x1, x2))

    if delta == 0:
        x1 = (-b - math.sqrt(delta)/(2*a))
        return ("{}".format(x1))

def ff(x):
    return x
def gg(x):
    return x*2

def integrate(function, lower, upper):
    a = lower
    b = upper
    n = 100000  #nbr de pas
    h = (b - a) / n
    result = 0
    for i in range(0,n-1):
        result += h * function(a + h*i)
    return result

if __name__ == '__main__':
    print(fact(5))
    print(roots(2, 2, 0))
    print(integrate(ff, 0, 1))
