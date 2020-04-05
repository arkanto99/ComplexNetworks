#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:24:28 2020

Generacion de una red de Watts-Strogratz: Red en la cual los nodos tiene "popularidad" y a mayor popularidad,
mayor probabilidad de que un nodo se enlace con el

Páginas 314-317
@author: pablo
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def barabasi_albert_graph(r): #Not working
    r=10
    g=nx.Graph()
    v0=g.add_node(0)
    v1=g.add_node(1)
    g.add_edge(v0,v1)
    
    for i in range(2,r):
        g.add_node(i)
        chain_nodes=[]
        for j in g.nodes():
            chain_nodes=chain_nodes + [j for k in range(0,g.degree(j))]
        n=np.random.randint(len(chain_nodes))
        g.add_edge(i,chain_nodes[n])
    
    nx.draw(g,node_size=40)
    plt.title('Barabasi-Albert Graph with '+str(n)+' nodes')
    degrees=[]
    for v in g.nodes():
        degrees.append(g.degree(v))
    plt.figure()
    plt.hist(degrees)
    plt.title('Nodal degree distribuction in a Barabasi-Albert graph with '+str(n)+' nodes')
    plt.xlabel('Nodal degree')
    plt.ylabel('Number of nodes')

barabasi_albert_graph(1000)

range(g.degree(2))
