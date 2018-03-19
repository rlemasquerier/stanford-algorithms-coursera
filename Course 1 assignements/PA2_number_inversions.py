# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:01:14 2018

@author: Rodolphe
"""

def read_input():
    with open('array_number.txt') as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content]
        return content

def merge_and_count(A,B):
    n, m = len(A) , len(B)
    i, j = 0, 0
    C = []
    count = 0
    while 0 <= i < n and 0 <= j <m:
        if B[j] < A[i]:
            count += n - i
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    if i == n:
        C += B[j:]
    else:
        C += A[i:]
        
    return count,C

def sort_and_count_inversions(L):
    if len(L) <= 1:
        return 0,L
    n = len(L)
    a,A = sort_and_count_inversions(L[0:int(n/2)])
    b,B = sort_and_count_inversions(L[int(n/2):])
    c,C = merge_and_count(A,B)
    
    return a+b+c, C

if __name__ == '__main__':
    
    data = read_input()
    print(data)
    result = sort_and_count_inversions(data)
    print('Number of inversions : '+str(result[0]))
    
    