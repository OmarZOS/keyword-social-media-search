import snscrape.modules.twitter as sninstagram
# import pandas as pd
import networkx as nx



def getHashtagPosts(name):
    insta_list1 = []
    graph = nx.DiGraph()
    
    name = name
    print(name)

    for i,post in enumerate(sninstagram.TwitterProfileScraper(name).get_items()): #declare a username
        if(i>5):
            break;
        print(post)
        insta_list1.append(post)
        # graph.add_nodes_from([(post.url,{
        #     "url":post.url,
        #     "content":post.content,
        #     "commentsDisabled":post.commentsDisabled,
        #     "username":post.username,
        #     "date":post.date,
        #     "node_type":"post"
        # })])
        # return insta_list1
        # insta_list1.append([post]) #declare the attributes to be returned
    
    return insta_list1

print(getHashtagPosts({"id":"912536424154529792"}))