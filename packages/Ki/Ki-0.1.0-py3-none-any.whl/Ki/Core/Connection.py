# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:18:28 2018

@author: Khera

Connection between two neurons
"""
import random as r

class Connection():
    
    Node1 = ""
    Node2 = ""
    Weight = 0
    Velocity = 0
    
    def __init__(self, _Node1, _Node2):
        
        self.Node1 = _Node1
        self.Node2 = _Node2
        self.Weight = r.random()
        self.Velocity =  r.uniform(-1,1)
        