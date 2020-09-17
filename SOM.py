import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

dataset = pd.read_csv("Credit_Card_Applications.csv")

X=dataset.iloc[: , :-1].values
y=dataset.iloc[: , -1].values

from sklearn.preprocessing import MinMaxScaler
sc= MinMaxScaler(feature_range = ( 0 , 1 ))
X= sc.fit_transform(X)


from minisom import  MiniSom
som= MiniSom(x=10 , y=10 , input_len =15 , sigma=1.0 , learning_rate= 0.5)
som.random_weights_init(X)
som.train_random(data = X , num_iteration = 100)

from pylab import bone , pcolor , colorbar , plot , show
bone()
pcolor(som.distance_map().T)
colorbar()

markers=['o' , 's']
colors=['r' , 'g']

for i , x in enumerate(X):
    w= som.winner(x)
    plot(w[0] + 0.5,
         w[1] +0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor='None',
         markersize=10,
         markeredgewidth=2
        )
show()    

mapping=som.win_map(X)
frauds=np.concatenate((mapping[(8,9)] , mapping[(7,9)]) , axis=0)

frauds= sc.inverse_transform(frauds)

X1=dataset.iloc[: , :-1].values

X2=X1
froud1=[]
for i in frauds:
    froud1.append(i[0])
    
froud2=[]    
for t in X1:
    froud2.append(t[0])

fofo=[]

for u in froud2:
    if u in froud1:
        fofo.append(1)
    else:
        fofo.append(0)

dataset['frauds'] = fofo

    