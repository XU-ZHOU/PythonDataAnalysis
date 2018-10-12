#使用pandas和seaborn绘图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()
