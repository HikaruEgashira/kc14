#%%
import json
import math
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing import layout

#%%
name = "github_ff"
G = nx.DiGraph(name=name)


#%%

# read json
with open("../data/" + name + ".json") as f:
    graph_data = json.load(f)

graph_data["data"]["user"]["login"]
#%%
def get_username(data: dict):
    return data["login"]


def get_data(data: dict) -> tuple:
    return (data["login"], {"company": data["company"]})


def has_atmark(x: dict) -> bool:
    return x != {} and x["company"] != None  # and x["company"].find("@") != -1


def filter_only_atmark(data: List[dict]) -> List[dict]:
    return list(filter(has_atmark, data))


def get_followers_list(data: dict) -> List[dict]:
    return list(filter(has_atmark, data["followers"]["nodes"]))


def get_following_list(data: dict) -> List[dict]:
    return list(filter(has_atmark, data["following"]["nodes"]))


#%%
# 0次
nodes: List[tuple] = []
user1 = graph_data["data"]["user"]

# 1次
followers1 = get_followers_list(user1)
for follower1 in followers1:
    nodes.append((get_data(follower1)))
    # nx.add_path(G, [get_username(follower1), get_username(user1)])

followings1 = get_following_list(user1)
for following1 in followings1:
    nodes.append((get_data(following1)))
    # nx.add_path(G, [get_username(user1), get_username(following1)])

# 2次
for follower1 in followers1:
    followers2 = get_followers_list(follower1)
    for follower2 in followers2:
        nodes.append((get_data(follower2)))
        if get_username(follower2) != get_username(user1):
            nx.add_path(G, [get_username(follower2), get_username(follower1)])

    followings2 = get_following_list(follower1)
    for following2 in followings2:
        nodes.append((get_data(following2)))
        if get_username(following2) != get_username(user1):
            nx.add_path(G, [get_username(following2), get_username((follower1))])

for following1 in followings1:
    followers2 = get_followers_list(following1)
    for follower2 in followers2:
        nodes.append((get_data(follower2)))
        if get_username(follower2) != get_username(user1):
            nx.add_path(G, [get_username(follower2), get_username(following1)])

    followings2 = get_following_list(following1)
    for following2 in followings2:
        nodes.append((get_data(following2)))
        if get_username(following2) != get_username(user1):
            nx.add_path(G, [get_username(following2), get_username(following1)])

G.add_nodes_from(nodes)
print(G.nodes.data().__len__())  # 243

#%% export
nx.write_gexf(G, "../data/" + name + ".gexf")

# %%
