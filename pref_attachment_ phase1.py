# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:46:18 2022

@author: PSClo
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

params = {
    'font.family' : 'serif',
    'font.size': 13.5,
    'figure.figsize':  [8.8, 8.8/1.618],
    'axes.grid': True,
    'legend.loc' :'best',
    'legend.fontsize': 10,
    'legend.handlelength':2,
    'image.cmap': 'YlGn'

}

plt.rcParams.update(params)

#%%

N = 100
m = 2
G = nx.barabasi_albert_graph(100,1)
nx.draw(G, node_size = 1)

degrees = dict(G.degree())
degree_values = sorted(set(degrees.values()))
histogram  = [list(degrees.values()).count(i)/float(nx.number_of_nodes(G)) for i in degree_values]

plt.figure()
plt.plot(degree_values, histogram, 'x')

#%%

class pref_attach:
    
    def _init_(self):
        self.m = m #no of edges to attach
        self.k = k
        self.n = N #total number of nodes
        self.neighborsN = np.zeros(N) #array of initial nodes

    def add_node(self):
        self.n = self.n + 1

    def no_nodes(self):
        self.n = np.zeros(n)
        
    def BA_model(self):
        
        
        
        
        
            
            
#%% 
k = np.zeros(n)
n = 10
for i in range(10):
    k[i] = 5

print(k)













