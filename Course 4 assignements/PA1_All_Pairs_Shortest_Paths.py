# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:48:19 2018

Have been using Floyd marshall algorithm on this one.

@author: Rodolphe

Test case 1:

4 5
1 2 1
1 3 4
2 4 2
3 4 3
4 1 -4

Expected result: negative cycle

Test case 2:

4 5
1 2 1
1 3 4
2 4 2
3 4 3
4 1 -2

Expected result: -2

Exam cases :
Graph 1 : 
Graph 2 :
Graph 3 : 

"""


def read_input():
    with open('g1.txt') as f:
        content = f.readlines()
        content = [list(map(int,x.strip().split())) for x in content]
        return (content[0][0],content[0][1],content[1:])
    
if __name__ == '__main__':
    
    n , m , inp = read_input()
    edges = {}
    
    for tail,head,cost in inp:
        edges[(tail,head)] = cost
    
    A = [[0 for i in range(0,n+1)] for j in range(0,n+1)]
    
    print('creation')
    c =0
    
    for i in range(0,n+1):
        for j in range(0,n+1):
            if c%10000 == 0:
                print(c)
            c += 1
            A[i][j] = [float('inf') for k in range(1,n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                A[i][j][0] = 0
            elif (i,j) in edges:
                A[i][j][0] = edges[(i,j)]
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                A[i][j][k] = min(A[i][j][k-1], A[i][k][k-1]+A[k][j][k-1])
                
    
    for i in range(1,n+1):
        if A[i][i][n] <0:
            print('There is a negative cycle')
            break
        
    print(min([A[i][j][n] for i in range(1,n+1) for j in range(1,n+1)]))
            
    

