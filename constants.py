from datetime import datetime, timedelta,date
import os

POOL_SIZE = 50
CHUNK_SIZE = 5
TWEET_LIMIT = 100
TASK_LIMIT = 200
TWITTER_NEXT_KEYWORD = "LOL"
START_DATE = datetime(2021, 7, 28)
END_DATE = datetime.now()

RMQ_HOST = "localhost"
RMQ_PORT = ""
RMQ_EXCHANGE = "transform"
RMQ_QUEUE = "Twitter"
RMQ_USER = "omar"
RMQ_PASS = "omar"
ROUTE_KEY="Twitter"

CONTEXT_SCHEME=str(os.getenv("CONTEXT_SCHEME"))
CONTEXT_HOST=str(os.getenv("CONTEXT_HOST"))
CONTEXT_PORT=str(os.getenv("CONTEXT_PORT"))

CONTEXT_URL=f"{CONTEXT_SCHEME}://{CONTEXT_HOST}:{CONTEXT_PORT}"