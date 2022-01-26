# %%
from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

# %%
name = "github_ff"
G = nx.Graph(nx.read_gexf("../data/" + name + ".gexf"))

print(list(G.nodes.data())[:5])

# %%
cliques = nx.find_cliques(G)
community = list(filter(lambda x: len(x) > 3, cliques))

print(community)
# %%
import numpy as np


def community_layout(g, partition):
    """
    Compute the layout for a modular graph.


    Arguments:
    ----------
    g -- networkx.Graph or networkx.DiGraph instance
        graph to plot

    partition -- dict mapping int node -> int community
        graph partitions


    Returns:
    --------
    pos -- dict mapping int node -> (float x, float y)
        node positions

    """

    pos_communities = _position_communities(g, partition, scale=3.0)

    pos_nodes = _position_nodes(g, partition, scale=1.0)

    # combine positions
    pos = dict()
    for node in g.nodes():
        pos[node] = pos_communities[node] + pos_nodes[node]

    return pos


def _position_communities(g, partition, **kwargs):

    # create a weighted graph, in which each node corresponds to a community,
    # and each edge weight to the number of edges between communities
    between_community_edges = _find_between_community_edges(g, partition)

    communities = set(partition.values())
    hypergraph = nx.DiGraph()
    hypergraph.add_nodes_from(communities)
    for (ci, cj), edges in between_community_edges.items():
        hypergraph.add_edge(ci, cj, weight=len(edges))

    # find layout for communities
    pos_communities: Any = nx.spring_layout(hypergraph, **kwargs)

    # set node positions to position of community
    pos = dict()
    for node, community in partition.items():
        pos[node] = pos_communities[community]

    return pos


def _find_between_community_edges(g, partition):

    edges = dict()

    for (ni, nj) in g.edges():
        ci = partition[ni]
        cj = partition[nj]

        if ci != cj:
            try:
                edges[(ci, cj)] += [(ni, nj)]
            except KeyError:
                edges[(ci, cj)] = [(ni, nj)]

    return edges


def _position_nodes(g, partition, **kwargs):
    """
    Positions nodes within communities.
    """

    communities = dict()
    for node, community in partition.items():
        try:
            communities[community] += [node]
        except KeyError:
            communities[community] = [node]

    pos = dict()
    for ci, nodes in communities.items():
        subgraph = g.subgraph(nodes)
        pos_subgraph = nx.spring_layout(subgraph, **kwargs)
        pos.update(pos_subgraph)

    return pos


# %%
from community import community_louvain

partition = community_louvain.best_partition(G)
pos = community_layout(G, partition)


nx.draw(G, pos, node_color=list(partition.values()))
plt.show()

# %%
def plot_by_partition(num: int):
    node_color = [i if i == num else None for i in partition.values()]
    nx.draw(
        G,
        pos,
        node_color=node_color,
    )
    print([k for k, v in partition.items() if v == num])


plot_by_partition(1)

# %%
# # インターン先
plot_by_partition(1)

# # %%
# # つくば1
# plot_by_partition(2)

# # %%
# # 言語界隈
# plot_by_partition(3)

# # %%
# # レイヤー低め
# plot_by_partition(4)

# %%
# # スタートアップ
plot_by_partition(5)

# # %%
# # つくば2
# plot_by_partition(6)

# # %%
# # 海外
# plot_by_partition(7)

# %%
name = "github_star"
G = nx.Graph(nx.read_gexf("../data/" + name + ".gexf"))

print(list(G.nodes.data())[:5])

# %%
partition = community_louvain.best_partition(G)
pos = community_layout(G, partition)


nx.draw(G, pos, node_color=list(partition.values()))
plt.show()

values: Any = partition.values()
community_count = max(values)  # 41

# range(community_count)
comunity_sum_count = [
    list(partition.values()).count(num) for num in range(community_count)
]
target_comunity_num = comunity_sum_count.index(max(comunity_sum_count))
plot_by_partition(target_comunity_num)

# %%
# 次数中心性(Degree Centrality)
degree_centrality = nx.degree_centrality(G)  # wpank

# 希望中心性(Betweenness Centrality)
betweenness_centrality = nx.betweenness_centrality(G)  # wpank

# 固有ベクトル中心性(Eigenvector Centrality)
eigenvector_centrality = nx.eigenvector_centrality(G)  # wpank

# %%
# PageRank
pagerank = nx.pagerank(G)  # wpank
# max_user = max(pagerank, key=pagerank.get)
# print(max_user)
