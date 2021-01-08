import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import task1 as my_graph
import task3 as stan


def degree(network, filename):
    degrees = nx.degree(network)
    list_of_degrees = [y for (x, y) in degrees]  # degree distribution (histogram)
    dist_of_degrees = [(x, list_of_degrees.count(x)/len(degrees)) for x in range(max(list_of_degrees)+1)]
    ave_degree = sum(list_of_degrees)/len(list_of_degrees)   # average node degree
    with open(filename + 'degreeDist.txt', 'w') as g:
        for (x) in dist_of_degrees:
            print(str(x[0]) + " " + str(x[1]), file=g)
    #plt.hist(list_of_degrees)   # degree distribution
    #plt.show()
    return ave_degree   # average node degree

def path(network, filename):
    paths = nx.shortest_path_length(network)
    list_of_paths = [tup[1][key] for tup in paths for key in tup[1].keys() if tup[0] < key]  # distribution of paths (histogram)
    dist_of_paths = [(x, list_of_paths.count(x)/len(list_of_paths)) for x in range(max(list_of_paths)+1)]
    ave_path = nx.average_shortest_path_length(network)  # ave_path = nx.average_shortest_path_length(network)
    diameter = max(list_of_paths)  # diameter
    with open(filename + 'pathDist.txt', 'w') as g:
        for x in dist_of_paths:
            print(str(x[0]) + " " + str(x[1]), file=g)
    #plt.hist(list_of_paths)  # distribution of paths
    #plt.show()
    return ave_path, diameter   # ave_path = nx.average_shortest_path_length(network), diameter

def clustering_coefficient(network, filename):
    coefficients = nx.clustering(network)
    list_of_coefficients = list(coefficients.values())  # distribution of clustering coeficient
    list_of_coefficients = [round(x, 2) for x in list_of_coefficients]
    dist_of_coefficients = [(x, list_of_coefficients.count(x)/len(list_of_coefficients)) 
                            for x in np.unique(list_of_coefficients)]
    ave_coefficient = sum(list_of_coefficients)/len(list_of_coefficients)  # ave_coefficient = nx.average_clustering(network)
    with open(filename + 'clusterDist.txt', 'w') as g:
        for x in dist_of_coefficients:
            print(str(x[0]) + " " + str(x[1]), file=g)
    #plt.hist(list_of_coefficients)   # distribution of clustering coeficient
    #plt.show()
    return ave_coefficient # average coefficient

def betweenness(network, filename):
    centrality = nx.betweenness_centrality(network)
    list_of_centrality = list(centrality.values())
    list_of_centrality = [round(x, 3) for x in list_of_centrality]
    dist_of_centrality = [(x, list_of_centrality.count(x)/len(list_of_centrality)) 
                            for x in np.unique(list_of_centrality)]
    with open(filename + 'betweennessDist.txt', 'w') as f:
        for x in dist_of_centrality:
            print(str(x[0]) + " " + str(x[1]), file=f)
    
def my_eccentricity(network, filename):
    centrality = nx.eccentricity(network)
    list_of_centrality = list(centrality.values())
    dist_of_centrality = [(x, list_of_centrality.count(x)/len(list_of_centrality)) 
                            for x in np.unique(list_of_centrality)]
    with open(filename + 'eccentricityDist.txt', 'w') as f:
        for x in dist_of_centrality:
            print(str(x[0]) + " " + str(x[1]), file=f)
    
def closeness(network, filename):
    centrality = nx.closeness_centrality(network)
    list_of_centrality = list(centrality.values())
    list_of_centrality = [round(x, 2) for x in list_of_centrality]
    dist_of_centrality = [(x, list_of_centrality.count(x)/len(list_of_centrality)) 
                            for x in np.unique(list_of_centrality)]
    with open(filename + 'closenessDist.txt', 'w') as f:
        for x in dist_of_centrality:
            print(str(x[0]) + " " + str(x[1]), file=f)

def barabasi_albert(n, m):
    ba = nx.barabasi_albert_graph(n, m)
    #nx.draw(ba, with_labels=True, pos=nx.kamada_kawai_layout(ba, scale=2))
    #plt.show()
    print(degree_r(ba, 'results\BA'))
    print(path(ba, 'results\BA'))
    print(clustering_coefficient(ba, 'results\BA'))
    betweenness(ba, 'results\BA')
    my_eccentricity(ba, 'results\BA')
    closeness(ba, 'results\BA')

def my_graph_ba(m, m0, n):
    my = my_graph.BA_network(m, m0, n)
    #nx.draw(my, with_labels=True, pos=nx.kamada_kawai_layout(my, scale=2))
    #plt.show()
    print(degree_r(my, 'results\myBA'))
    print(path(my, 'results\myBA'))
    print(clustering_coefficient(my, 'results\myBA'))
    betweenness(my, 'results\myBA')
    my_eccentricity(my, 'results\myBA')
    closeness(my, 'results\myBA')

def watts_strogatz(n, k, p):
    ws = nx.watts_strogatz_graph(n, k, p)
    #nx.draw(ws, with_labels=True, pos=nx.kamada_kawai_layout(ws, scale=2))
    #plt.show()
    print(degree(ws, 'results\WS'))
    print(path(ws, 'results\WS'))
    print(clustering_coefficient_r(ws, 'results\WS'))
    betweenness(ws, 'results\WS')
    my_eccentricity(ws, 'results\WS')
    closeness(ws, 'results\WS')

def erdos_renyi_p(n, p):
    er = nx.erdos_renyi_graph(n, p)
    #nx.draw(er, with_labels=True, pos=nx.kamada_kawai_layout(er, scale=2))
    #plt.show()
    print(degree(er, 'results\ERp'))
    print(path(er, 'results\ERp'))
    print(clustering_coefficient(er, 'results\ERp'))
    betweenness(er, 'results\ERp')
    my_eccentricity(er, 'results\ERp')
    closeness(er, 'results\ERp')

def erdos_renyi_L(n, l):
    er = nx.gnm_random_graph(n, l)
    #nx.draw(er, with_labels=True, pos=nx.kamada_kawai_layout(er, scale=2))
    #plt.show()
    print(degree(er, 'results\ERl'))
    print(path(er, 'results\ERl'))
    print(clustering_coefficient(er, 'results\ERl'))
    betweenness(er, 'results\ERl')
    my_eccentricity(er, 'results\ERl')
    closeness(er, 'results\ERl')
    
def Stan_graph():
    St = stan.Stanford_graph('facebook_combined.txt')
    print(degree_r(St, 'results\St'))
    print(path(St, 'results\St'))
    print(clustering_coefficient_r(St, 'results\St'))
    betweenness(St, 'results\St')
    my_eccentricity(St, 'results\St')
    closeness(St, 'results\St')