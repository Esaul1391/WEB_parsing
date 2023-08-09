import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import lxml
import json

ua = UserAgent()
print(ua.random)
def collect_data():
    # response = requests.get(url=url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type={cat_type}&withStack=true')
    #
    # with open('result.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)
    offset = 0
    batch_size = 60

    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type=&withStack=true'
            response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})

            offset += batch_size

            data = response.json()
            items = data.get('items')


                    


def main():
    collect_data()


if __name__ == "__main__":
    main()
