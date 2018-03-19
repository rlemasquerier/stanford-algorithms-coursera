# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:23:28 2018

@author: Rodolphe
"""

def integer_multiplication(x,y):
    x = str(x)
    y = str(y)
    n = len(x)
    
    if n == 1:
        return int(x)*int(y)
    
    a = x[:n/2]
    b = x[n/2:]
    c = y[:n/2]
    d = y[n/2:]
    
    z1 = integer_multiplication(int(a),int(c))
    z2 = integer_multiplication(int(b),int(d))
    z3 = integer_multiplication(int(a)+int(b),int(c)+int(d))
    
    #To do

if __name__ == '__main__':