import pandas as pd
import numpy as np
import pylab as P

df = pd.read_csv('train.csv', header=0)
df['Age'].dropna().hist(bins=16, range=(0,80), alpha=.5)
P.show()
