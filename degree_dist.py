# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:14:31 2022

@author: PSClo
"""

import networkx as nx
import itertools
import random as rnd
import numpy as np
from tqdm import tqdm 
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import os
import shutil
import pandas as pd
import glob

data_dest = '/Data'
params = {
    'font.family' : 'serif',
    'font.size': 13.5,
    'figure.figsize':  [8.8, 8.8/1.618]
    
    
}
data_dest = os.getcwd() + '\Data'
plt.rcParams.update(params)

outputdir = ' /DATA/kdist/'

def degree_dist(G, plot):
    plt.close()
    max_k = 0
    
    
    for i in G.nodes():
        if G.degree(i) > max_k:
            max_k = G.degree(i)
            
    kvals = []
    k_probvals = []
            
    for i in range(max_k +1):
        kvals.append(i)
        k_probvals.append(0)
        
        for j in G.nodes():
            if G.degree(j) == i:
                k_probvals[i] += 1 #need square brackets as o/w not iterable
        prob = [i/G.number_of_nodes() for i in k_probvals]
        
    kdist_data_filename = 'k_vs_kprob_{}'.format(nodes_final)
    kdist_data = np.column_stack((kvals, prob))
        
    np.savetxt(kdist_data_filename + '.txt', kdist_data, delimiter = ',', header = 'k,kprob',footer = 'N = {}'.format(nodes_final), comments = '')
    
    
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            shutil.copy(file, data_dest)   
            
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            os.remove(file)
            
    if plot == True:
        
        plt.plot(kvals, prob, 'o', color = 'red', label = 'Degree Distribution', markersize = 5, alpha = 0.5)
        plt.title('Degree Distribution (Total Nodes = {})'.format(nodes_final))
        #plt.scatter(kvals, prob, c=prob, cmap = cm.plasma_r, label = 'Degree Distribution')
        plt.xlabel('Degree $k$')
        plt.ylabel('Degree Probability $p_{k}$')
        #plt.grid()
        plt.legend()
        plt.show()
        
    else:
        pass

    
degree_dist(G, plot = True)

x= glob.glob(data_dest + "/*.txt") 

df_N_100 = pd.read_csv(data_dest + '\k_vs_kprob_100.txt', delimiter = ',',skipfooter =1, engine = 'python' )
df_N_250 = pd.read_csv(data_dest + '\k_vs_kprob_250.txt', delimiter = ',',skipfooter =1, engine = 'python' )
df_N_1000 = pd.read_csv(data_dest + '\k_vs_kprob_1000.txt', delimiter = ',',skipfooter =1, engine = 'python' )
df_N_10000 = pd.read_csv(data_dest + '\k_vs_kprob_10000.txt', delimiter = ',',skipfooter =1, engine = 'python' )
#%%
l = [pd.read_csv(filename,  delimiter = ',') for filename in glob.glob(data_dest + "/*.txt")]
df = pd.concat(l, axis=0)

