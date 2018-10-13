#重采样及频率转换

import pandas as pd
import numpy as np
rng = pd.date_range('2018-10-13',periods=100,freq='D')
ts = pd.Series(np.random.randn(len(rng)),index=rng)
print(ts)

print(ts.resample('M').mean())

print(ts.resample('M',kind='period').mean())

#降采样
rng = pd.date_range('2018-10-13',periods=12,freq='T')
ts = pd.Series(np.arange(12),index=rng)
print(ts)

print(ts.resample('5min',closed='right').sum())

#OHLC重采样
print(ts.resample('5min').ohlc())

#升采样和插值
frame = pd.DataFrame(np.random.randn(2,4),
                     index=pd.date_range('10/13/2018',periods=2,
                                         freq='W-WED'),
                     columns=['Colorado','Texas','New York','Ohio'])
print(frame)
