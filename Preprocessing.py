import numpy as np 
import pandas as pd


dataset = pd.read_csv('Data.csv')
X= dataset.iloc[: , 0:3 ].values
y=dataset.iloc[:, 3]

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
imputer.fit(X[: , 7:8])
X[: , 7:8]= imputer.transform(X[: , 7:8])


from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X_1 = LabelEncoder()
X[:,0]= labelencoder_X_1.fit_transform(X[:,0])
ct = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)
X=X[:,1:5]




from sklearn.model_selection import train_test_split



 from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
X_train=sc.fit_transform(X_train)
X_test = sc.transform(X_test)
