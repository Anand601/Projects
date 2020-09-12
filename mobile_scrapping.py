# Installing and importing all necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
list_brand=["Realme","Motorola","Samsung","Mi","Apple"]

list_3 = []

for brand in list_brand:
   print(brand)
   url = (
      "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_1_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=183554e9-9727-4e1e-914e-42082a41df19&as-searchtext=m&p%5B%5D=facets.brand%255B%255D%3D{}&sort=price_{}").format(
      brand, "desc")

   r = requests.get(url)  # to send the request of url

   htmlcontent = r.content  # to fetch html content

   soup = BeautifulSoup(htmlcontent, 'html.parser') # here we will parse our html content

   products = []
   prices = []
   features = []

   for i in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
      # here we will fetch our product name
      name = i.find('div', attrs={'class': '_3wU53n'})
      products.append(name.text)

      # here we will be fetching price of the product
      price = i.find('div', attrs={'class': '_1vC4OE _2rQ-NK'}).text.replace('₹', ' ').strip()
      prices.append(price)

      # here we will be fetching feature of the product
      fea = i.find('div', attrs={'class': '_3ULzGw'})
      features.append(fea.text)


   # here we  will append all list in list1
   list_1 = [products, prices, features]

   # here we transpose list1 and save it in list2
   list_2 = pd.DataFrame(list_1).transpose()

   # here we will add column name to list2
   list_2.columns = ["Product_Names", "Product_Prices", "Product_Features"]

   # here we fetch top 5 mobile of particular brand
   data = list_2.head(5)
   print(data)
   list_3.append(data) # here we will append all dataframe of all mobile's brand

result = pd.concat(list_3) # here concate all the datframe

result.reset_index(drop=True, inplace=True) # here we will fix index
print(result)

result.to_csv("Top_20_mobile_data.csv") # here we save our data in csv format



