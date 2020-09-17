from urllib.error import HTTPError





from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq
from urllib.request import Request

myurl=('https://www.hindustantimes.com/business-news/' )

req = Request(myurl, headers={'User-Agent': 'Mozilla/5.0'})

uClient = uReq(req)

        

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div" ,{"class":"media-heading headingfour"})
containers1 = page_soup.findAll("p")





a5=[]

for i in containers:
    a5.append(i.text)
    
    
    
    
    
    
a6=[]

for i in containers1:
    a6.append(i.text)    
    



from datetime import date 
  
  
# Returns the current local date 
today = date.today() 

today1=str(today)

    
from neo4j import GraphDatabase    
    
graphdb = GraphDatabase.driver(uri = "bolt://neo4j:news1_db@localhost:7687" , auth = ("neo4j" , "news1_db") , encrypted=False)    
    
session=graphdb.session()

q1 = "CREATE (Source1:news{name: 'Hindustan times', date:'2020-05-31'})" 

nodes= session.run(q1)

q2= "CREATE (content1:Business{title: 'Google stake in Voda-Idea could heat up race for digital ecosystem', content:'Google had in January announced a partnership with Bharti Airtel Ltd to extend its G Suite services to Airtel subscribers. '})"

nodes= session.run(q2) 




q3 = "CREATE (Source1)-[r:newsof]->(content1)  Return  Source1 , content1"
nodes= session.run(q3)











    