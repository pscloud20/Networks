# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:14:31 2022

@author: PSClo
"""

N_nodes_init = 10 #Number of nodes in initial network 
N_nodes_total = 20 #Number of total nodes
m = 5 #Number of edges

#%%

def BA_graph(n,m,seed = None):
    
    if m < 1 or  m >=n:
            raise nx.NetworkXError(\
              "Barabási-Albert network must have m>=1 and m<n, m=%d,n=%d"%(m,n))
    if seed is not None:
        random.seed(seed)

    # Add m initial nodes (m0 in barabasi-speak)
        G=empty_graph(m)
        G.name="barabasi_albert_graph(%s,%s)"%(n,m)
        # Target nodes for new edges
        targets=list(range(m))
        # List of existing nodes, with nodes repeated once for each adjacent edge
        repeated_nodes=[]
        # Start adding the other n-m nodes. The first node is m.
        source=m
        while source<n:
            # Add edges to m nodes from the source.
            G.add_edges_from(zip([source]*m,targets))
            # Add one node to the list for each new edge just created.
            repeated_nodes.extend(targets)
            # And the new node "source" has m edges to add to the list.
            repeated_nodes.extend([source]*m)
            # Now choose m unique nodes from the existing nodes
            # Pick uniformly from repeated_nodes (preferential attachement)
            targets = _random_subset(repeated_nodes,m)
            source += 1
            return G
        
G = BA_graph(100,1)
nx.draw()