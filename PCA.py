import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

dataset = pd.read_csv('Wine.csv')

X=dataset.iloc[: , 0:13 ].values

y=dataset.iloc[:,13].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size= 0.2 , random_state=0)

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()

X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)

from sklearn.decomposition import PCA

pca=PCA(n_components= 2)

X_train=pca.fit_transform(X_train)

X_test=pca.transform(X_test)

#explained_varience = pca.explained_variance_ratio_