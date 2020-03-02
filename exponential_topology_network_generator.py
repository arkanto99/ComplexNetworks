#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:29:27 2020

@author: pablo

Generacion de una red de topologia exponencial (págona 313)

La fundamentacion matematica de este apartado es muy interesante, estando demostrado paso por paso en las paginas 312-313

"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def grafo_exponencial(n): #n->numero de nodos de la red
    
    g=nx.Graph()
    ##Algoritmo de generacion de la red
    v0=g.add_node(0) #Añadimos el nodo inicial a la red
    for i in range (1,n): #No comenzamos en 0 porque hemos fijado 0 como nodo inicial
        a=np.random.randint(i) #Generamos un entero perteneciente a [0,i)
        g.add_node(i) #Añadimos el nodo 'i' a la red
        g.add_edge(i,a) #Añadimos un arco entre el nodo i y el nodo a: Este paso provoque que, a medida que aumente la red, se disperse mas (como es natural), y que los nodos mas antiguos tengan mas conexiones
    #####Representacion del grafo
    plt.figure()
    nx.draw(g,node_size=40)
    plt.title('Grafo exponencial de '+str(n)+' nodos')
    
    #Distribucion nodal del grafo
    grados=[]
    for v in g.nodes(): #Recorremos los nodos del grafo
        grados.append(g.degree(v)) #Guardamos el grado del nodo i de la red en la posicion i del array
    plt.figure()
    plt.hist(grados) #Representamos en un histograma los grados de los nodos del grafo
    plt.xlabel('Grado nodal')
    plt.ylabel('Numero de nodos')
    plt.title('Distribicion del grado nodal')
    
grafo_exponencial(1000)
