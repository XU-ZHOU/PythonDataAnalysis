#14.3 全国婴儿姓名

import pandas as pd
names1880 = pd.read_csv('H:/ML/pydata-book-2nd-edition/datasets/babynames/yob1880.txt',
                        names=['name','sex','births'])
print(names1880)

print(names1880.groupby('sex').births.sum())

years = range(1880,2011)
pieces = []
columns = ['name','sex','births']
for year in years:
    path = 'H:/ML/pydata-book-2nd-edition/datasets/babynames/yob%d.txt' % year
    frame = pd.read_csv(path,names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces,ignore_index=True)
print(names)

total_births = names.pivot_table('births',index='year',
                                 columns='sex',aggfunc=sum)
print(total_births.tail())

def add_prop(group):
    group['prop'] = group.births / group.births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
print(names)

names.groupby(['year','sex']).prop.sum()

def get_top1000(group):
    return group.sort_values(by='births',ascending=False)[:1000]
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
top1000.reset_index(inplace=True,drop=True)
print(top1000)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births',index='year',
                                   columns='name',aggfunc=sum)
print(total_births.info())

table = top1000.pivot_table('prop',index='year',
                            columns='sex',aggfunc=sum)
