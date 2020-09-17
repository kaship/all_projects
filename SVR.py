
import numpy as np
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')

X=dataset.iloc[:, 1:2].values

y=dataset.iloc[:, 2].values

y=y.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
sc2=StandardScaler()

X=sc1.fit_transform(X)
y=sc2.fit_transform(y)

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)

y_pred=regressor.predict(sc1.transform([[6.5]]))

y_pred1 = sc2.inverse_transform(y_pred)