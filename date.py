from datetime import datetime, timedelta,date

from constants import END_DATE, START_DATE

def date_range(start, end):
    delta = end - start  # as timedelta
    days = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(delta.days + 1)]
    return days

def sequenced(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a = iter(iterable[::])
    b = iter(iterable[1::])
    return zip(a, b)

def get_since_until():
    
    start_date = START_DATE
    end_date = END_DATE
        
    # print(date_range(start_date, end_date))

    return [ (x,y) for x, y in sequenced(date_range(start_date, end_date))]
    # print(f"since:{x} until:{y}")

# print(get_since_until())
