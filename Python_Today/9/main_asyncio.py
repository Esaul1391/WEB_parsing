import time
import requests
from bs4 import BeautifulSoup
import datetime
import csv
import json
import asyncio
import aiohttp



async def get_page_data():
    pass

async def gather_data():
    pass


def main():
    pass


if __name__ == "__main__":
    main()

def get_dat():
    cur_data = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"labirint_{cur_data}.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Название книги",
                "Автор",
                "Издательство",
                "Цена со скидкой",
                "Цена без скидки",
                "Процент скидки",
                "Наличие на складе"
            )
        )

    url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    page_count = int(soup.find_all(class_="pagination-number__text")[-1].text)


    sp_books_data = []
    for page in range(1, page_count + 1):
        url = f'https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table&page={page}'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        books_items = soup.find('tbody', class_="products-table__body").find_all("tr")

        for bi in books_items:

            books_data = bi.find_all("td")
            try:
                book_title = books_data[0].find("a").text.strip()

            except:
                book_title = "not find"

            try:
                book_author = books_data[1].text.strip()
            except:
                book_author = "not find"

            try:
                book_publishing = books_data[2].find_all('a')
                book_publishing = ": ".join([bp.text for bp in book_publishing])
            except:
                book_publishing = "not find"

            try:
                book_new_price = books_data[3].find("div", class_="price").find("span").find(
                    "span").text.strip().replace(" ", '')
            except:
                book_new_price = "not find"

            try:
                book_old_price = books_data[3].find('span', class_="price-gray").text.strip().replace(" ", '')
            except:
                book_old_price = "not find"
            try:
                book_sale = round(((book_old_price - book_new_price) / book_old_price) * 100)
            except:
                book_sale = "not find"

            try:
                book_status = books_data[-1].text.strip()
            except:
                book_status = "not find"


            # print(book_title)
            # print(book_author)
            # print(book_publishing)
            # print(book_new_price)
            # print(book_old_price)
            # print(book_sale)
            # print(book_status)

            sp_books_data.append(
                {
                    'book_title': book_title,
                    'book_author': book_author,
                    'book_publishing': book_publishing,
                    'book_new_price': book_new_price,
                    'book_old_price': book_old_price,
                    'book_sale': book_sale,
                    'book_status': book_status
                }
            )

            with open(f"labirint_{cur_data}.csv", "a") as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                    book_title,
                    book_author,
                    book_publishing,
                    book_new_price,
                    book_old_price,
                    book_sale,
                    book_status
                    )
                )
        print(f"processed {page}/{page_count}")
        time.sleep(1)

    with open(f"labirint_{cur_data}.json", 'w') as file:
        json.dump(sp_books_data, file, indent=4, ensure_ascii=False)
def main():
    get_dat()


if __name__ == "__main__":
    main()
