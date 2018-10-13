#时间序列基础

import pandas as pd
import numpy as np
from datetime import datetime
dates = [datetime(2011,1,2),datetime(2011,1,5),
         datetime(2011,1,7),datetime(2011,1,8),
         datetime(2011,1,10),datetime(2011,1,12)]
ts = pd.Series(np.random.randn(6),index=dates)
print(ts)
print(ts.index)
print(ts+ts[::2])

stamp = ts.index[0]
print(stamp)

#索引，选取，子集构造
stamp = ts.index[2]
print(ts[stamp])

longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('1/1/2000',periods=1000))
print(longer_ts)
print(longer_ts['2001'])
print(longer_ts['2001-05'])

print(ts[datetime(2011,1,7)])

print(ts.truncate(after='1/9/2011'))

dates = pd.date_range('1/1/2000',periods=100,freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100,4),
                       index=dates,
                       columns=['Colorado','Texas',
                                'New York','Ohio'])
print(long_df['5-2001'])

dates = pd.DatetimeIndex(['1/1/2000','1/2/2000','1/2/2000',
                          '1/2/2000','1/3/2000'])
dup_ts = pd.Series(np.arange(5),index=dates)
print(dup_ts)
print(dup_ts.index.is_unique)

grouped = dup_ts.groupby(level=0)
print(grouped.mean())
print(grouped.count())



