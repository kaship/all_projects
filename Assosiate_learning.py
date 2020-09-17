import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

dataset = pd.read_csv("C:/Users/user/Downloads/P14-Apriori-Python/Apriori_Python/Market_Basket_Optimisation.csv" , header= None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)


soll=[]
for k in results:
    soll.append(list(k[0]))
ask=input("Product name")        

for n in soll:
    if ask in n:
        #print("hi")
        n.remove(ask)
        for o in n:
            print(o)
        break
    else:
        #print("no")
        continue
