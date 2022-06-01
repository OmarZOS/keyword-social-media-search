import asyncio
from constants import *
from date import get_since_until
from twitter_scrapper import  process_data, save_json, search_twitter

list_of_trends = ['ouargla']
#   '#DamlaSönmez', 'الفردوس الاعلي','Alger', 'المغرب', '#كلنا_جنين', '#SPYxFamily', '#Bitcoin', '#الحريه_لاحمد_مناصره','#souhilabenlachhab', '#الو_ساهو_btv', '#Maroc', 
# class TwitterExtractor:

    # scraper = TwitterSearcher()

async def search_chunk(start,end,keyword):
    # await asyncio.sleep(delay)
    print(f"Searching for {keyword}  over  {start}=>{end}")
    data = search_twitter(f'{keyword} since:{start} until:{end}')
    print(f"Done searching for {keyword}  over  {start}=>{end}")
    return data

async def worker(tasks, results):
    # individual worker task (sometimes called consumer)
    # - sequentially process tasks as they come into the queue
    # and emit the results
    
    while True:
        start,end,keyword = await tasks.get()
        
        result = await search_chunk(start,end,keyword)
        if result :
            # print("Something to publish")
            await results.put((f"data/{keyword}/{start}{end}{keyword}",result))

async def assigner(tasks):
    # come up with tasks dynamically and enqueue them for processing
    task_n = 0

    while task_n < TASK_LIMIT and len(list_of_trends)>0 :
        
        # keyword = context.get(TWITTER_NEXT_KEYWORD)
        keyword = list_of_trends.pop(0)
        pair_days = get_since_until()

        for start,end in pair_days:
            # await asyncio.sleep(1)
            task_n += 1
            await tasks.put((start,end,keyword))
    
async def displayer(q):
    # show results of the tasks as they arrive
    while True:
        name,result = await q.get()
        graph = process_data(result)
        if(len(graph.nodes)>0):
            try:
                save_json(name,graph)
            except BaseException as e:
                print(str(e))
        # print(result)

async def main(pool_size):
    tasks = asyncio.Queue(100)
    results = asyncio.Queue(100)
    workers = [asyncio.create_task(worker(tasks, results))
            for _ in range(pool_size)]
    await asyncio.gather(assigner(tasks), displayer(results), *workers)



if __name__ == '__main__':
    
    asyncio.run(main(POOL_SIZE))