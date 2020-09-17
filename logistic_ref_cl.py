import numpy as np
import pandas as pd

dataset = pd.read_csv('Social_Network_Ads.csv')

X=dataset.iloc[:, 1:-1].values
y=dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer

lb= LabelEncoder()
X[:,0]=lb.fit_transform(X[:, 0])
ct = ColumnTransformer([("Gender", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)


X=X[:,1:4]


from sklearn.model_selection import train_test_split
X_train,X_test, y_train , y_test=train_test_split(X,y , test_size=0.2, random_state=0)





from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:,1:3]=sc.fit_transform(X_train[:,1:3])
X_test[:,1:3]=sc.fit_transform(X_test[:,1:3])


from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X_train, y_train)


from sklearn.neighbors import KNeighborsClassifier

classifier=KNeighborsClassifier(n_neighbors=5 , metric='minkowski', p=2)
classifier.fit(X_train, y_train)




from sklearn.svm import SVC
classifier=SVC(kernel='linear' , random_state=0 )
classifier.fit(X_train,y_train)



from sklearn.svm import SVC
classifier=SVC(kernel='rbf' , random_state=0 )
classifier.fit(X_train,y_train)


from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy' , random_state=0)
classifier.fit(X_train, y_train)




from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=10,criterion='entropy' , random_state=0)
classifier.fit(X_train, y_train)














y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
