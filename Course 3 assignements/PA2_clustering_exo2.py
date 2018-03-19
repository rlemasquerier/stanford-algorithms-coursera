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

Test case 2 for pb 2:
    6
    
RESULT FOR MAIN EXO 2:
    6118 about 1h

"""

import collections

def read_input():
    with open('clustering_big.txt') as f:
        content = f.readlines()
        content = [ x.strip().replace(' ','') for x in content if x != '\n']
        return content[1:] 
    
    
if __name__ == '__main__':
    
    inp = read_input()
    code_to_cluster = {}
    cluster_to_code = {}
    k = 0
    n = len(inp)
    nbits = 24
    
    print('Step 0')
    for code in inp:
        k += 1
        if k%10000 == 0:
            print(str(k)+'/'+str(n))
        if code not in code_to_cluster:
            code_to_cluster[code] = k
            cluster_to_code[k] = [code]
    
    print('Step 1')
    n = len(code_to_cluster)
    k = 0    
    
    for code in code_to_cluster:
        k+=1
        if k%10000 == 0:
            print(str(k)+'/'+str(n))
        cluster1 = code_to_cluster[code]
        #Generating distances 1 codes
        for i in range(0,nbits):
            newcode = code[:i]+str(1-int(code[i]))+code[i+1:]
            if newcode in code_to_cluster:
                if code_to_cluster[newcode] != cluster1:
                    #move this newcode and its belong to cluster1
                    cluster2 = code_to_cluster[newcode]
                    to_change_cluster = cluster_to_code[cluster2]
                    del cluster_to_code[cluster2]
                    
                    for moving_code in to_change_cluster:
                        code_to_cluster[moving_code] = cluster1
                        cluster_to_code[cluster1].append(moving_code)
     
    print('Step 2')
    n = len(code_to_cluster)
    k = 0  
                   
    for code in code_to_cluster:
        k+=1
        if k%10000 == 0:
            print(str(k)+'/'+str(n))
        cluster1 = code_to_cluster[code]
        #Generating distances 1 codes
        for i in range(0,nbits):
            for j in range(i+1,nbits):
                newcode = code[:i]+str(1-int(code[i]))+code[i+1:j]+str(1-int(code[j]))+code[j+1:]
                if newcode in code_to_cluster:
                    if code_to_cluster[newcode] != cluster1:
                        #move this newcode and its belong to cluster1
                        cluster2 = code_to_cluster[newcode]
                        to_change_cluster = cluster_to_code[cluster2]
                        del cluster_to_code[cluster2]
                        
                        for moving_code in to_change_cluster:
                            code_to_cluster[moving_code] = cluster1
                            cluster_to_code[cluster1].append(moving_code)                        
                            
    print(len(cluster_to_code))

    
 