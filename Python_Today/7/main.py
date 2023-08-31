import time

import requests
import os
from bs4 import BeautifulSoup
import lxml



def get_all_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    # r = requests.get(url="https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/", headers=headers)
    #
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    #
    # with open("data/page_1.html", "w") as file:
    #     file.write(r.text)


    with open("data/page_1.html") as file:
        src = file.read()


    soup = BeautifulSoup(src, 'lxml')
    pages_count = int(soup.find("div", class_=" ").find_all("a")[-2].text)
    for i in range(1, pages_count + 1):
        url = f"https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/?PAGEN_1={i}"

        r = requests.get(url=url, headers=headers)

        with open (f"data/page_{i}.html", "w") as file:
            file.write(r.text)

        time.sleep(2)

        return pages_count + 1


def collct_data(pages_count):

    for page in range(1, pages_count):
        with open(f"data/page_{page}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        items_cards = soup.find_all('a', class_='  ')

        for item in items_cards:
            product_article = item.find()


def main():
    get_all_pages()

if __name__ == "__main__":
    main()

