#数据聚合

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})

#print(df)

grouped = df.groupby('key1')
#print(grouped['data1'].quantile(0.9))

def peak_to_peak(arr):
    return arr.max() - arr.min()
#print(grouped.agg(peak_to_peak))

tips = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
#print(tips[:6])

grouped = tips.groupby(['day','smoker'])
grouped_pct = grouped['tip_pct']

#print(grouped_pct.agg('mean'))

functions = ['count','mean','max']
result = grouped['tip_pct','total_bill'].agg(functions)
#print(result)

#print(grouped.agg({'tip':np.max,'size':'sum'}))

#print(grouped.agg({'tip_pct':['min','max','mean','std'],'size':'sum'}))




