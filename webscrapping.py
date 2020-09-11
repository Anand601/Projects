# Installing and importing all necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


url=("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=mobiles&requestId=f028cdb7-b300-428f-8cff-0b760463e257&sort=price_desc")
r=requests.get(url)  #to send the request of url
htmlcontent=r.content   #to fetch html content


soup= BeautifulSoup(htmlcontent,'html.parser') # to parse html content and beautify it in beautifulsoup


products=[] # empty list to store product's name in it.
prices=[] # to store price of product in it
features=[] # to store features in it

for i in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}): # to find all the anchor tag of specific class
   name=i.find('div', attrs={'class':'_3wU53n'})
   products.append(name.text)

   price = i.find('div', attrs={'class': '_1vC4OE _2rQ-NK'}).text.replace('₹', ' ').strip()
   prices.append(price)

   fea = i.find('div', attrs={'class': '_3ULzGw'})
   features.append(fea.text)



c1=[products,prices,features] # append all lists in single list

c2=pd.DataFrame(c1).transpose() # changing row in colummns
c2.columns=["Product_Names","Product_Prices","Product_Features"] # adding columns name
data=c2.head(20) # fetching top 20 products
print(data)
data.to_csv("mobile_data.csv") # saving file in csv format