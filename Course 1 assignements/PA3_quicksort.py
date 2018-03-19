# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:24:06 2018

@author: Rodolphe
"""

def read_input():
    with open('quick_sort.txt') as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content]
        return content
    
def partition(L,begin,end):
    
    mid = int(begin+(end-begin)/2)
    if L[begin] <= L[mid] <= L[end] or L[end] <= L[mid] <= L[begin]:
        L[begin], L[mid] = L[mid], L[begin]
    elif L[begin] <= L[end] <= L[mid] or L[mid] <= L[end] <= L[begin]:
        L[begin], L[end] = L[end], L[begin]
        
    pivot = begin
    i = begin
    
    for k in range(begin+1,end+1):
        if L[k] < L[pivot]:
            L[i+1], L[k] = L[k], L[i+1]
            i += 1
    L[i], L[pivot] = L[pivot], L[i]
    
    return i

def quicksort(L,begin=0,end=None):
    
    if end is None:
        end = len(L)-1
        
    if begin >= end:
        return 0
    
    pivot = partition(L,begin,end)
    cpt = end-begin
    cpt += quicksort(L,begin,pivot-1)
    cpt += quicksort(L,pivot+1,end)    
    
    return cpt
    
if __name__ == '__main__':
    
    A=read_input()
    
    n = quicksort(A)
    print(A, n)
    
 
    