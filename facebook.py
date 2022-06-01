import snscrape.modules.facebook as snfacebook
# import pandas as pd
import networkx as nx


def getUserPosts(name):
    fb_list1 = []
    graph = nx.DiGraph()
    name = '' + name
    print(name)

    for i,result in enumerate(snfacebook.FacebookGroupScraper(name).get_items()): #declare a username 
        if(i>5):
            break;
        print(result.id)
        
        fb_list1.append([result]) #declare the attributes to be returned
    
    return fb_list1

print(getUserPosts("useless"))