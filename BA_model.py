# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:48:26 2022

@author: PSClo
"""
import networkx as nx
import itertools
import random as rnd
import numpy as np
from tqdm import tqdm 
from time import sleep
import matplotlib.pyplot as plt
import sys

sys.getrecursionlimit()

nodes_init = 1
nodes_final = 250
new_N_nodes = nodes_init
m = 2
G = nx.complete_graph(nodes_init)
new_N_nodes = nodes_init
count= 0 
show_network = False


"""
BA model with 2 functions

prob_node()
    1. Defines the probability that each edge attached to exisitng node
    2. Picks random node
    
edge_add_rnd()
    1. adds an edge to existing vertex 
"""
def prob_node():
    
     #labelling the Model as G is common as seen in python/networkx file on BB
    edges_tot = len(G.edges)
    nds_prob = []
    
    for n in G.nodes:
        k = G.degree(n)
        
        #From master equation slide in lecture slides p.191
        Pi = k/(2* edges_tot) #Pi is 
        nds_prob.append(Pi) #Add values of each Pi(n(k,t)) to probability list
        
        #One requirement is to choose entry at random from existing edges which is already
    rnd_Pi_choice = np.random.choice(G.nodes(), p =nds_prob)
    return rnd_Pi_choice

def edge_add_rnd():
    
    if len(G.edges()) == 0 :
        rnd_Pi_choice = 0
    else:
        rnd_Pi_choice = prob_node()
    edge_new = (rnd_Pi_choice, new_N_nodes)
    if edge_new in G.edges():
        edge_add_rnd()
    else:
        G.add_edge(new_N_nodes, rnd_Pi_choice)
        #print("edge added: {} {}".format(new_N_nodes+1, rnd_Pi_choice))


#Iterative program 

for i in tqdm(range(nodes_final - nodes_init)):
    sleep(0.01)
    

    for i in range(1):
            G.add_node(nodes_init + count)
        #print((new_N_nodes + count + 1))
        
            count += 1
            for j in range(0,m):
                edge_add_rnd() #built in networkx function to add edge
                new_N_nodes  = new_N_nodes +1
                

if show_network == True:
    plt.figure()
    nx.draw(G, edge_color = 'grey', node_color = 'blue', node_size=50)
    plt.title('Total number of nodes = {}'.format(nx.number_of_nodes(G)))
else:
    pass
        
print('Total number of nodes = {}'.format(nx.number_of_nodes(G)))
print('Total number of edges = {}'.format(nx.number_of_edges(G)))






#%% 
"""
Function to create network for ease of use when running program

However reach recursion limit as python doesnt allow a function to be called more than the limit
Best to write iterative program (above) to avoid this

 
def graph_create(nodes_init, nodes_final, new_N_nodes, m, count = count):
    for i in tqdm(range(nodes_final - nodes_init)):
        sleep(0.01)
    

        for i in range(1):
                G.add_node(nodes_init + count)
        #print((new_N_nodes + count + 1))
        
                count += 1
                for j in range(0,m):
                    edge_add_rnd() #built in networkx function to add edge
                    new_N_nodes  = new_N_nodes +1
                    
graph_create(nodes_init, nodes_final, new_N_nodes, m)
    
"""
