#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:04:06 2020

@author: pablo

Generación de una red de Erdös-Renyi (página 300)
Este tipo de redes surgen cuando, al tener un gran conjunto de nodos y aristas muy grande, enlazamos 2 nodos de manera aleatoria

Este tipo de redes no son realistas, ya que suponen que la conectividad entre los diferrentes nodos siguen una distribucion de Poisson!
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def grados_erdos_renyi(n,m): # n-> Cantidad de nodos ; m->Cantidad de aristas
    
    g=nx.Graph(); #Creamos un grafo vacio
    for i in range (n): #for(i=0;i<n;i++)
        u=g.add_node(i)
    #Algoritmo de generacion de la red###
    for i in range(m):
        a=np.random.randint(n)#Generamos un entero aleatorio del intervali [0,n) , Intervalo Abierto!
        b=np.random.randint(m)
        if a!=b and (a,b) not in g.edges() and (b,a) not in g.edges: #Condiciones para crear un arco en este algoritmo: Que no exista uno ya (son dirigidos) y que no sean los dos nodos el mismo
            g.add_edge(a,b) #Añadimos el arco (a,b)
    ######################Representamos la red
    nx.draw(g,node_size=40)
    plt.title('Grafo Ërdos-Renyi de '+str(n)+' nodos y '+str(m)+' arcos')

grados_erdos_renyi(100,300)
