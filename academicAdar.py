import math
import itertools
import networkx as nx
from networkx.algorithms import bipartite

def criaGrafo(devices):
    grafo = nx.Graph()
    adicionados = []
    #print(devices)
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


def academicAdar(grafo, mac1, mac2):
    node1 = None
    ssids = []
    resultado = 0.0
    if(mac1 == mac2):
        return 'mesmo device'
    lista = list(set(list(grafo.neighbors(mac1))).intersection(list(grafo.neighbors(mac2))))
    if(len(lista) > 0):
        for x in lista:
                resultado += (1/math.log(len(list(grafo.neighbors(x))),2))    
    return resultado

def runTeste(grafo):
    top_nodes = list({n for n, d in grafo.nodes(data=True) if d['bipartite']==1})
    #print(top_nodes)
    #for x in top_nodes:
    #    print(x,grafo.ed
    for x in top_nodes:
        if(len(list(grafo.neighbors(x))) > 1):
            for pair in itertools.combinations(list(grafo.neighbors(x)),2):
                result = academicAdar(grafo,pair[0],pair[1])
                if(result > 0):
                    print('mac1: %s, mac2: %s, similaridade: %f' %(pair[0],pair[1],result))




