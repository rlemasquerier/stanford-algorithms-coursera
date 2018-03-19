# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:02:26 2018

@author: Rodolphe

Test case for Problem 1:
Expected result:
For K = 2 --> 5
For K = 3 --> 2
For K = 4 --> 1

Final case for pb 1:
106

Test case for Problem 2:
Expected result: 2



"""

import collections

def read_input():
    with open('clustering1.txt') as f:
        content = f.readlines()
        content = [[int(i) for i in x.strip().split()] for x in content]
        return content 
    
def union(cluster,clusters_sizes,vertice1,vertice2):
    if clusters_sizes[cluster[vertice1]] >= clusters_sizes[cluster[vertice2]]:
        leader = vertice1
        joiner = vertice2
    else:
        leader = vertice2
        joiner = vertice1
    new_size = clusters_sizes[cluster[vertice1]]+clusters_sizes[cluster[vertice2]]
    del clusters_sizes[cluster[joiner]]
    clusters_sizes[cluster[leader]] = new_size
    changing_cluster = cluster[joiner]
    for elem in cluster:
        if cluster[elem] == changing_cluster:
            cluster[elem] = cluster[leader]
    
if __name__ == '__main__':
    inp = read_input()
    n = inp[0][0]
    del inp[0]
    k = 4

    Edge = collections.namedtuple('Edge',['dep','to','cost'])
    
    edges = [Edge(dep = node1, to = node2, cost = cost) for (node1,node2,cost) in inp]
    cluster = {i:i for i in range(1,n+1)}
    clusters_sizes = {i:1 for i in range(1,n+1)}
    clusters_nb = n
    
    edges.sort(key = lambda x:x.cost)
    
    for edge in edges:
        if cluster[edge.dep] != cluster[edge.to]:
            if clusters_nb <= k:
                max_spacing_edge = edge
                break
            clusters_nb -= 1
            union(cluster,clusters_sizes,edge.dep,edge.to)

    print(max_spacing_edge.cost)
 