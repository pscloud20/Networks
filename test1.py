# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:48:26 2022

@author: PSClo
"""
import networkx as nx
import test as t
import itertools
import random as rnd
import numpy as np


def k_distrib(graph, scale='lin', colour='#40a6d1', alpha=.8, fit_line=False, expct_lo=1, expct_hi=10, expct_const=1):
    
    plt.close()
    num_nodes = graph.number_of_nodes()
    max_degree = 0
    
    # Calculate the maximum degree to know the range of x-axis
    for n in graph.nodes():
        if graph.degree(n) > max_degree:
            max_degree = graph.degree(n)
    
    # X-axis and y-axis values
    x = []
    y_tmp = []
    
    # Loop over all degrees until the maximum to compute the portion of nodes for that degree
    for i in range(max_degree + 1):
        x.append(i)
        y_tmp.append(0)
        for n in graph.nodes():
            if graph.degree(n) == i:
                y_tmp[i] += 1
        y = [i / num_nodes for i in y_tmp] 
    
    # Check for the lin / log parameter and set axes scale
    if scale == 'log':
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Degree distribution (log-log scale)')
        plt.ylabel('log(P(k))')
        plt.xlabel('log(k)')
        plt.plot(x, y, linewidth = 0, marker = 'o', markersize = 8, color = colour, alpha = alpha)
        
        if fit_line:
            # Add theoretical distribution line k^-3
            # Note that you need to parametrize it manually
            w = [a for a in range(expct_lo,expct_hi)]
            z = []
            for i in w:
                x = (i**-3) * expct_const # set line's length and fit intercept
                z.append(x)

            plt.plot(w, z, 'k-', color='#7f7f7f')
            
    else:
        plt.plot(x, y, linewidth = 0, marker = 'o', markersize = 8, color = colour, alpha = alpha)
        plt.title('Degree distribution (linear scale)')
        plt.ylabel('P(k)')
        plt.xlabel('k')

    plt.show()
    
#%%




def init_BA(N_nodes_init):
    
    n_nodes, nodes = N_nodes_init
    init_BA = nx.empty_graph(n_nodes, 'None')
    if len(nodes) >1:
        if init_BA.nx.is_directed():
            m = itertools.permutations(nodes, 2)
        else:
            m = itertools.permutations(nodes, 2)
        init_BA.add_edges_from(m)
    return init_BA



#%%



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
        
        

#%%
# =============================================================================
# new_N_nodes = t.N_nodes_init
# count = 0 
# G = nx.complete_graph(t.N_nodes_init)    
# =============================================================================
nodes_init = 12
new_N_nodes = nodes_init


def network_create(nodes_init, nodes_final, m):
    
    #N_init = t.N_nodes_init
    G = nx.complete_graph(nodes_init)
    new_N_nodes = nodes_init
    
    new_nodes_count = [nodes_init, nodes_final]
    x = np.diff(new_nodes_count)
    count = 0
    
    for i in range(nodes_final - nodes_init):
        G.add_node(nodes_init + count)
        print((new_N_nodes + count + 1))
        
        count += 1
        for j in range(0,m):
            edge_add_rnd() #built in networkx function to add edge
        new_N_nodes  = new_N_nodes +1
    
    
F = network_create(10,20, 7)   
        
    
    
    