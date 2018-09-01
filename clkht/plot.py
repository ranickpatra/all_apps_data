from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np


dataset = pd.read_csv(sys.argv[1])


x = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values


poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(x)
poly_reg.fit(X_poly, y)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)


X_grid = np.arange(min(x), max(x), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
#plt.scatter(x, y, s=10, color = 'red')
plt.plot(x, y, color='blue', linewidth=2)
plt.plot(X_grid, lin_reg.predict(poly_reg.fit_transform(X_grid)), color = 'black')
plt.title(sys.argv[1])
lbl = dataset.columns.tolist()
plt.xlabel(lbl[0])
plt.ylabel(lbl[1])
plt.show()