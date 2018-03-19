# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:14:16 2018

@author: Rodolphe


Expected result for test case 3 (total cost of the Minimum Spanning Tree):
3

Original version 
Clean version on top

"""

import heapq
import copy
import collections

def read_input():
    with open('edges.txt') as f:
        content = f.readlines()
        content = [[int(i) for i in x.strip().split()] for x in content]
        return content
    
def minimum_spanning_tree_cost(graph):
    """Return the sum of the costs of the edges in the minimum spanning
    tree for the given graph, which must be a mapping from nodes to an
    iterable of (neighbour, edge-cost) pairs.

    """
    total = 0                   # Total cost of edges in tree
    explored = set()            # Set of vertices in tree
    start = next(iter(graph))   # Arbitrary starting vertex
    unexplored = [(0, start)]   # Unexplored edges ordered by cost
    while unexplored:
        cost, winner = heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            total += cost
            for neighbour, cost in graph[winner]:
                if neighbour not in explored:
                    heappush(unexplored, (cost, neighbour))
    return total
    
if __name__ == '__main__':
    inp = read_input()
    
    n,m = inp[0][0],inp[0][1]
    del inp[0]
    
    Vertice = collections.namedtuple('Vertice',['key','previous','id'])
    
    vertices = [Vertice(key = 0, previous = None, id = 1)]+[Vertice(key = float('inf'), previous = None, id = i) for i in range(2,n+1)]
    adjacency = {i:[] for i in range(1,n+1)}
    isinQ = {i:True for i in range(1,n+1)}
    A = set()
    visited = set()
    
    for edge in inp:
        adjacency[edge[0]].append((edge[1],edge[2]))
        adjacency[edge[1]].append((edge[0],edge[2]))
    
    total = 0
    Q = copy.deepcopy(vertices)
    heapq.heapify(Q)
    
    while Q:
        u = heapq.heappop(Q)
        if u.id not in visited:
            A.add(u)
            total += u.key
            visited.add(u.id)
            for v,cost in adjacency[u.id]:
                if v not in visited:
                    heapq.heappush(Q,Vertice(key = cost, previous = u.id, id = v))
            
        
    print(total)
    
    
                
        
    
    
