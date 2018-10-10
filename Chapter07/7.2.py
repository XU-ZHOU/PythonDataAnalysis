#数据转换：过滤、清理以及其他转换
import pandas as pd
import numpy as np
data = pd.DataFrame({'k1':['one','two']*3 + ['two'],
                     'k2':[1,1,2,3,3,4,4]})
print(data)

print(data.duplicated())
print(data.drop_duplicates())

data['v1'] = range(7)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k1','k2'],keep='last'))

data = pd.DataFrame({'food':['bacon','pilled pork','bacon',
                             'Pastrami','corned beef','Bacon',
                             'pastrami','honey ham','nova lox'],
                     'ounces':[4,3,12,6,7.5,8,3,5,6]})
print(data)

meat_to_anlimal = {
    'bacon':'pig',
    'pilled pork':'pig',
    'pastrami':'cow',
    'corned beef':'cow',
    'honey ham':'pig',
    'nova lox':'salmon'
}

lowercased = data['food'].str.lower()
print(lowercased)

data['animal'] = lowercased.map(meat_to_anlimal)
print(data)

data['food'].map(lambda x:meat_to_anlimal[x.lower()])
print(data)

data = pd.Series([1.,-999.,2.,-999.,-1000.,3.])
print(data)

print(data.replace(-999,np.nan))

print(data.replace([-999,-1000],np.nan))

print(data.replace([-999,-1000],[np.nan,0]))

print(data.replace({-999:np.nan,-1000:0}))

data = pd.DataFrame(np.arange(12).reshape((3,4)),
                    index=['Ohio','Colorado','New York'],
                    columns=['one','two','three','four'])
transform = lambda x:x[:4].upper()
print(data.index.map(transform))

data.index = data.index.map(transform)
print(data)

print(data.rename(index=str.title,columns=str.upper))

print(data.rename(index={'OHIO':'INDIANA'},
                  columns={'three':'peekaboo'}))

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
cats = pd.cut(ages,bins)
print(cats)
print(cats.codes)
print(cats.categories)
print(pd.value_counts(cats))

group_names = ['Youth','YoungAdult','MiddleAged','Senior']
print(pd.cut(ages,bins,labels=group_names))

data = np.random.rand(20)
print(pd.cut(data,4,precision=2))

data = np.random.randn(1000)
cats = pd.qcut(data,4)
print(cats)
print(pd.value_counts(cats))

data = pd.DataFrame(np.random.randn(1000,4))
print(data.describe())

col = data[2]
print(col[np.abs(col)>3])
print(data[(np.abs(data)>3).any(1)])

df = pd.DataFrame(np.arange(5*4).reshape(5,4))
sampler = np.random.permutation(5)
print(sampler)

print(df)

print(df.take(sampler))

print(df.sample(n=3))

df = pd.DataFrame({'key':['b','b','a','c','a','b'],
                   'data1':range(6)})
print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'],prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

np.random.seed(12345)
values = np.random.rand(10)
print(values)

bins = [0,0.2,0.4,0.6,0.8,1]
print(pd.get_dummies(pd.cut(values,bins)))


