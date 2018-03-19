# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:11:37 2018

@author: Rodolphe

8 6
1 1
2 3
5 4
5 2
4 2
1 5
Expected result: 14

200009190 10
10 100001001
20 150001010
25 180001011
21 70000201
15 80000202
30 40000310
36 10000430
27 120000101
19 30000104
7 140000203

Expected result: 112

knapsack1:
2493893
knapsack_big:
4243395

"""

import sys

sys.setrecursionlimit(3000)

def read_input():
    with open('knapsack_big.txt') as f:
        content = f.readlines()
        content = [list(map(int,x.strip().split())) for x in content]
        return (content[0][0],content[0][1],content[1:])
    
def knapsack(inp, M, memo):
    
    if M <= 0:
        memo[len(inp),M] = 0
        return 0
    
    if len(inp) <=0:
        memo[len(inp),M] = 0
        return 0
    
    if M-inp[-1][1] >= 0:
        if (len(inp[:-1]),M-inp[-1][1]) in memo:
            with_n = memo[(len(inp[:-1]),M-inp[-1][1])] + inp[-1][0]
        else:
            with_n = knapsack(inp[:-1], M-inp[-1][1], memo) + inp[-1][0]
    else:
        with_n = -float('inf')
    
    if (len(inp[:-1]),M) in memo:
        without_n = memo[(len(inp[:-1]),M)]
    else:
        without_n = knapsack(inp[:-1], M, memo)
    
    memo[len(inp),M] = max(with_n,without_n)    
    return max(with_n,without_n)
        
if __name__ == '__main__':
    M , n , inp = read_input()
    print(n,M)
    memo = {}
    print(knapsack(inp,M,memo))
    
