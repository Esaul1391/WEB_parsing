import requests
import re
import csv
from models import Items

class ParseWB():
    def __init__(self, url:str):
        self.url = url


    @staticmethod
    def __get_brand_id__(url:str):
        pass

    def parse(self):
        self.__create_csv()
        # while True:
        # headers = {
        #     'Accept': '*/*',
        #     'Accept-Language': 'en-US,en;q=0.9',
        #     'Connection': 'keep-alive',
        #     'Origin': 'https://www.wildberries.ru',
        #     'Referer': 'https://www.wildberries.ru/brands/msi',
        #     'Sec-Fetch-Dest': 'empty',
        #     'Sec-Fetch-Mode': 'cors',
        #     'Sec-Fetch-Site': 'cross-site',
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        #     'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Linux"',
        # }

        response = requests.get(
            'https://catalog.wb.ru/brands/m/catalog?appType=1&brand=27445&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&sort=rate&spp=0',
                    )
        items_info = Items.model_validate(response.json('data'))
        self.__save_csv(items_info)

    def __create_csv(self):
        with open("wb_data.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'название', 'цена', 'бренд', 'продаж', 'рейтинг', 'в наличие'])

    def __save_csv(self, items):
        with open("wb_data.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            for product in items.products:
                writer.writerow([product.id,
                                 product.name,
                                 product.salePriceU,
                                 product.brand,
                                 product.sale,
                                 product.rating,
                                 product.volume])





if __name__ == "__main__":
    ParseWB('https://www.wildberries.ru/brands/msi?sort=rate&page=2').parse()