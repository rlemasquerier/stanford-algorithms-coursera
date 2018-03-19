# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 23:35:35 2018

@author: Rodolphe
"""

from random import randint
import copy

def read_input():
    with open('kargerMinCut.txt') as f:
        content = f.readlines()
        content = [[int(i) for i in x.strip().split()] for x in content]
        return content
    
def random_contraction(graph):
    vertices = [k for k in graph]
    while len(vertices) > 2:
        a = vertices[randint(0,len(graph)-1)]
        b = graph[a][randint(0,len(graph[a])-1)]
        graph[a] += graph[b]
        graph[a] = [i for i in graph[a] if i not in [a,b]]
        vertices = [i for i in vertices if i != b]
        for k in graph[b]:
            for i in range(len(graph[k])):
                if graph[k][i] == b:
                    graph[k][i] = a
        graph.pop(b)
    return len(graph[list(graph.keys())[0]])

if __name__ == '__main__':
    
    inp = read_input()
    graph = {l[0] : l[1:] for l in inp}
    current = float('inf')
    N = len(graph)**2
    print('Size of graph : '+str(len(graph))+', performing '+str(N)+' random contractions.')
    for i in range(N):
        if i%100 == 0:
            print('Iteration '+str(i)+' : Minimum so far is '+str(current))
        n = random_contraction(copy.deepcopy(graph))
        if current > n:
            current = n
            current_iter = i
    print('DONE ! Min cut after '+str(i)+' iterations : '+str(current)+' (obtained at iteration '+str(current_iter)+' )')

    