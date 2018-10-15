#Groupby高级应用

import pandas as pd
import numpy as np
df = pd.DataFrame({'key':['a','b','c']*4,
                   'value':np.arange(12.)})
print(df)

g = df.groupby('key').value
print(g.mean())

g.transform(lambda x:x.mean())
print(g)

print(g.transform(lambda x:x*2))

print(g.transform(lambda x:x.rank(ascending=False)))

#分组时间重采样
N = 15
times = pd.date_range('2018-10-15',freq='1min',periods=N)
df = pd.DataFrame({'time':times,
                   'value':np.arange(N)})
print(df)

print(df.set_index('time').resample('5min').count())

df2 = pd.DataFrame({'time':times.repeat(3),
                    'key':np.tile(['a','b','c'],N),
                    'value':np.arange(N*3)})
print(df2[:7])

time_key = pd.TimeGrouper('5min')
reshampled = (df2.set_index('time').groupby(['key',time_key]).sum())
print(reshampled)

