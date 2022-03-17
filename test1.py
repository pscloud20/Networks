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
        

def prob_node():
    
    G = nx.complete_graph(t.N_nodes_init) #labelling the Model as G is common as seen in python/networkx file on BB
    edges_tot = len(G.edges)
    nds_prob = np.zeros(len(ed_tot))
    
    for n in G.nodes:
        k = G.degree(n)
        
        #From master equation slide in lecture slides p.191
        Pi = k/(2* edges_tot) #Pi is 
        nds_prob.append(Pi) #Add values of each Pi(n(k,t)) to probability list
        
        #One requirement is to choose entry at random from existing edges which is already
        rnd_Pi_choice = rnd.choice(G.nodes(), nds_prob)
    return rnd_Pi_choice

def edge_add():

#%%
new_N_nodes = t.N_nodes_init
count = 0 
G = nx.complete_graph(t.N_nodes_init)    

def network_create(N_init, N_final):
    
    #N_init = t.N_nodes_init
    G = nx.complete_graph(N_init)
    new_N_nodes = N_init
    
    new_nodes_count = [N_init, t.N_nodes_total]
    x = np.diff(new_nodes_count)
    count = 0
    
    for i in range(N_final - N_init):
        G.add_node(N_init + count)
        
        count += 1
        for j in range(0,m):
            G.add_edge(N_init, N_final) #built in networkx function to add edge
        new_N_nodes  = new_N_nodes +1
    
    
network_create(t.N_nodes_init, t.N_nodes_total)   
        
    
    #for i in G.nodes
    
#%%
# =============================================================================
# def rand_prob_node():
#     nodes_probs = []
#     for node in G.nodes():
#         node_degr = G.degree(node)
#         #print(node_degr)
#         node_proba = node_degr / (2 * len(G.edges()))
#         #print("Node proba is: {}".format(node_proba))
#         nodes_probs.append(node_proba)
#         #print("Nodes probablities: {}".format(nodes_probs))
#     random_proba_node = np.random.choice(G.nodes(),p=nodes_probs)
#     #print("Randomly selected node is: {}".format(random_proba_node))
#     return random_proba_node
# 
# def add_edge():
#         if len(G.edges()) == 0:
#             random_proba_node = 0
#         else:
#             random_proba_node = rand_prob_node()
#         new_edge = (random_proba_node, new_node)
#         if new_edge in G.edges():
#             print("!ככה לא בונים חומה")
#             add_edge()
#         else:
#             print("!מזל טוב")
#             G.add_edge(new_node, random_proba_node)
#             print("Edge added: {} {}".format(new_node + 1, random_proba_node))
# =============================================================================
            
#%%

# =============================================================================
# print("***\nWelcome to Barabási–Albert (BA) model simulation\nAuthor: Aleksander Molak (2017)\n!איזה כיף\n\n")
# 
# # Get parameters
# init_nodes = int(input("Please type in the initial number of nodes (m_0): "))
# final_nodes = int(input("\nPlease type in the final number of nodes: "))
# m_parameter = int(input("\nPlease type in the value of m parameter (m<=m_0): "))
# 
# print("\n")
# print("Creating initial graph...")
# 
# G = nx.complete_graph(init_nodes)
# 
# print("Graph created. Number of nodes: {}".format(len(G.nodes())))
# print("Adding nodes...")
# 
# count = 0
# new_node = init_nodes
# 
# for f in range(final_nodes - init_nodes):
#     print("----------> Step {} <----------".format(count))
#     G.add_node(init_nodes + count)
#     print("Node added: {}".format(init_nodes + count + 1))
#     count += 1
#     for e in range(0, m_parameter):
#         add_edge()
#     new_node += 1
# 
# 
# print("\nFinal number of nodes ({}) reached".format(len(G.nodes())))
# =============================================================================
