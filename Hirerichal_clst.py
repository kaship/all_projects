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

import scipy.cluster.hierarchy as sch

dendrogram= sch.dendrogram(sch.linkage(X, method='ward'))


from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=6, affinity = 'euclidean' , linkage='ward')
y_hc=hc.fit_predict(X)