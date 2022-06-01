import snscrape.modules.twitter as sntwitter
CHUNK_SIZE = 5
TWEET_LIMIT = 150


def search_twitter(query):
        # Using TwitterSearchScraper to scrape data and append tweets to list
        local_list=[]
        for i,trend in enumerate(sntwitter.TwitterTrendsScraper().get_items()):
            
            # if i%CHUNK_SIZE == 0:
            #     self.process_data(local_list)
            #     local_list=[]
            
            # if i > TWEET_LIMIT:
            #     # self.process_data(local_list)
            #     break    #.date, tweet.id, tweet.content, tweet.user.username,tweet.user.id
            
            # print(tweet.id)
            # print(tweet.user.id)
            if trend.domainContext == "Trending in Algeria":
                local_list.append(trend.name)
            
        return local_list

keyword = "DZ"
from_date="2021-01-01"
to_date="2022-04-06"


data = search_twitter(f'{keyword}')# since:{from_date} until:{to_date}
print(data)
# print([k.hashtags for k in data])
# print(scraper.graph.nodes)
# scraper.save_json("somewhere",scraper.graph)












