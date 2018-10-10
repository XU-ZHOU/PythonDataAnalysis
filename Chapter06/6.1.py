import pandas as pd
df = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex1.csv')
print(df)

df1 = pd.read_table('H:/ML/pydata-book-2nd-edition/examples/ex1.csv',sep=',')
print(df1)

df3 = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex2.csv',header=None)
print(df3)

df4 = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex2.csv',names=['a','b','c','d','message'])
print(df4)

names = ['a','b','c','d','message']
df5 = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex2.csv',names=names,index_col='message')
print(df5)

parsed = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/csv_mindex.csv',index_col=['key1','key2'])
print(parsed)

print(list(open('H:/ML/pydata-book-2nd-edition/examples/ex3.txt')))
result = pd.read_table('H:/ML/pydata-book-2nd-edition/examples/ex3.txt',sep='\s+')
print(result)

result = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex5.csv')
print(result)

print(pd.isnull(result))

result = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex5.csv',na_values=['*'])
print(result)

pd.options.display.max_rows = 10
result = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex6.csv')
print(result)

read1 = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex6.csv',nrows=5)
print(read1)

chunker = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex6.csv',chunksize=1000)
print(chunker)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10])

data = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex5.csv')
print(data)

data = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/ex7.csv')
print(data)

import csv
f = open('H:/ML/pydata-book-2nd-edition/examples/ex7.csv')
reader = csv.reader(f)
for line in reader:
    print(line)

with open('H:/ML/pydata-book-2nd-edition/examples/ex7.csv') as f:
    lines = list(csv.reader(f))
header,values = lines[0],lines[1:]
data_dict = {h: v for h,v in zip(header,zip(*values))}
print(data_dict)

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
reader = csv.reader(f,dialect=my_dialect)


