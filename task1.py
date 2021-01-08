import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt


def BA_network(m, m0, n):  # m - no. of edges connecting added node, m0 - initial nodes, n - no of nodes
    G = nx.Graph()

    if (m <= m0 and m0 <= n):
        for i in range(n):
            G.add_node(i)  # creating n nodes

        for i in range(m0):
            for j in range(m0 + 1):
                if i != j:
                    G.add_edge(i, j)  # creating complete graph with m0 nodes

        x = m0
        prob = np.zeros(n)

        while x < n:
            for i in range(n):
                prob[i] = G.degree[i] / len(G.edges())

            for i in range(m):
                newNode = random.choices(list(range(n)), prob)
                prob[newNode] = 0
                G.add_edge(x, newNode[0])
            x += 1

    else:
        print("Wrong parameters.")

    return G


#graph = BA_network(1, 3, 10)

#nx.draw(graph, with_labels=True, pos=nx.kamada_kawai_layout(graph, scale=2))
#plt.show()
