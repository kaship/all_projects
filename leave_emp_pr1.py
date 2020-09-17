import pandas as pd
import numpy as np
dataset=pd.read_csv('hr_data.csv')
dataset.columns
dataset.describe()
dataset.info()

dataset2=pd.read_excel('employee_satisfaction_evaluation.xlsx')

df=dataset.set_index('employee_id').join(dataset2.set_index('EMPLOYEE #'))

df=df.reset_index()
df.isnull().sum()
df1=df.iloc[:,1:12]
neworder=[0,1,2,3,5,6,7,8,9,4,]
df1=df1[df1.columns[neworder]]
X=df1.iloc[:,0:9].values
y=df1.iloc[:,-1].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
imputer.fit(X[: , 7:9])
X[: , 7:9]= imputer.transform(X[: , 7:9])


from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer

lb= LabelEncoder()
X[:, 5]=lb.fit_transform(X[:, 5])
ct = ColumnTransformer([("catsale", OneHotEncoder(), [5])], remainder = 'passthrough')
X = ct.fit_transform(X)
X=X[:, 1:19]

lb1= LabelEncoder()
X[:,14]=lb1.fit_transform(X[:, 14])
ct1= ColumnTransformer([("catsale", OneHotEncoder(), [14])], remainder = 'passthrough')
X = ct1.fit_transform(X)
X=X[:, 1:19]




from sklearn.model_selection import train_test_split
X_train,X_test, y_train , y_test=train_test_split(X,y , test_size=0.2, random_state=0)






pdx1=pd.DataFrame(X_train)
pdx2=pd.DataFrame(X_test)

neworder1=[0,1,2,3,4,5,6,7,8,9,10,14,15,11,12,13,16,17,]
pdx1=pdx1[pdx1.columns[neworder1]]
pdx2=pdx2[pdx2.columns[neworder1]]


pdx1.isnull().sum()



X_train=pdx1.values
X_test=pdx2.values


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:,13:18]=sc.fit_transform(X_train[:,13:18])

X_test[:,13:18]=sc.fit_transform(X_test[:,13:18])



from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X_train, y_train)





y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score
print("Accuracy (0:.2f)%".format(100*accuracy_score(y_pred,y_test)))





import keras
 
from keras.models import Sequential 

from keras.layers import Dense


classifier = Sequential()

classifier.add(Dense(output_dim=9, init='uniform' , activation = 'relu' , input_dim=18))

classifier.add(Dense(output_dim=9, init='uniform' , activation = 'relu' ))

classifier.add(Dense(output_dim=1, init='uniform' , activation = 'sigmoid'))

classifier.compile(optimizer ='adam' , loss= 'binary_crossentropy' , metrics=['accuracy'])  

classifier.fit(X_train, y_train , batch_size=10 , nb_epoch=100)

y_pred = classifier.predict(X_test)




y_pred1=(y_pred > 0.6)
cm1=confusion_matrix(y_test,y_pred1)



from sklearn.externals import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(classifier, 'kaship.pkl') 




 












