# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:33:39 2018

@author: Rodolphe

Testcase1
Max sum: 2616
Chosen points (position): [2, 4, 6, 8, 10]

Testcase2
Max sum: 2533
Chosen points (position): [1, 3, 6, 9]


"""

def read_input():
    with open('mwis.txt') as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content if x != '\n']
        return content[1:] 
    
if __name__ == '__main__':
    inp = read_input()
    A = [0,inp[0]]
    
    for i in range(1,len(inp)):
        if A[i] > A[i-1]+inp[i]:
            A.append(A[i])
        else:
            A.append(A[i-1]+inp[i])
    
    B = []        
    j = len(A)-1
    while j >= 1:
        if A[j] > A[j-1]:
            B.append(j)
            j -= 2
        else:
            j -= 1
    
#    print(inp)
#    print(A)        
#    print(B,A[-1])
            
    print([b for b in B if b in {1, 2, 3, 4, 17, 117, 517, 997}])
            
            
        
