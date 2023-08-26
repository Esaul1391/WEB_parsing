import pandas as pd
import requests


def get_category():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/muzhchinam/odezhda/bryuki-i-shorty',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get(
        'https://catalog.wb.ru/catalog/men_clothes1/catalog?appType=1&cat=8144&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,22,110,48,71,114&sort=popular&spp=0',
        headers=headers,
    )
    return response.json()


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'sale': product.get('sale', None)
            })
    return products

def main():
    response = get_category()
    products = prepare_items(response)

    pd.DataFrame(products).to_csv('products.csv', index=False)

if __name__ == '__main__':
    main()
