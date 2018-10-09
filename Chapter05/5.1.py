import pandas as pd
import numpy as np
from pandas import Series,DataFrame
obj = pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)

obj2 = pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)
print(obj2['a'])
print(obj2['d'])
print(obj2[['c','a','d']])

print(obj2[obj2>0])
print(obj2*2)

print('b' in obj2)
sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = pd.Series(sdata)
print(obj3)

states = ['California','Ohio','Oregon','Texas']
obj4 = pd.Series(sdata,index=states)
print(obj4)

print(pd.isnull(obj4))

print(pd.notnull(obj4))

print(obj4.isnull())

print(obj3)
print(obj4)
print(obj3+obj4)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

print(obj)
obj.index = ['Bob','Steve','Jeff','Ryan']
print(obj)

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002,2003],
        'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head())
print(pd.DataFrame(data,columns=['year','state','pop']))
frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],
                      index=['one','two','three','four','five','six'])
print(frame2)

print(frame2['state'])

print(frame2.loc['three'])

frame2['debt'] = 16.5
print(frame2)

frame2['debt'] = np.arange(6.)
print(frame2)

val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt'] = val
print(frame2)

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

del frame2['eastern']
print(frame2)

pop = {'Nevada':{2001:2.4,2002:2.9},
       'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)

print(frame3.T)

frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)

print(frame3.values)

obj = pd.Series(range(3),index=['a','b','c'])
index = obj.index
print(index)
print(index[1:])

labels = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5,-2.5,0],index=labels)
print(obj2)

obj = pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print(obj)

obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)

obj3 = pd.Series(['blue','purple','yellow'],index=[0,2,4])
print(obj3)

print(obj3.reindex(range(6),method='ffill'))

frame = pd.DataFrame(np.arange(9).reshape((3,3)),
                     index=['a','c','d'],
                     columns=['Ohio','Texas','California'])
print(frame)

frame2 = frame.reindex(['a','b','c','d'])
print(frame2)

obj = pd.Series(np.arange(5.),index=['a','b','c','d','e'])
print(obj)

new_obj = obj.drop('c')
print(new_obj)

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
    index=['Ohio', 'Colorado', 'Utah', 'New York'],
    columns=['one', 'two', 'three', 'four'])
print(data)

print(data.loc['Colorado',['two','three']])

print(data.iloc[2,[3,0,1]])

print(data.iloc[2])

print(data.iloc[[1,2],[3,0,1]])


