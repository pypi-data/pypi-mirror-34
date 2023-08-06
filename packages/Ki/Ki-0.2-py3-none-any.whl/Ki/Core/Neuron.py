# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:09:59 2018

@author: Khera

Neurons of a network
"""

import random as r

class Neuron():
    
    ConnectionsIn = []
    ConnectionsOut = []
    Bias = 0
    Value = 0
    ActivatedAdjustedValue = 0
    
    def __init__(self):
        
        self.ConnectionsIn = []
        self.ConnectionsOut = []
        self.Bias = r.random()
        self.Value = 0
        self.ActivatedAdjustedValue = 0
        
    #add a new connection to the network
    def addInConnection(self, connection):
        
        self.ConnectionsIn.append(connection)
        
    #add a new connection to the network
    def addOutConnection(self, connection):
        
        self.ConnectionsOut.append(connection)
        
        
        
        
        
        
        