#%%
import json
import math
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing import layout

#%%
name = "github_star"
G = nx.DiGraph(name=name)


#%%

# read json
with open("../data/" + name + ".json") as f:
    graph_data = json.load(f)

graph_data["data"]["repository"]["stargazers"]["nodes"]
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
users = graph_data["data"]["repository"]["stargazers"]["nodes"]

for user in users:
    followers = get_followers_list(user)
    for follower in followers:
        nodes.append((get_data(follower)))
        nx.add_path(G, [get_username(follower), get_username(user)])

    followings = get_following_list(user)
    for following in followings:
        nodes.append((get_data(following)))
        nx.add_path(G, [get_username(user), get_username(following)])

G.add_nodes_from(nodes)
print(G.nodes.data().__len__())  # 1080

#%% export
nx.write_gexf(G, "../data/" + name + ".gexf")

# %%
