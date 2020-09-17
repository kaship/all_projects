import pandas as pd

dataset=pd.read_excel('Book1.xlsx')
dataset.head(10)


t=dataset.describe()

info=dataset.info()

a=[1,2,4,6,2,3,4]
df=pd.DataFrame(a)

dict1=pd.DataFrame({'http_status':[200,300,400,300,600], 'responce_time':[1,2,3,4,5] })

dataset.columns
dataset[['age']].mean(axis=0)
dataset.mean(numeric_only=True)

#filters
count1=dataset[dataset['branch']=='com']
count2=count1[count1['gender']=='girl']
count3=count2[count2['age']==18]
count3.count()

#tocheck  null function
dataset.isnull()
dataset['sex'].isnull()
dataset1213=(dataset['age'] > 60) | (dataset['age'] < 5)
dataset[dataset1213]















#new dataset
dataset=pd.read_csv('amazon_fires.csv' , encoding="ISO-8859-1")

dataset.tail()

len(dataset['estado'].unique())

newcolumn={'ano' : 'year',
            'estado' : 'state' ,
             'mes': 'month' ,
              'numero' : 'number-of-fire' ,
               'encontro' : 'date'}


dataset.rename(columns = newcolumn , inplace=True)



dataset.head()


dataset['year'].unique()
dataset.info()



neworder=[4,1,0,2,3,]

dataset=dataset[dataset.columns[neworder]]



dataset['number-of-fire'].str.isnumeric()




dataset['number-of-fire'].str.isdigit()




dataset[dataset['number-of-fire'].astype(str).str.isnumeric()]



dataset['number-of-fire'] = dataset['number-of-fire'].str.strip("Fires")




dataset['number-of-fire'] = dataset['number-of-fire'].str.replace(' ' , '0').astype(float)





#creating copy of dataframe
dataset_copy=dataset.copy()

#getting number of null values 
dataset.isnull().sum()


#to drop the values with null values
dataset=dataset.dropna()
dataset= dataset.reset_index()

#to make every word capital
dataset['state'] =dataset['state'].str.title()


#to make groups of dataset basically aggregation     

state_group= dataset.groupby('state')


state_group1= state_group.get_group('Rio')




state_group.size()

state_group.sum()

state_group.mean()


#pivot tables
import numpy as np

fire=dataset.pivot_table(values='number-of-fire' , index='state' , aggfunc=np.mean , margins=True)
max1= fire['number-of-fire'].max()  +10
 

fire.plot(kind='barh' , title='fire by stste' , xlim=(0,max1) , legend=False)


#to  insert a new column
dataset['newclmn']=np.random.randint(1,5,dataset.shape[0])


pd.DataFrame(dataset.groupby('state')['month'])




#time and date series

from datetime import datetime


df=pd.date_range(start='11/01/2019', end='11/07/2019' , freq='H')

df=pd.DataFrame(df , columns=['date'])

df['sales'] = np.random.randint(0,1000 , size=(len(df)))


df=df.set_index('date')


df.loc['2019-11-01 03:00:00' , 'sales']


#map 
num = [1,2,3,4,5]

def square(x):
    return x**2

x=map(square , num)

y=list(x)


#filter
evod=[1,2,3,4,5,6,7,8,9]
def even(x):
    return x % 2 ==0
y2=list(filter(even,evod))



















