# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:39:50 2018

@author: Rodolphe

Test case 1 answer:

output:

1 0 []
2 1 [2]
3 2 [2, 3]
4 3 [2, 3, 4]
5 4 [2, 3, 4, 5]
6 4 [8, 7, 6]
7 3 [8, 7]
8 2 [8]

"""

import collections
import copy
import heapq

def read_input():
    with open('dijkstra_data.txt') as f:
        content = f.readlines()
        content = [[s for s in x.strip().split()] for x in content]
        return content 
    
def initialize_single_source(vertices,source):
    vertices[source] = Vertex(estimate = 0, predecessor = None)
    
def relax(vertices,vertexUid,edge,Q):
    vertexV = vertices[edge.destination]
    vertexU = vertices[vertexUid]
    if vertexV.estimate > vertexU.estimate + edge.length:
        vertices[edge.destination] = Vertex(estimate = vertexU.estimate + edge.length, predecessor = vertexUid)
        heapq.heappush(Q,(vertexU.estimate + edge.length,edge.destination))
        
def extract_min(Q,S):
     c = heapq.heappop(Q)
     if c[1] in S:
         c = extract_min(Q,S)

     return c

if __name__ == '__main__':
    
    inp = read_input()
    
    Edge = collections.namedtuple('Edge',['destination','length'])
    Vertex = collections.namedtuple('Vertex',['estimate','predecessor'])
    
    graph = collections.defaultdict(list)
    vertices = {}
    for elem in inp:
        graph[int(elem[0])]
        vertices[int(elem[0])] = Vertex(estimate = float('inf'), predecessor = None)
        for string in elem[1:]:
            graph[int(elem[0])].append(Edge(destination = int(string[:string.index(',')]), length = int(string[string.index(',')+1:])))
    
    initialize_single_source(vertices,1)
    S = {}
    Q = [(vertex.estimate,vertexid) for vertexid,vertex in vertices.items()]
    heapq.heapify(Q)
    while len(S) < len(vertices):
        c = extract_min(Q,S)
        cost,  vertexUid = c
        S[vertexUid] = cost
        for edge in graph[vertexUid]:
            relax(vertices,vertexUid,edge,Q)            
         
    print(S[7],S[37],S[59],S[82],S[99],S[115],S[133],S[165],S[188],S[197])
      
            
            