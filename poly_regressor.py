import numpy as np
import pandas as pd

dataset= pd.read_csv('Position_Salaries.csv')

X=dataset.iloc[:, 1:-1].values
y=dataset.iloc[:,-1].values



from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=2)
X_poly=poly_reg.fit_transform(X)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_poly,y)
v=6.5
y_pred=regressor.predict(poly_reg.fit_transform([[6.5]])) 