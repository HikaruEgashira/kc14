#%%
import json
import math
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing import layout

#%%
G = nx.DiGraph(name="GitHub ff")


#%%
# read json
with open("../data/github_ff.json") as f:
    data = json.load(f)

data["data"]["user"]["login"]
#%%
def get_username(data):
    return data["login"]


def get_followers_list(data):
    return list(filter(lambda x: x != {}, data["followers"]["nodes"]))


def get_following_list(data):
    return list(filter(lambda x: x != {}, data["following"]["nodes"]))


#%%
userlist = set()

# 0次
user1 = data["data"]["user"]

# 1次
followers1 = get_followers_list(user1)
for follower1 in followers1:
    userlist.add(follower1)
    nx.add_path(G, [get_username(follower1), get_username(user1)])

followings1 = get_following_list(user1)
for follower1 in followings1:
    nx.add_path(G, [get_username(user1), get_username(follower1)])

# 2次
for follower1 in followers1:
    followers2 = get_followers_list(follower1)
    for follower2 in followers2:
        nx.add_path(G, [get_username(follower2), get_username(follower1)])

    followings2 = get_following_list(follower1)
    for following2 in followings2:
        nx.add_path(G, [get_username(follower1), get_username((following2))])

for following1 in followings1:
    followers2 = get_followers_list(following1)
    for follower2 in followers2:
        nx.add_path(G, [get_username(follower2), get_username(following1)])

    followings2 = get_following_list(following1)
    for following2 in followings2:
        nx.add_path(G, [get_username(following1), get_username(following2)])


#%%
# plot G
nx.draw(G, with_labels=False)
plt.show()

# print(G.nodes.data())

# export
# nx.write_gexf(G, "../data/graph.gexf")

# %%
