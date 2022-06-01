

import json
import os
from networkx.readwrite import json_graph
import networkx as nx

# def FunctionName(args):

def graph_to_json(graph):
    return json_graph.node_link_data(graph)
    
def get_users(path):
    
    user_graph = nx.DiGraph()

    keywords = os.listdir(path)
    for term in keywords:
        for file in os.listdir(f"{path}/{term}")    :
            graph = from_networkx(f"{path}/{term}/{file}")
            for item in graph.nodes(data=True):
                try:
                    if item[1]["node_type"] == "user":
                        user_graph.add_nodes_from([(item[0],item[1].items())])
                    # if len(user_graph.nodes())>5:
                    #     break
                except BaseException as e:
                    print(str(e))
                print(len(user_graph.nodes()))
                
    return user_graph
        

def from_networkx(target):
    with open(target) as f:
        data  = json.load(f)
    graph = json_graph.node_link_graph(data)
    return graph

def save_user_node_file(filename):
    graph = get_users("data")
    g_json = graph_to_json(graph)
    # os.makedirs(os.path.dirname(filename), exist_ok=True)
    print(f"loading into {filename}")
    json.dump(g_json,open(filename,'w'),indent=2)
    
save_user_node_file("users.json")