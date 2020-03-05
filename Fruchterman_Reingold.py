#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:21:20 2020

@author: pablo

Resultado del algoritmo de Fruchterman-Reingold (algoritmo de fuerzas dirigidas para la visualización de grafos)
implementado en NetworkX sobre el grafo de Les Miserables
Página 296-297
"""

import networkx as nx
#import matplotlib.pyplot as plt #Solo es necesaria importarla si queremos guardar la imagen resultado

g=nx.read_graphml('./Datasets/miserables.graphml') #Leemos el dataset

pos=nx.spring_layout(g) #Ejecutamos el algortimo de Fruchterman (es una variante del algortimo spring embeder, de ahí el nombre de la función)
color_nodes={} #Creamos los arrays para contener los colores y las etiquetas de los nodos
labels_nodes={}
for i in g.nodes():#Recorremos todos los nodos del algoritmos
    labels_nodes[i]=g.nodes[i]['name'] #Usamos como parametro para las etiquetas el nombre de cada nidi, recogido en el dataset
    if g.nodes[i]['name']=='JV':
        color_nodes[i]='b'
    else:
        color_nodes[i]='r'

nx.draw(g,pos=pos) #Dibujamos el grafo con sus aristas, tomando como datos el dataset, y como posición la generada por el algoritmo
nx.draw_networkx_nodes(g,pos,node_color=color_nodes.values())#Añadimos los colores de los nodos
nx.draw_networkx_labels(g,pos,labels=labels_nodes)#Añadimos las etiquetas de los nodos


#Opciones para guardar la imagen
#plt.axis('off')
#plt.savefig('lesmiserablesnet.png',dpi=350)
#plt.show()
