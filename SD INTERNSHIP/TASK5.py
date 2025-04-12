import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.snapdeal.com/products/mobiles'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

with open('snapdeal_mobiles.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Product Name', 'Price', 'Rating'])

    products = soup.find_all('div', class_='product-tuple-listing')

    for product in products:
        name = product.find('p', class_='product-title').get_text(strip=True)

        price = product.find('span', class_='lfloat product-price').get_text(strip=True).replace('₹', '').strip()

        rating_tag = product.find('span', class_='product-rating')
        rating = rating_tag.get_text(strip=True) if rating_tag else 'No Rating'

        writer.writerow([name, price, rating])

print("✅ Scraping complete! Data saved to 'snapdeal_mobiles.csv'.")
