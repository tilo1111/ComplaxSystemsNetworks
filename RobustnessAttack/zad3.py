import networkx as nx

def closeness_attack(network, file_name):
    size = len(network.nodes())
    giantP = len(sorted(nx.connected_components(network), key = len, reverse=True)[0]) 
    results = []
    for f in range(1,size+1):
        centrality = nx.closeness_centrality(network)
        node_to_remove = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[0][0]
        network.remove_node(node_to_remove)
        if len(network.nodes()) > 0:
            giant = len(sorted(nx.connected_components(network), key = len, reverse=True)[0])
            results.append((f/size, giant/giantP))
        else:
            results.append((1, 0))
            
    with open(file_name + 'closeness.txt', 'w') as file:
        for (x, y) in results:
            print(str(x) + "  " + str(y), file=file)

def betweenness_attack(network, file_name):
    size = len(network.nodes())
    giantP = len(sorted(nx.connected_components(network), key = len, reverse=True)[0]) 
    results = []
    for f in range(1,size+1):
        centrality = nx.betweenness_centrality(network)
        node_to_remove = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[0][0]
        network.remove_node(node_to_remove)
        if len(network.nodes()) > 0:
            giant = len(sorted(nx.connected_components(network), key = len, reverse=True)[0])
            results.append((f/size, giant/giantP))
        else:
            results.append((1, 0))
            
    with open(file_name + 'betweenness.txt', 'w') as file:
        for (x, y) in results:
            print(str(x) + "  " + str(y), file=file)
            

for N in [1000]:
    ba = nx.barabasi_albert_graph(N, 1)
    closeness_attack(ba, "BAk2N" + str(N))
    ba = nx.barabasi_albert_graph(N, 1)
    betweenness_attack(ba, "BAk2N" + str(N))
    
for N in [1000]:
    ba1 = nx.barabasi_albert_graph(N, 2)
    closeness_attack(ba, "BAk4N" + str(N))
    ba1 = nx.barabasi_albert_graph(N, 2)
    betweenness_attack(ba, "BAk4N" + str(N))