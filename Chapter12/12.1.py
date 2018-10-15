#pandas的高级功能

#12.1 分类数据

import numpy as np
import pandas as pd
values = pd.Series(['apple','orange','apple','apple']*2)
print(values)

print(pd.unique(values))
print(pd.value_counts(values))

values = pd.Series([0,1,0,0]*2)
dim = pd.Series(['apple','orange'])
print(values)
print(dim)

print(dim.take(values))


#pandas的分类类型

fruits = ['apple','orange','apple','apple'] * 2
N = len(fruits)
df = pd.DataFrame({'fruit':fruits,
                   'basket_id':np.arange(N),
                   'count':np.random.randint(3,15,size=N),
                   'weight':np.random.uniform(0,4,size=N)},
                  columns=['basket_id','fruit','count','weight'])
print(df)

fruit_cat = df['fruit'].astype('category')
print(fruit_cat)
c = fruit_cat.values
print(type(c))
print(c.categories)
print(c.codes)

df['fruit'] = df['fruit'].astype('category')
print(df.fruit)

#用分类进行计算
np.random.seed(123456)
draws = np.random.randn(1000)
print(draws[:5])

bins = pd.qcut(draws,4)
print(bins)

