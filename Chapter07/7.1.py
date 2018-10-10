#本章讨论处理缺失数据、重复数据、字符串操作和其他分析数据转换的工具
import pandas as pd
import numpy as np
string_data = pd.Series(['aardvark','artickhoke',np.nan,'avocado'])
print(string_data)

string_data[0] = None
print(string_data.isnull())

from numpy import nan as NA
data = pd.Series([1,NA,3.5,NA,7])
print(data)
print(data.dropna())

data = pd.DataFrame([[1.,6.5,3.],[1.,NA,NA],
                     [NA,NA,NA],[NA,6.5,3.]])
cleaned = data.dropna()
print(data)
print(cleaned)

print(data.dropna(how='all'))
data[4] = NA
print(data)

print(data.dropna(axis=1,how='all'))

df = pd.DataFrame(np.random.randn(7,3))
df.iloc[:4,1] = NA
df.iloc[:2,2] = NA
print(df)

print(df.dropna())
print(df.dropna(thresh=2))
print(df.fillna(0))
print(df.fillna({1:0.5,2:0}))

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[2:,1] = NA
df.iloc[4:,2] = NA
print(df)

print(df.fillna(method='ffill'))
print(df.fillna(method='ffill',limit=2))

data = pd.Series([1.,NA,3.5,NA,7])
print(data.fillna(data.mean()))


