import numpy as np
import pandas as pd

dataset= pd.read_csv('Mall_Customers.csv' )

X=dataset.iloc[:,1:5].values

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer

lb= LabelEncoder()
X[:,0]=lb.fit_transform(X[:, 0])
ct = ColumnTransformer([("Gender", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)

X=X[:,1:5]


from sklearn.cluster import KMeans

wcss=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i , init='k-means++' , max_iter =300, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
import matplotlib.pyplot as plt
plt.plot(range(1,11), wcss)    
plt.show()

kmeans= KMeans(n_clusters=6 , init='k-means++' , max_iter =300, random_state=0)

y_kmeans= kmeans.fit_predict(X)