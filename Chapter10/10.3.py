#apply：一般性的“拆分-应用-合并”

import pandas as pd
import numpy as np

tips = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']

def top(df,n=5,column='tip_pct'):
    return df.sort_values(by=column)[-n:]

#print(top(tips,n=6))

#print(tips.groupby('smoker').apply(top))

frame = pd.DataFrame({'data1':np.random.randn(1000),
                      'data2':np.random.randn(1000)})
quartiles = pd.cut(frame.data1,4)
#print(quartiles[:10])

def get_stats(group):
    return {'min':group.min(),'max':group.max(),
            'count':group.count(),'mean':group.mean()}

grouped = frame.data2.groupby(quartiles)
#print(grouped.apply(get_stats).unstack())

s = pd.Series(np.random.randn(6))
s[::2] = np.nan
#print(s)

#print(s.fillna(s.mean()))

states = ['Ohio','New York','Vermont','Florida',
          'Oregon','Nevada','California','Idaho']

group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8),index=states)
#print(data)

data[['Vermont','Nevada','Idaho']] = np.nan
#print(data)

#print(data.groupby(group_key).mean())

fill_mean = lambda g:g.fillna(g.mean())
#print(data.groupby(group_key).apply(fill_mean))

fill_values = {'East':0.5,'West':-1}
fill_func = lambda g:g.fillna(fill_values[g.name])
#print(data.groupby(group_key).apply(fill_func))


df = pd.DataFrame({'category':['a','a','a','a',
                               'b','b','b','b'],
                   'data':np.random.randn(8),
                   'weights':np.random.randn(8)})
#print(df)

grouped = df.groupby('category')
get_wavg = lambda g:np.average(g['data'],weights=g['weights'])
#print(grouped.apply(get_wavg))


close_px = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/stock_px_2.csv',parse_dates=True,index_col=0)
#print(close_px.info())
#print(close_px[-4:])










