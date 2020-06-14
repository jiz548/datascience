import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_table(r'iris.data',sep=',',header=None)
iris_targets = data[4]
iris_features = data.iloc[:,0:4]

