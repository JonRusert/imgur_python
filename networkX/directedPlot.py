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
        

def analyzeGraph(graph):
    out = open("directedGraphOut", 'w')
    out.write("Number of nodes:" + str(number_of_nodes(graph)) + "\n")
    out.write("Number of edges:" + str(number_of_edges(graph)) + "\n")
    out.write("Average clustering coefficient of graph:" + str(average_clustering(graph)) + "\n")
    out.write("Diameter of graph:" + str(diameter(graph)) + "\n")
    out.close()

G = createDirectedGraph(acquireNodes('../nodes'))
#analyzeGraph(G)
pos = random_layout(G)
draw_networkx_nodes(G, pos, node_size=0.1)
draw_networkx_edges(G,pos)
outPut = 'DirectedGraphPlots/DirectedImgurGraph.png'
plt.savefig(outPut, dpi=1000)
    

'''for i in range(0, 50, 5):
    if i == 0:
        count = 1
    else:
        count = i
        
    curN = '../graphNodes/' + str(count) + '/'
    G = createDirectedGraph(acquireNodes(curN))
    #analyzeGraph(G)
    pos = random_layout(G)
    draw_networkx_nodes(G, pos, node_size=0.1)
    draw_networkx_edges(G,pos)
    
    outPut = 'DirectedGraphPlots/DirectedImgurGraph' + str(count) + '.png'
    plt.savefig(outPut, dpi=1000)
'''
                                                   
