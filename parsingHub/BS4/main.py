from bs4 import BeautifulSoup
import lxml
import requests

def parser(url:str):
    list_product = []
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'lxml')
    products = soup.find_all("div", class_='product-card oneclick-enabled')
    for product in products:
        name = product.get('data-product-name')
        code = product.find('span', class_ = 'product-card__key').text
        link = product.find('div', class_="product-card__img-container").find('a').get('href')
        price = product.find('span', itemprop='price').get('content')
        # list_product.append(Produc)
def create_csv():
    ...

def write_scv():
    pass

if __name__ == "__main__":
    parser(url='https://glavsnab.net/santehnika/smesiteli.html')
