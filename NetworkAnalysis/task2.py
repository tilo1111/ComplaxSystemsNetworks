import networkx as nx
import numpy as np


def path(network):
    paths = nx.shortest_path_length(network)
    list_of_paths = [tup[1][key] for tup in paths for key in tup[1].keys() if tup[0] < key]  # distribution of paths
    ave_path = sum(list_of_paths)/len(list_of_paths)  # ave_path = nx.average_shortest_path_length(network)
    return ave_path


def clustering_coefficient(network):
    coefficients = nx.clustering(network)
    list_of_coefficients = list(coefficients.values())  # distribution of clustering coeficient
    ave_coefficient = sum(list_of_coefficients)/len(list_of_coefficients)  # ave_coefficient = nx.average_clustering(network)
    return ave_coefficient  # average coefficient


def path_diam(network):
    paths = nx.shortest_path_length(network)
    list_of_paths = [tup[1][key] for tup in paths for key in tup[1].keys() if tup[0] < key]
    ave_path = sum(list_of_paths)/len(list_of_paths)  # ave_path = nx.average_shortest_path_length(network)
    diameter = max(list_of_paths)
    return ave_path, diameter


times = 10


def beta_f():
    list_with_steps = np.arange(0.01, 1.001, 0.01, dtype='float')
    n = 1000
    for k in [2, 4, 10]:
        with open(str(k) + 'k.txt', 'w') as f:
            for beta in list_with_steps:
                ave_path = 0
                ave_coefficient = 0
                for time in range(0, times):
                    network = nx.watts_strogatz_graph(n, k, beta)
                    ave_path += path(network)/times
                    ave_coefficient += clustering_coefficient(network)/times
                print(str(beta), str(ave_path), str(ave_coefficient), file=f)


beta_f()


def several_n():
    list_with_steps = np.arange(100, 1001, 10, dtype='int')
    k = 4
    beta = 0.8
    with open('N.txt', 'w') as f:
        for N in list_with_steps:
            path_val = 0
            diam_val = 0
            for time in range(0, times):
                network = nx.watts_strogatz_graph(N, k, beta)
                ave_path, diameter = path_diam(network)
                path_val += ave_path/times
                diam_val += diameter/times
            print(str(N), str(path_val), str(diam_val), (np.log(N)/np.log(k)), file=f)


several_n()
