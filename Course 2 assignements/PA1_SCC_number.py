# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:37:01 2018

@author: Rodolphe


Test case 1 answer : 6,3,2,1,0

"""

import collections

def read_input():
    with open('data_SCC.txt') as f:
        content = f.readlines()
        content = [[int(i) for i in x.strip().split()] for x in content]
        return content     

def DFS_Loop(G,T,passnb=1):  
    
    global s
    
    def DFS(G,node):
        
        global t
        global s
        explored.add(node)
        S[node] = s
        stack = [node]
        ramif = []
        while len(stack)>0:
            current = stack.pop()
            ramif.append(current)
            for child in G[current]:
                if child not in explored:
                    stack.append(child)
                    explored.add(child)
                    S[child] = s
        ramif = ramif[::-1]
        for n in ramif:
            t = t+1
            T[t] = n
               
    explored = set()
    S = collections.defaultdict(int)
    
    if passnb == 1:
        Range = [i for i in range(len(G),0,-1)]
    else:
        Range = [T[i] for i in range(len(G),0,-1)]
    
    for node in Range:
        if node not in explored:
            s = node
            DFS(G,node)
            
    return S

if __name__ == '__main__':
    
    print('Reading input...')
    edges = read_input()
    print('Done')
    
    #Global variables
    #t will store the number of nodes visited so far (for 1st DFS)
    t=0
    #s will store the current leader node (for 2nd DFS)
    s=0
    
    #Build reversed and actual graph
    G = collections.defaultdict(list)
    Grev = collections.defaultdict(list)
    for edge in edges:
        G[edge[0]].append(edge[1])
        G[edge[1]]
        Grev[edge[1]].append(edge[0])
        Grev[edge[0]]
        
    #Build hashtable of finishing times
    T = collections.defaultdict(int)
    
    DFS_Loop(Grev,T)
    S = DFS_Loop(G,T,passnb=2)
    
    Q = collections.defaultdict(int)
    for key,value in S.items():
        Q[value] += 1
        
    res = sorted(list(Q.values()))[::-1][0:5]
        
    print(res)  
    