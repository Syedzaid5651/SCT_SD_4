import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.snapdeal.com/search?keyword=mobile"  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

product_names = []
product_prices = []
product_ratings = []
limit = 5

for product in soup.find_all('div', class_='product-tuple-description', limit=limit):
    name = product.find('p', class_='product-title').text.strip()
    price = product.find('span', class_='lfloat product-price').text.strip()
    
    rating_tag = product.find('div', class_='filled-stars')
    rating = rating_tag['style'] if rating_tag else 'No rating'
    
    product_names.append(name)
    product_prices.append(price)
    product_ratings.append(rating)

data = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings
})

data.to_csv('snapdeal_products.csv', index=False)

print("Data for 5 products has been saved to snapdeal_products.csv")


#this concept is new for me so i used code with harry youtube channel to learn this  
