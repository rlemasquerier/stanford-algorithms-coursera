# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:04:56 2018

@author: Rodolphe

Question 10 of exam:
w1=.2,w2=.05,w3=.17,w4=.1,w5=.2,w6=.03,w7=.25

"""

if __name__ == '__main__':
    
    P = [0.2,0.05,0.17,0.1,0.2,0.03,0.25]
    n = len(P)
    A = [[0 for i in range(0,n+1)] for j in range(0,n+1)]
        
    for s in range(0,n):
        for i in range(0,n-s):
            sum_p = sum(P[i:i+s+1])
            mini = float('inf')
            for r in range(i,i+s+1):
                a = A[i][r]+A[r+1][i+s+1]
                if a < mini:
                    mini = a
            A[i][i+s+1] = mini + sum_p
            
    print(A[0][n])