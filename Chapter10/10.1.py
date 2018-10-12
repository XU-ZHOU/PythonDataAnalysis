#数据整合与分组运算

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})
#print(df)
grouped = df['data1'].groupby(df['key1'])
#print(grouped.mean())

means = df['data1'].groupby([df['key1'],df['key2']]).mean()
#print(means)

#print(means.unstack())

states = np.array(['Ohio','California','California','Ohio','Ohio'])
years = np.array([2005,2005,2006,2005,2006])

#print(df['data1'].groupby([states,years]).mean())

columns = pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],
                                     [1,3,5,1,3]],
                                    names=['cty','tenor'])
hier_df = pd.DataFrame(np.random.randn(4,5),columns=columns)
print(hier_df)



