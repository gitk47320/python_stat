# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#data definition
height = [178,165,168,152,175,175,165,162,164,170,169,155,153,162,168]
weight = [63,62,69,41,71,61,62,48,52,55,69,48,44,49,69]

clf = LinearRegression()
height = np.array(height)
weight = np.array(weight)
height = height.reshape(-1,1)
weight = weight.reshape(-1,1)

clf.fit(height, weight)

plt.scatter(height, weight)
plt.plot(height,clf.predict(height))
plt.show()