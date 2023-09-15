import csv

from bs4 import BeautifulSoup
import lxml
import requests
from  model import Product
def parser(url:str):
    create_csv()
    list_product = []
    src = requests.get(url=url)
    soup = BeautifulSoup(src.text, 'lxml')
    page_len = int(soup.find_all('a', class_="pagination--link")[-2].text)  # find volume pagination
    print(page_len)
    for page in range(1, 36):
        res = requests.get(f'{url}&p={page}')   #
        soup = BeautifulSoup(res.text, 'lxml')
        products = soup.find_all("div", class_='product-card oneclick-enabled')     # find kart with product
        #   find data product
        for product in products:
            name = product.get('data-product-name')
            code = product.find('span', class_ = 'product-card__key').text
            link = product.find('div', class_="product-card__img-container").find('a').get('href')
            price_elem= product.find('span', itemprop='price')
            if price_elem:
                price = price_elem.get("content")
            else:
                price = "По запросу"
            list_product.append(Product(code=code,
                                        name=name,
                                        link=link,
                                        price=price ))
    write_scv(list_product)

def create_csv():
    with open(f'glavsnab.csv', mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            'code',
            'name',
            'link',
            'price'
        ])

def write_scv(products: list[Product]):
    with open(f'glavsnab.csv', mode='a', newline="") as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([
                product.code,
                product.name,
                product.link,
                product.price
                ])

if __name__ == "__main__":
    parser(url='https://glavsnab.net/santehnika/smesiteli.html?limit=100')
