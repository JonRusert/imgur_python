import os
from networkx import *
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def acquireNodes(directory):
    nodes = {}
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            curFile = open(subdir + '/' +file, 'r')
            #iterate through line by line to retrieve usernames from files to be used as nodes
            for line in curFile:
                line = line.replace(',', ' ')
                line = line.split()
                for i in range(len(line)):
                    if line[i] not in nodes:
                        nodes[line[i]] = []
                    if i > 0:
                        #some users reply to their own comments, no need to link to self
                        #if not equal and not already in, append to first on line to create edge
                        if line[i] != line[0] and line[i] not in nodes[line[0]]:
                            nodes[line[0]].append(line[i])

            curFile.close()
                        
    return nodes

def createDirectedGraph(nodes):
    G = DiGraph()
    
    #iterate through nodes and add each key as a node
    for node in nodes:
        G.add_node(node)

    #iterate through nodes again adding directed from the replying node to the original
    for node in nodes:
        edges = nodes[node]
        for edge in edges:
            G.add_edge(edge, node)

    return G
        
    
G = createDirectedGraph(acquireNodes('../nodes'))
#pos = spring_layout(G)
#draw(G, pos)
#plt.savefig("NormalImgurGraph.png", format="PNG")
