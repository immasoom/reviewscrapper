from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from urllib.request import urlopen as uReq

#url=requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")

uClient = uReq("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
Page    = uClient.read()
#print(Page)
uClient.close()

flipkart_html = bs(Page, "html.parser")
#print(flipkart_html)

#table = flipkart_html.find_all("table",class_='wikitable sortable')[0]

table = flipkart_html.find_all("table",class_='wikitable sortable')[0]
print(table)


