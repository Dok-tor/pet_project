import networkx as nx

G = nx.DiGraph()
for i in range(100):
    G.add_node(i)

G.add_edge(1, 10, weight=10)

print(nx.shortest_path(G, 1, 10))