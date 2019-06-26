import math
import itertools
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import random

def criaGrafo(devices):
    grafo = nx.Graph()
    for mac in devices.keys():
        if(len(devices[mac]['pnl']) > 0):
            grafo.add_node(mac, bipartite=0)
            for ssid in devices[mac]['pnl']:
                ssid = ssid.split('_')[1]
                if(ssid in grafo):
                    grafo.add_edge(ssid,mac)
                else:
                    grafo.add_node(ssid, bipartite=1)
                    grafo.add_edge(ssid,mac)   
    return grafo


def adamicAdar(grafo, mac1, mac2):
    resultado = 0.0
    if(mac1 == mac2):
        return 'mesmo device'
    lista = list(set(list(grafo.neighbors(mac1))).intersection(list(grafo.neighbors(mac2))))
    if(len(lista) > 0):
        for x in lista:
            resultado += (1/math.log(len(list(grafo.neighbors(x))),2))    
    return resultado

def geraSimilaridade(grafo):
    top_nodes = list({n for n, d in grafo.nodes(data=True) if d['bipartite']==1})
    file = open('graph.csv', 'w')
    file.write('mac1;mac2;similaridade\n')
    for x in top_nodes:
        if(len(list(grafo.neighbors(x))) > 1):
            for pair in itertools.combinations(list(grafo.neighbors(x)),2):
                result = adamicAdar(grafo,pair[0],pair[1])
                if(result >= 0.3):
                    file.write('%s;%s;%f\n' % (pair[0],pair[1],result))
    file.close()

def plot():
    H = nx.read_edgelist(path="grid.edgelist", delimiter=",")
    nx.draw(H)
    plt.show()

def plotG(G):
    C = nx.connected_component_subgraphs(G)
    for g in C:
         node_colors = [random.random()] * nx.number_of_nodes(g)
         nx.draw(g, None, node_size=4, node_color=node_colors, vmin=0.0, vmax=1.0, with_labels=False )
    plt.savefig('destination_path.pdf', format='pdf', dpi=1200)




