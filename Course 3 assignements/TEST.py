# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:35:20 2018

@author: Rodolphe
"""

import heapq

class MyObject():
    
    def __init__(self,a=0,name='toto'):
        
        self.a = a
        self.name = name

if __name__ == '__main__':
    
    priority_list = []
    heapq.heappush(priority_list,(1,'abc'))
    heapq.heappush(priority_list,(1,'abc'))
