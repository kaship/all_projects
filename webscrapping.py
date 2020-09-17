from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

myurl='https://in.tradingview.com/markets/stocks-india/sectorandindustry-sector/commercial-services/'

uClient = uReq(myurl)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div" ,{"class":"tv-screener__content-pane"})

print(len(containers))
a1= soup.prettify(containers[0])

container=containers[0]
a2=container.findAll("a" )

a4=[]

for i in range(0,len(a2)):
    a4.append(a2[i].text)
 
    
    
    
a5=[]    
for i in range(0,len(a4)):
    if i%2==0:
        a5.append(a4[i])
    else:
        continue


a7 = list(dict.fromkeys(a6))