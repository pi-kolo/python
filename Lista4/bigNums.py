from cmath import exp
from math import pi
import numpy as np
import random

import time

"""
FastBigNum v1 - wykładowa
"""
def omega(k,n):
    return exp(-2j*k*pi/n)

def dft(x,n):
    return [sum(x[i]*omega(i*k,n) if i<len(x) else 0 for i in range(n)) for k in range(n)]

def idft(x,n):
    return [int(round(sum(x[i]*omega(-i*k,n) if i<len(x) else 0 for i in range(n)).real)/n) for k in range(n)]

class FastBigNum:

    def __init__(self, string_number):
        self.number = string_number
        self.n = len(string_number)
    
    def __str__(self):
        return self.number

    def __mul__(self, other):
        x_ast = dft(list(map(int, list(''.join([self.number, self.n*'0'])))), 2*self.n)
        y_ast = dft(list(map(int, list(''.join([other.number, other.n*'0'])))), 2*other.n)
        z_ast = [x_ast[i]*y_ast[i] for i in range(2*self.n)]
        result = idft(z_ast, 2*self.n)
        result = result[:-1]
        r2 = 0
        for i, el in enumerate(result[::-1]):
            r2 += el * 10**i
        return FastBigNum(str(r2))

"""
FastBigNum v2 - z numpy
"""
class FastBigNumNUMPY:

    def __init__(self, string_number):
        self.number = string_number
        self.n = len(string_number)
    
    def __str__(self):
        return self.number

    def __mul__(self, other):
        x_ast = np.fft.fft(list(map(int, list(''.join([self.number, self.n*'0'])))))
        y_ast = np.fft.fft(list(map(int, list(''.join([other.number, other.n*'0'])))))
        z_ast = x_ast * y_ast
        result = np.fft.ifft(z_ast)
        result = list(map(int, list(map(round, result))))
        result = result[:-1]
        r2 = 0
        for i, el in enumerate(result[::-1]):
            r2 += el * 10**i
        return FastBigNumNUMPY(str(r2))

"""
FastBigNum v3 - własna implementacja fft
"""
def my_fft(x):
    pass
    # N = len(x)
    # if N <= 1: return x
    # even = my_fft(x[0::2])
    # odd =  my_fft(x[1::2])
    # T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    # return [even[k] + T[k] for k in range(N//2)] + \
    #        [even[k] - T[k] for k in range(N//2)]


# class FastBigNumMy:

#     def __init__(self, string_number):
#         self.number = string_number
#         self.n = len(string_number)
    
#     def __str__(self):
#         return self.number

#     def __mul__(self, other):
#         x_ast = my_fft(list(map(int, list(''.join([self.number, self.n*'0'])))))
#         y_ast = my_fft(list(map(int, list(''.join([other.number, other.n*'0'])))))
#         z_ast = [x_ast[i]*y_ast[i] for i in range(2*self.n)]
#         result = idft(z_ast, 2*self.n)
#         result = result[:-1]
#         r2 = 0
#         for i, el in enumerate(result[::-1]):
#             r2 += el * 10**i
#         return FastBigNumMy(str(r2))


ns = [1000, 5000, 10000]

for n in ns:
    a = ''.join([random.choice("0123456789") for i in range(n)])
    b = ''.join([random.choice("0123456789") for i in range(n)]) 

    A = FastBigNumNUMPY(a)
    B = FastBigNumNUMPY(b)
    
    c = A*B
    if c.number != str(int(a)*int(b)):
        print("ERROR")
    else:
        print("done")

# A = '1312312231232131231231231231231231212331233231349'
# B = '1212312311223123121312312321321231231112323123231'

# a = FastBigNumNUMPY(A)
# b = FastBigNumNUMPY(B)

# z = a*b
# z2 =a*b

# print(z*z2)
