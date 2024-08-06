from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = requests.get("https://www.flipkart.com/search?q=iphone")
#print(url)
soup=bs(url.text,"html.parser")
#print(soup)

item=soup.find_all("div",class_="cPHDOP col-12-12")

#print(item[2])

#for i in item:
#    print ()
#prod=item[2].find_all("div",class_="tUxRFH")

del item[0:2]
#print (item[0])
page=item[0].find('a')['href']
produrl= "https://www.flipkart.com" + page
#print(produrl)

url1=requests.get(produrl)
soup1=bs(url1.text,"html.parser")
#print(soup1)
commentbox=soup1.find_all("div",class_="_8-rIO3")
cbox=commentbox[1].findAll("div",class_="RcXBOT")

#print(cbox[0].find("div",class_="XQDdHH Ga3i8K").text)  #rating
#print(cbox[0].find("p",class_="z9E0IG").text)          #title

comtag=cbox[0].find_all('div', {'class': ''})  
#print(comtag[1].text)                                  #review

name=cbox[0].find("div",class_="row gHqwa8").p.text
#print(name)
l=[]

df=pd.DataFrame(columns=["rating","title","review","name"])
for i in cbox:
    l.append(i.find("div",class_="XQDdHH Ga3i8K").text)  #rating
    l.append(i.find("p",class_="z9E0IG").text)           #title   

    comtag=i.find_all('div', {'class': ''})           #review
    l.append(comtag[1].text)    

    name=i.find("div",class_="row gHqwa8").p.text     #name
    l.append(name)

    length=len(df)
    df.loc[length] = l

    l=[]

print(df)

df.to_csv(r"C:\Users\masoo\OneDrive\Desktop\ReviewFlask\review_scrapping.csv",index=False)





