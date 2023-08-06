# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 19:40:34 2018

@author: Khera
"""
import numpy as np

class ActivationFunctions():
    
    f = 0
    
    def __init__(self,_f):
        self.f = _f
        
    def Sigmoid(self, x):
        return 1 / (1 + np.exp(-x))   
    
    def DerivedRelu(self, x):
        return 1. * (x > 0)
    
    #essentially x = x
    def Identity(self, x):
        return x
    
    def Arctan(self, x):
        return np.arctan(x)
    
    #Hyperbolic Activation
    #Cosh, Sinh, Tanh
    def Cosh(self, x):
        return np.cosh(x)
    
    def Sinh(self, x):
        return np.sinh(x)
    
    def Tanh(self, x):
        return np.tanh(x)
    
    #Trig style Activation:
    #Sin, Cos, Tan
    
    def Cos(self, x):
        return np.cos(x)
    
    def Sin(self, x):
        return np.sin(x)
    
    def Tan(self, x):
        return np.tan(x)
    
    def ExecuteActivationFunction(self, x):
        
        if self.f == 0:
            return self.Identity(x)
        
        elif self.f == 1:
            return self.Sigmoid(x)
        
        elif self.f == 2:
            return self.DerivedRelu(x)
        
        elif self.f == 3:
            return self.Arctan(x)
        
        elif self.f == 4:
            return self.Cosh(x)
        
        elif self.f == 5:
            return self.Sinh(x)
        
        elif self.f == 6:
            return self.Tanh(x)
        
        elif self.f == 7:
            return self.Cos(x)
        
        elif self.f == 8:
            return self.Sin(x)
        
        elif self.f == 9:
            return self.Tan(x)













