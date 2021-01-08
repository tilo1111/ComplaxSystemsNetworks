import networkx as nx

def degree_attack(network, file_name):
    size = len(network.nodes())
    giantP = len(sorted(nx.connected_components(network), key = len, reverse=True)[0]) 
    results = []
    for f in range(1,size+1):
        degrees = nx.degree(network)
        node_to_remove = max(degrees, key = lambda x:x[1])[0]
        network.remove_node(node_to_remove)
        if len(network.nodes()) > 0:
            giant = len(sorted(nx.connected_components(network), key = len, reverse=True)[0])
            results.append((f/size, giant/giantP))
        else:
            results.append((1, 0))
            
    with open(file_name + 'degree.txt', 'w') as file:
        for (x, y) in results:
            print(str(x) + "  " + str(y), file=file)
            

for N in [1000, 10000, 100000]:
    er = nx.erdos_renyi_graph(N, 0.0005)  
    degree_attack(er, "ERk05N" + str(N))

    er1 = nx.erdos_renyi_graph(N, 0.002)   
    degree_attack(er1, "ERk2N" + str(N))

    ba = nx.barabasi_albert_graph(N, 1) 
    degree_attack(ba, "BAk2N" + str(N))
    
    ba1 = nx.barabasi_albert_graph(N, 2) 
    degree_attack(ba1, "BAk4N" + str(N))
    
    ws = nx.watts_strogatz_graph(N, 2, 0.01)  
    degree_attack(ws, "WSk2N" + str(N))
    
    ws1 = nx.watts_strogatz_graph(N, 4, 0.01) 
    degree_attack(ws1, "WSk4N" + str(N))