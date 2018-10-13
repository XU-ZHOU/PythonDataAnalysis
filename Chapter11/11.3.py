#日期的范围，频率和移动

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import datetime



dates = [datetime(2011,1,2),datetime(2011,1,5),
         datetime(2011,1,7),datetime(2011,1,8),
         datetime(2011,1,10),datetime(2011,1,12)]
ts = pd.Series(np.random.randn(6),index=dates)
print(ts)
reshampler = ts.resample('D')
print(reshampler)

index = pd.date_range('2012-04-01','2012-06-01')
print(index)

print(pd.date_range(start='2018-04-01',periods=20))

print(pd.date_range(end='2020-06-01',periods=20))

#print(pd.date_range(('2018-01-01','2019-12-10',freq='BM')))

print(pd.date_range('2012-05-02 12:56:31',periods=5))
print(pd.date_range('2018-10-13-21:20:59',periods=5,normalize=True))


#频率和日期偏移量
from pandas.tseries.offsets import Hour,Minute
hour = Hour()
print(hour)

four_hours = Hour(4)
print(four_hours)

print(pd.date_range('2018-01-01','2018-01-02 23:59',freq='5h'))
print(pd.date_range('2018-10-13',periods=10,freq='2h30min'))

print(pd.date_range('2018-01-13','2018-12-20',freq='WOM-1FRI'))

ts = pd.Series(np.random.randn(4),
               index=pd.date_range('10/13/2018',periods=4,freq='M'))
print(ts)
print(ts.shift(2))
print(ts.shift(-2))
print(ts/ts.shift(1) - 1)

print(ts.shift(2,freq='M'))


from pandas.tseries.offsets import Day,MonthEnd
now = datetime(2018,10,13)
print(now+3*Day())

print(now+MonthEnd())

offset = MonthEnd()
print(offset.rollforward(now))

