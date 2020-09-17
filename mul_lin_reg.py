import numpy as np
import pandas  as pd


dataset= pd.read_csv('50_Startups.csv')

X=dataset.iloc[: , 0:4].values
y=dataset.iloc[: , 4].values



from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer


lb= LabelEncoder()
X[:,3]=lb.fit_transform(X[:, 3])
ct = ColumnTransformer([("Country", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)
X=X[:,1:6]

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test=train_test_split(X, y , test_size=0.2, random_state=0)






from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)


from sklearn.decomposition import PCA

pca=PCA(n_components= 2)

X_train=pca.fit_transform(X_train)

X_test=pca.transform(X_test)

#explained_varience = pca.explained_variance_ratio_

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, y_train)


y_pred=regressor.predict(X_test)


import keras
 
from keras.models import Sequential 

from keras.layers import Dense

from keras.layers import Dropout



classifier = Sequential()

classifier.add(Dense(output_dim=5, init='uniform' , activation = 'relu' , input_dim=2))
#classifier.add(Dropout(p=0.1))

classifier.add(Dense(output_dim=5, init='uniform' , activation = 'relu' ))
#classifier.add(Dropout(p=0.1))

classifier.add(Dense(output_dim=1, init='uniform' ))

classifier.compile(optimizer ='adam' , loss= 'binary_crossentropy' , metrics=['accuracy'])  

classifier.fit(X_train, y_train , batch_size=2 , nb_epoch=500)



from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
y_pred1=classifier.predict(X_test)

hoho=sc1.fit_transform(y_test.reshape(-1,1))
y_pred2=sc1.inverse_transform(y_pred1)



