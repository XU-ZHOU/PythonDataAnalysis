#时间序列

from datetime import datetime
import pandas as pd

now = datetime.now()
print(now)

print(now.year,now.month,now.day)

delta = datetime(2018,10,13) - datetime(1993,10,19,10,11)
print(delta)
print(delta.days)
print(delta.seconds)

from datetime import timedelta
start = datetime(2011,1,7)
print(start+timedelta(12))

stamp = datetime(2011,1,3)
print(str(stamp))

print(stamp.strftime('%Y-%m-%d'))

value = '2011-01-03'
print(datetime.strptime(value,'%Y-%m-%d'))

datestrs = ['7/6/2011','8/6/2011']
print([datetime.strptime(x,'%m/%d/%Y') for x in datestrs])

from dateutil.parser import parse
print(parse('2011-01-03'))

print(parse('Jan 31,1997 10:45 PM'))

print(parse('6/12/2011',dayfirst=True))

datestrs = ['2018-07-06 12:00:00','2018-08-06 00:00:00']
print(pd.to_datetime(datestrs))

idx = pd.to_datetime(datestrs+[None])
print(idx)
print(idx[2])

print(pd.isnull(idx))

