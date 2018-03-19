# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:46:37 2018

@author: Rodolphe

Testcase 1 parameter and answer:
t: [3,10]
output : 8

RES final : 427 en 11489 secondes

"""

from multiprocessing.dummy import Pool as ThreadPool 
import time


def read_input():
    with open('2sum.txt') as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content]
        return content
    
def two_sum(A,t):
    targets = set()
    for a in A:
        if t-a in targets and t-a != a:
            return True
        else:
            targets.add(a)
    return False

if __name__ == '__main__':
    
    start_time = time.time()
    L = read_input()
    R = range(-10000,10001)
    res = []
    
#    pool = ThreadPool(4) 
#    res = pool.map(lambda x: two_sum(L,x), R)
    
    for t in R:
        if t%500 == 0:
            print(t)
        res.append(two_sum(L,t))
            
    print(len(list(filter(lambda x:x==True,res))))
    print("--- %s seconds ---" % (time.time() - start_time))
