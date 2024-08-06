from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from urllib.request import urlopen as uReq

#url=requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")

uClient = uReq("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
Page    = uClient.read()
#print(Page)
uClient.close()

soup = bs(Page, "html.parser")

#print(url) # this will give response object

#soup.find_all()
#print(soup.prettify())
table = soup.find_all("table",class_='wikitable sortable')[0]
#print(table.findAll("th"))  #this will give list

l=[]
for i in table.findAll("th"):
    l.append(i.text.strip())
#print(l)

df=pd.DataFrame(columns=l)
#print(df)

m=[]

#rows=table.find('tbody')

#rows=table.findAll('tr')
#print(rows)
column_data = table.findAll('tr')
#print(len(column_data))
#print(column_data[1].findAll('td'))
#print(column_data[2].findAll('td'))

#print(column_data[1].findAll('td'))

"""
for i in column_data[1].findAll('td'):
    m.append(i.text.strip())

print(m)

"""
#for i in range(1,len(column_data)):
    #print(column_data[i].findAll('td'))
    #individual_row_data= [j.text.strip() for j in column_data[i].findAll('td') ]
    #print(individual_row_data)
    #for j in column_data[i].findAll('td'):
    #    m.append(j.text.strip())
    #print(m)
    #m=[]
#for row in column_data:
#    row_data=row.findAll('td')
#    for data in row_data:
#        m.append(data.text.strip())
#    print(m)
#    m=[]
flag=False
for row in column_data:
    row_data=row.findAll('td')
    for data in row_data:
        m.append(data.text.strip())    
    print(m)
    
    if len(m) == 0:
       continue
    else:
       length = len(df)
       df.loc[length] = m

    m=[]    

print(df)

df.to_csv(r"C:\Users\masoo\OneDrive\Desktop\ReviewFlask\companies.csv",index=False)
    







