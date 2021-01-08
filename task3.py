import networkx as nx
import numpy as np
import pandas as pd

def Stanford_graph(file):
    file = pd.read_csv(file, delim_whitespace=True, names = ['e1' , 'e2'])
    links1 = np.array(file['e1'])
    links2 = np.array(file['e2'])
    G =nx.Graph()
    for x in range(len(links1)):
        G.add_edge(links1[x], links2[x])  

    return G