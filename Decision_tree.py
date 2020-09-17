import numpy as np
import pandas as pd 

dataset = pd.read_csv('Position_Salaries.csv')

X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)


from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=20 , random_state=0)
regressor.fit(X,y)

y_pred=regressor.predict([[6.5]])
