# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:24:38 2018

@author: Rodolphe

TestCase1 :
10
37
59
43
27
30
96
96
71
8
76

Min length = 2
Max length = 5

Testcase2 :
15
895
121
188
953
378
849
153
579
144
727
589
301
442
327
930

Min length = 3
Max length = 6

FINAL CASE:
Min = 9
Max = 19

"""

import collections
import heapq

def read_input():
    with open('huffman.txt') as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content if x != '\n']
        return content[1:]  
    
class TreeNode():
    
    def __init__(self, left = None, right = None, max_depth = 0, min_depth = 0):
        
        self.left = left
        self.right = right
        self.max_depth = max_depth
        self.min_depth = min_depth
    
    #This is needed to break the tie in the priority list in case of ties    
    def __lt__(obj1, obj2):
        return True
    
if __name__ == '__main__':
    inp = read_input()
    priority_queue = []
    
    for weight in inp:
        heapq.heappush(priority_queue,(weight,TreeNode()))

    while len(priority_queue) >= 2:
        left_key, node_left = heapq.heappop(priority_queue)
        right_key, node_right = heapq.heappop(priority_queue)
        new_max = 1+max(node_left.max_depth,node_right.max_depth)
        new_min = 1+min(node_left.min_depth,node_right.min_depth)
        heapq.heappush(priority_queue,(left_key+right_key,TreeNode(left = node_left, right = node_right, max_depth = new_max, min_depth = new_min)))
        
    _ , root = heapq.heappop(priority_queue)
    print(root.max_depth, root.min_depth)
    
    
    

