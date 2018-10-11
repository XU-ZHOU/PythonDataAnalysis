#重塑和轴向旋转
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=pd.Index(['Ohio','Colorado'],name='state'),
                    columns=pd.Index(['one','two','three'],
                    name='number'))
print(data)

result = data.stack()
print(result)
print(result.unstack())

print(result.unstack(0))
print(result.unstack('state'))

data = pd.read_csv('H:/ML/pydata-book-2nd-edition/examples/macrodata.csv')
print(data.head())




