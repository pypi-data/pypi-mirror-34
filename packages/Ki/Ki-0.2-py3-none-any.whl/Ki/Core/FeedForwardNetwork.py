# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:18:40 2018

@author: Khera

Feed Forward Network
"""

from .Neuron import Neuron as Node
from .Connection import Connection as Con
from .ActivationFunctions import ActivationFunctions as Act
import numpy as np
import math

class FeedForwardNetwork():
    
    Layers = []
    Activations = []
    Fitness = 0
    
    def __init__(self, _LayerSizes):
        
        self.Layers = []
        self.Activations = []
        self.CreateNetwork(_LayerSizes)
        self.Fitness = 0
    
    
    def CreateNetwork(self, _LayerSizes):
        
        for i in _LayerSizes:
            self.Activations.append(6)
            Layer = []
            
            for j in range(i):
                N = Node()
                Layer.append(N)
            
            self.Layers.append(Layer)
        self.ConnectLayers()
        
    #connect up all the nodes in the network
    def ConnectLayers(self):
        
        Length = len(self.Layers)
        #print(Length)
                
        for i in range(len(self.Layers)):
            
            if i != len(self.Layers) -1:
                
                for j in self.Layers[i]:
                    
                    for k in self.Layers[i+1]:
                    
                        connection = Con(j,k)
                        j.addOutConnection(connection)
                        k.addInConnection(connection)
                        
    
    #Feed Forward
    def predict(self, _inputs):
        
        #print("Feeding Forward!")
        
        for i in range(len(_inputs)):
            self.Layers[0][i].Value = _inputs[i]
            self.Layers[0][i].ActivatedAdjustedValue = self.Layers[0][i].Value #self.Tanh(self.Layers[0][i].Value+self.Layers[0][i].Bias)
        
        for i in range(1, len(self.Layers)):
            
            af = Act(self.Activations[i])
            
            for j in self.Layers[i]:
                
                nodeValue = 0
                
                for k in j.ConnectionsIn:
                    
                    nodeValue += (np.dot(k.Weight, k.Node1.ActivatedAdjustedValue)) #+ k.Node2.Bias
                
                #print(nodeValue)
                j.Value = nodeValue
                j.ActivatedAdjustedValue = af.ExecuteActivationFunction(j.Value)
                
        outputs = []
        
        for i in self.Layers[len(self.Layers)-1]:
            
            outputs.append(i.Value)
        
        return outputs
                

    def sinh(self, x):
        
        return np.sinh(x)
       
        
    def sigmoid(self, x):
        

        return 1 / (1 + math.exp(-x))   
    
    def Tanh(self, x):
        
        return np.tanh(x)
    
    
#Network = FeedForwardNetwork([1,5,5,10])
#preds = Network.predict([8])
#prediction = np.argmax(preds)

























