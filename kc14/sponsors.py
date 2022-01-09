#%%
import json

import networkx as nx
import pandas as pd

#%%
# read json
with open("../data/github_sponsors.json") as f:
    data = json.load(f)
print(data["data"]["user"]["login"])

#%%
user1 = data["data"]["user"]  # 1次
namelist = [user1["login"]]

users2 = filter(lambda x: x != {}, user1["sponsors"]["nodes"])

for user2 in users2:  # 2次
    users3 = filter(lambda x: x != {}, user2["sponsors"]["nodes"])
    namelist.extend([u["login"] for u in users3])

    for user3 in users3:  # 3次
        users4 = filter(lambda x: x != {}, user3["sponsors"]["nodes"])
        namelist.extend([u["login"] for u in users4])

        for user4 in users4:  # 4次
            users5 = filter(lambda x: x != {}, user4["sponsors"]["nodes"])
            namelist.extend([u["login"] for u in users5])

            for user5 in users5:  # 5次
                users6 = filter(lambda x: x != {}, user5["sponsors"]["nodes"])
                namelist.extend([u["login"] for u in users6])

namelist.__len__()
#%%
df = pd.json_normalize(data["data"]["user"]["sponsors"]["nodes"])
df.head()

# G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2, 3])
# G.add_nodes_from(
#     [
#         (4, {"color": "red"}),
#         (5, {"color": "green"}),
#     ]
# )

# print(G.nodes.data())

# export
# nx.write_gexf(G, "./data/graph.gexf")

# %%
