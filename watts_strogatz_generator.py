#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:13:20 2020

@author: pablo

Generacion de una red de Watts-Strogratz: Red que tiene en cuenta clusteres de nodos conectados.
Páginas 303-306
La segunda funcion calcula la probabilidade de que, dado un grafo g, dos individuos sean amigos, utilizando para ello
el numero de amigos comunes entre ellos. 
Páginas 309-310
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def watts_strogatz_graph(n,k,alpha,draw=True):
    
    if k<n:
        g = nx.Graph() #Creamos el grafo
        nodes=range(n) #Creamos una lista de tamaño n y asignamos a cada elemento un valor consecutivo de [0,n-1]
       
        for j in range(1,2*k): #Para cada elemento en el rango [1,2*k]
            targets = list(nodes[j:]) + list(nodes[0:j]) #Damos valores para enlazar con el nodo de ese valor
            g.add_edges_from(zip(nodes,targets)) #Añadimos un arco, formando parejas nodo-target
        
        for j in range(1,2*k):
            targets = list(nodes[j:]) + list(nodes[0:j])
            for u,v in zip(nodes,targets): #Para cada combinacion nodo-target 
                if np.random.random() < alpha: #Sorteamos un numero perteneciente a [0,1)
                    w=np.random.choice(nodes)
                    while w==u or g.has_edge(u,w):
                        w=np.random.choice(nodes) #Tomamos un valor aleatorio del listado de nodos
                        if g.degree(u) >= n-1: #Si el nodo ya esta conectado con n-1 vecinos, paramos
                            break
                    else: #Entramos en este else si se da alguna de las condiciones de parada del bucle while!
                        g.remove_edge(u,v)
                        g.add_edge(u,w)
        
        if draw == True:
            plt.figure()
            nx.draw(g,node_size=40)
            plt.title('Watts-Strogatz Graph with '+str(n)+' nodes')
            degrees=[]
            for v in g.nodes():
                degrees.append(g.degree(v))
            plt.figure()
            plt.hist(grades)
            plt.title('Nodal degree distribuction in a Watts-Strogatz graph with '+str(n)+' nodes')
            plt.xlabel('Nodal degree')
            plt.ylabel('Number of nodes')
        
        return g
    else:
        print('Error: Chose k<n')

def friendship_probability(g): #NO FUNCIONAAA
    global comunes
    commons={} #Declaramos un diccionario vacio
    probability={}
    
    degrees=[]
    for v in g.nodes():
                degrees.append(g.degree(v))
    
    for i in range(np.mean(degrees).astype(int)):
        #commons[i]=list([0,0]) #Inicializamos en elemento i-esimo
    visited_couples=[]

    for v in g.nodes:
        v_neighbors=set(g.neighbors(v))
        for w in g.nodes():
            if w!=v and (v,w) not in visited_couples and (w,v) not in visited_couples:
                w_neighbors=set(g.neighbors(w))
                common_friends=len(v_neighbors.intersection(w_neighbors))
                if v in g.neighbors(w):
                    commons[common_friends][0]+=1
                else:
                    commons[common_friends][1]+=1
    
    for i in commons.keys():
        if commons[i][0]+commons[i][1]!=0:
            probability[i]=float(commons[i][0])/(commons[i][0]+commons[i][1])
        else:
            probability[i]=1
    
    plt.plot(probability.values())
    plt.ylabel("Friendship probability")
    plt.xlabel("Number of common friends")
    plt.title("Friendship probability vs Common friends \n") 
    
    return commons,probability

graph=watts_strogatz_graph(1000,5,0.1)
friendship_probability(graph)
      
        
        
        
        
        
            


