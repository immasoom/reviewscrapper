from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from urllib.request import urlopen as uReq

url=requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")



flipkart_html = bs(url.text, "html.parser")
#print(type(flipkart_html))
#print(flipkart_html)

#table = flipkart_html.find_all("table",class_='wikitable sortable')[0]

table = flipkart_html.find_all("table",class_='wikitable sortable')[0]

column_data = table.findAll('tr')

#print(column_data[1].findAll('td'))

#for i in column_data[1].findAll('td'):
#    #print(i)
#    #print(i.find('a'))
#    for j in i.findAll('a'):
#        print(j)
        #print(j['href'])
    #print(i.findAll('a').get('href'))
    #print(i.a)
#row_data=row.findAll('td')


for i in column_data[1].findAll('td'):
    #print(i.a)
    if i.a == None:
        continue
    else:
        print(i.a['href'])

    #print(type((i.a)))