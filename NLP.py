
import numpy as np
import pandas as pd
from bert_serving.client import BertClient
client = BertClient()


#dataset=pd.read_csv('Restaurant_Reviews.tsv' , delimiter='\t' , quoting=3)
dataset=pd.read_csv('yoyoreviews.csv')
dataset=dataset.iloc[:,3:5]

import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
corpus=[]
b=0
for i in range(0,16070):
       review=re.sub('[^a-zA-Z]' , ' ' , dataset['content'][i])
       review=review.lower()
       review=review.split()
       ps=PorterStemmer()
       review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
       review= ' '.join(review)
       corpus.append(review)
       b=b+1
       print(b)
a=0
vector1= client.encode([dataset['content'][0]])      
for i in range(0,16069):
    vectors = client.encode([dataset['content'][i+1]])
    vector1 = np.append(vector1 , vectors , axis=0)
    
    a=a+1
    print(a)
    
    
y=dataset.iloc[:,1].values     

y=list(y)     
    
for j in range(0,16070):
    if corpus[i]=="":
        corpus.pop(i)
        y.pop(i)
    else:
        continue
    
    
    
a=0
vector1= client.encode([corpus[0]])      
for i in range(0,16069):
    vectors = client.encode([corpus[i+1]])
    vector1 = np.append(vector1 , vectors , axis=0)
    
    a=a+1
    print(a)    
    
X=vector1
y=np.array(y)
       
from sklearn.feature_extraction.text import CountVectorizer

cv= CountVectorizer(max_features=1500)
X=cv.fit_transform(corpus).toarray()
y=dataset.iloc[:,1]        


from sklearn.model_selection import train_test_split
X_train,X_test, y_train , y_test=train_test_split(X,y , test_size=0.25, random_state=0)


from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)



y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
import pickle
filename = 'finalized_model_nlp_senti.sav'
pickle.dump(regressor, open(filename, 'wb'))


loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
print(classifier.score(X_test, y_test))
cm1=confusion_matrix(y_test1,y_pred2)
y_test1=[]
for l in range(0,3999):
    y_test1.append(float(y_test[l]))
y_test1=np.array(y_test1)    

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

y_pred2=regressor.predict(X_test)
print(regressor.score(X_test, y_test1))

true=[]
for k , m  in  zip(y_test1 , y_pred2):
    if k==m:
        true.append("yes")
    else:
        continue


tutu="i am very happy  with your services"
vec_tutu=client.encode([tutu])  
vec_tutu1=np.append(X_test,vec_tutu , axis=0)   

tryeg=regressor.predict(vec_tutu1)
tryeg[3999]


from numpy import savetxt

savetxt('vector2.csv', vector1, delimiter=',')

from numpy import savetxt

savetxt('y_train.csv', y_train, delimiter=',')


from numpy import savetxt

savetxt('X_train.csv', X_train, delimiter=',')


loaded_model = load_model("‪C:\\Users\\user\\Downloads\\network.h5") 