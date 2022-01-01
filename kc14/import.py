import networkx as nx

# import
G = nx.Graph(nx.read_gexf("./data/graph.gexf"))

print(G.nodes.data())
