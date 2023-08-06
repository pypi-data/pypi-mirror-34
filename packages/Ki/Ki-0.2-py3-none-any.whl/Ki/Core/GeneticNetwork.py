# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:10:56 2018

@author: Khera
"""
from .FeedForwardNetwork import FeedForwardNetwork as FFN
import numpy as np
import pandas as pd
import copy
import random as r

class GeneticNetwork():
    
    Population = []
    PopulationSize = 0
    NetworkSize = []
    Best = []
    
    def __init__(self, _PopulationSize, _NetworkSize):
        
        self.Population = []
        self.PopulationSize = _PopulationSize
        self.NetworkSize = _NetworkSize
        self.Best = []
        
        #initialise the starting population
        for i in range(self.PopulationSize):
            
            self.Population.append(FFN(self.NetworkSize))
    
    
    #assess the fitness of a single network
    def AssessNetworkAccuracy(self, NetworkNumber, X, Y):
        
        Network = self.Population[NetworkNumber]
        
        TotalValues = len(Y)
        Accuracy = 0
        
        for i in range(len(Y)):
            #print(i)
            prediction = Network.predict(X[i])
            
            if np.argmax(prediction) == Y[i]:
                #print(np.argmax(prediction))
                Accuracy += 1
        
        Fitness = Accuracy/TotalValues
        Network.Fitness = Fitness
    
    #Assess the entire population
    def AssessPopulation(self, X, Y):
        
        for i in range(len(self.Population)):
            
            self.AssessNetworkAccuracy(i, X, Y)
        
        bestFitness = 0
        popfitness = 0
        
        for i in range(len(self.Population)):
            popfitness += self.Population[i].Fitness
            if self.Population[i].Fitness > bestFitness:
                bestFitness = self.Population[i].Fitness
        
        popfitness = popfitness / self.PopulationSize
        print("Best Fitness = " + str(bestFitness))
        print("Population Fitness = " + str(popfitness))
        
        return bestFitness
    
    #Copy a network
    def CopyNetworkIndex(self, index):
        
        NewNet = copy.deepcopy(self.Population[index])
        NewNet.Fitness = 0
        return NewNet
    
    #Copy a network
    def CopyNetwork(self, Network):
        NewNet = copy.deepcopy(Network)
        NewNet.Fitness = 0
        return NewNet
    
    #crossover style using a the mean of the weights and biases
    def Crossover(self, newNet, Network1, Network2):

        newNet = FFN(self.NetworkSize)
        
        for i in range(len(newNet.Layers)):
            
            if i != len(newNet.Layers):
                
                for j in range(len(newNet.Layers[i])):
                    
                    for k in range(len(newNet.Layers[i][j].ConnectionsIn)):
                        val = r.random()
                        
                        if val <= 0.5:
                        
                            newNet.Layers[i][j].ConnectionsIn[k].Weight = 0+Network1.Layers[i][j].ConnectionsIn[k].Weight
                            
                        else:
                            
                            newNet.Layers[i][j].ConnectionsIn[k].Weight = 0+Network2.Layers[i][j].ConnectionsIn[k].Weight
                                
                    val = r.random()
                    if val <= 0.5:
                        
                        newNet.Layers[i][j] = 0+Network1.Layers[i][j].Bias
                    else:
                        newNet.Layers[i][j] = 0+Network2.Layers[i][j].Bias
                        

                        
    
    #mutate a network
    def Mutate(self, Network):
        
        for i in range(len(Network.Layers)):
            
            if i != len(Network.Layers) -1:
                
                for j in Network.Layers[i]:
                    
                    for k in j.ConnectionsIn:
                        
                        val = r.random()
                        
                        #flip the weight sign
                        if val <= 0:
                            
                            k.Weight *= -1
                        
                        #randomise the weight value
                        elif val <= 0.02:
                            
                            k.Weight = r.random()
                        
                        #increase by a factor
                        elif val <= 0.04:
                            
                            factor = r.random() + 1
                            k.Weight *= factor
                            
                        elif val <=0.08:
                            
                            factor = r.random()
                            k.Weight *= factor
        
                    val = r.random()
                    
                    #flip the weight sign
                    if val <= 0:
                        
                        j.Bias *= -1
                    
                    #randomise the weight value
                    elif val <= 0.02:
                        
                        j.Bias = r.random()
                    
                    #increase by a factor
                    elif val <= 0.04:
                        
                        factor = r.random() + 1
                        j.Bias *= factor
                        
                    elif val <=0.08:
                        
                        factor = r.random()
                        j.Bias *= factor
                            
    #do the entire GA process
    def Fit(self, X, Y, NumIterations, Custom=False, Function=AssessPopulation):
        
        for i in range(NumIterations):
            
            #assess the networks
            if Custom == False:
                self.Function(X, Y)
            else:
                Function(self, X, Y)
            
            #sort the population in fitness order
            for j in range(len(self.Population)):
                
                for k in range(j+1, len(self.Population)):
                    
                    if self.Population[j].Fitness < self.Population[k].Fitness:
                        
                        net = self.Population[j]
                        self.Population[j] = self.Population[k]
                        self.Population[k] = net
            
            #store the best two in the bests array
            self.Best = []
            self.Best.append(self.Population[1])
            self.Best.append(self.Population[0])
            
            #Create a new Population
            NewPopulation = []
            NewPopulation.append(self.Population[1])
            NewPopulation.append(self.Population[0])
            
            for i in range(self.PopulationSize - 2):
                
                operation = r.random()
                
                if operation <=0.25:
                    
                    net = r.randrange(0,self.PopulationSize/2)
                    newNet = self.CopyNetworkIndex(net)
                    self.Mutate(newNet)
                    NewPopulation.append(newNet)
                
                elif operation <= 0.75:
                    
                    net1 = int(r.randrange(0,self.PopulationSize/2))
                    net2 = int(r.randrange(0,self.PopulationSize/2))
                    net3 = FFN(self.NetworkSize)
                    self.Crossover(net3, self.Population[net1], self.Population[net2])
                    NewPopulation.append(net3)
                    
                elif operation <= 0.9:
                    net1 = int(r.randrange(0,self.PopulationSize/2))
                    net2 = int(r.randrange(0,self.PopulationSize/2))
                    net3 = FFN(self.NetworkSize)
                    self.Crossover(net3, self.Population[net1], self.Population[net2])
                    self.Mutate(net3)
                    NewPopulation.append(net3)
                else: 
                    #print(self.NetworkSize)
                    NewPopulation.append(FFN(self.NetworkSize))
            
            self.Population = NewPopulation
