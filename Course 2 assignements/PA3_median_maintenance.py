# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 22:56:00 2018

@author: Rodolphe


Testcase 1 output (sum of medians modulo 10000):
142

Testcase 2 output (sum of medians modulo 10000):
9335

"""

import heapq

def read_input():
    with open('median.txt') as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content]
        return content 
    
if __name__ == '__main__':
    inp = read_input()
    
    #initialisation
    running_median = [inp[0],min(inp[0],inp[1])]
    
    #Convention : the median is the max of min heap 
    
    minheap = [-min(inp[0],inp[1])]
    maxheap = [max(inp[0],inp[1])]
    
    for n in inp[2:]:
        if n <= maxheap[0]:
            heapq.heappush(minheap,-n)
        else:
            heapq.heappush(maxheap,n)
            
        if len(minheap) > len(maxheap)+1:
            to_move = -heapq.heappop(minheap)
            heapq.heappush(maxheap,to_move)
        elif len(maxheap) > len(minheap):
            to_move = heapq.heappop(maxheap)
            heapq.heappush(minheap,-to_move)
            
        running_median.append(-minheap[0])
    
    print(inp)    
    print(running_median)
    print('Answer for the exercice is : '+str(sum(running_median)%10000))
    