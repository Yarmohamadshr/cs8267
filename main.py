
import numpy as np
import pandas as pd

data = pd.read_csv("./kmtest.csv")
print(data)

def euclidean_distance(x1,x2):
       return np.sqrt(np.sum(x1-x2)**2)
       