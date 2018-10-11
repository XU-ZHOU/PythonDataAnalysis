import pandas as pd
import numpy as np
df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],
                    'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],
                    'data2':range(3)})
print(df1)
print(df2)

print(pd.merge(df1,df2))
print(pd.merge(df1,df2,on='key'))

df3 = pd.DataFrame({'1key':['b','b','a','c','a','a','b'],
                    'data1':range(7)})
df4 = pd.DataFrame({'rkey':['a','b','d'],
                    'data2':range(3)})

print(pd.merge(df3,df4,left_on='1key',right_on='rkey'))

df1 = pd.DataFrame({'key':['b','b','a','c','a','b'],
                    'data1':range(6)})
df2 = pd.DataFrame({'key':['a','b','a','b','d'],
                    'data2':range(5)})
print(df1)
print(df2)

arr = np.arange(12).reshape((3,4))
print(arr)

print(np.concatenate([arr,arr],axis=1))

s1 = pd.Series([0,1],index=['a','b'])
s2 = pd.Series([2,3,4],index=['c','d','e'])
s3 = pd.Series([5,6],index=['f','g'])
print(pd.concat([s1,s2,s3]))
print(pd.concat([s1,s2,s3],axis=1))

s4 = pd.concat([s1,s3])
print(s4)

print(pd.concat([s1,s4],axis=1))
print(pd.concat([s1,s4],axis=1,join='inner'))

a = pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],
              index=['f','e','d','c','b','a'])
b = pd.Series(np.arange(len(a),dtype=np.float64),
              index=['f','e','d','c','b','a'])
b[-1] = np.nan
print(a)
print(b)

print(np.where(pd.isnull(a),b,a))
print(b[:-2].combine_first(a[2:]))

