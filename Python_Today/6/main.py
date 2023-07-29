import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def get_data(url):
    r = requests.get(url=url)

    with open("index.html", "w") as file:
        file.write(r.text)

    soup = BeautifulSoup(r.text, 'lxml')
    hotels_card = soup.find_all('div', class_="reviews-travel__item")

    for hotel_url in hotels_card:
        h_url = hotel_url.find("a").get("href")
        print(h_url)


def get_data_with_selenium(url):

    try:
        with webdriver.Chrome() as browser:
            browser.get('url')
            time.sleep(2)
            with open("index_selenium.html", "w") as file:
                file.write(browser.page_source)


    except Exception as ex:
        print(ex)



def main():
    #get_data("https://tury.ru/hotel/most_luxe.php")
    get_data_with_selenium("https://tury.ru/hotel/most_luxe.php")


if __name__ == '__main__':
    main()
