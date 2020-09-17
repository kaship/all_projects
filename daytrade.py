

import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


yahoo_financials = YahooFinancials('TSLA')

data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
                                                  end_date='2019-12-31', 
                                                  time_interval='daily')


tsla_df = pd.DataFrame(data['TSLA']['prices'])

tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
open1=tsla_df.iloc[:,2].values
close1=tsla_df.iloc[:,3].values


d=[]
dp=[]
dp1=[]
dp2=[]
dp3=[]

    
    
for i in range(0,len(open1)-1) :
    op=open1[i+1]
    cl=close1[i]
    d.append(op-cl)
    diff= d[i]/close1[i]   
    dp.append(diff*100)
    if diff*100 > 2 and diff*100 <8:
        dp1.append(tsla_df.iloc[:,1].values[i+1])
        val1 = open1[i+1]  - tsla_df.iloc[:,1].values[i+1] 
        cl2=cl*0.70
        val2 = op - cl
        if val1 > val2:
            dp2.append("win")
        else:
            dp2.append("loose")
            
    elif diff*100 > -8 and diff*100 <-2:
       #dp1.append(tsla_df.iloc[:,0].values[i+1])
        val1 =  tsla_df.iloc[:,0].values[i+1]  - open1[i+1]  
        cl2=cl*0.70
        val2 =  cl -op
        if val1 > val2:
            dp3.append("win")
        else:
            dp3.append("loose")        
    else:
        continue
  

dp3=[]
    
tick_list=a7

for tick in tick_list:
    yahoo_financials = YahooFinancials(tick)
    print("bitch121")
    data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
                                                      end_date='2019-12-31', 
                                                      time_interval='daily')
    
    print("bitch222")
    try:
      tsla_df = pd.DataFrame(data[tick]['prices'])
     
    except :
        print("bitch")
        continue
    
    tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
    open1=tsla_df.iloc[:,2].values
    close1=tsla_df.iloc[:,3].values
    
    
    d=[]
    dp=[]
    dp1=[]
    dp2=[]
   
        
        
    for i in range(0,len(open1)-1) :
        op=open1[i+1]
        cl=close1[i]
        d.append(op-cl)
        diff= d[i]/close1[i]   
        dp.append(diff*100)
        if diff*100 > 2 and diff*100 <8:
            dp1.append(tsla_df.iloc[:,1].values[i+1])
            val1 = open1[i+1]  - tsla_df.iloc[:,1].values[i+1] 
            cl2=cl*0.50
            val2 = op - cl
            if val1 > val2:
                dp2.append("win")
            else:
                dp2.append("loose")
                
        elif diff*100 > -8 and diff*100 <-2:
           #dp1.append(tsla_df.iloc[:,0].values[i+1])
            val1 =  tsla_df.iloc[:,0].values[i+1]  - open1[i+1]  
            cl2=cl*0.50
            val2 =  cl -op
            if val1 > val2:
                dp3.append("win")
            else:
                dp3.append("loose")        
        else:
            continue
      
    print("yaaa bitch")
    
    







  
  