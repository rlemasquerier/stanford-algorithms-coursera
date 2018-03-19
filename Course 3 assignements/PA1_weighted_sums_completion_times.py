# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:17:02 2018

@author: Rodolphe

Test Case 1 results:
    
Difference Method: 32780
Ratio Method: 32104

Answers for main case:
Ex1 : 69119377652
Ex2 : 67311454237

"""

def read_input():
    with open('jobs.txt') as f:
        content = f.readlines()
        content = [[int(i) for i in x.strip().split()] for x in content]
        return content
    
def compute_res(liste):
    length_so_far = 0
    res = 0
    for item in liste:
        length_so_far += item[1]
        res += length_so_far * item[0]
        
    return res

if __name__ == '__main__':
    
    inp = read_input()
    n = inp[0][0]
    del inp[0]
    
    #Exerecice 1 : Greedy method is difference
    ordre = sorted(inp,key=lambda x: (x[0]-x[1],x[0]),reverse=True)
    print(compute_res(ordre))
    #Exercice 2 : Greedy method is ratio
    ordre = sorted(inp,key=lambda x: (x[0]/x[1],x[0]),reverse = True)
    print(compute_res(ordre))
    

