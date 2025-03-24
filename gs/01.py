import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

np.random.seed(42)

data_root = '../datasets/lifesat/'
df = pd.read_csv( data_root + 'lifesat.csv' )
df.plot()