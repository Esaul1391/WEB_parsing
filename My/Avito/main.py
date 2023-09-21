
import json
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random

second = random.randint(20, 30)
def get_url(url):
    driver = uc.Chrome(version_main=116)  # write my version

    driver.get(url)
    return driver

def paginator(driver):
    pagiation = driver.find_elements(By.CSS_SELECTOR, '[class*="styles-module-listItem-_La42"]')     # don't add count
    print(pagiation[-2].text)
    return int(pagiation[-2].text)
        # __parse_page()
        # driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/next']").click()
        # time.sleep(40)


def parse_page(driver):

    titles = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
    for title in titles:
        name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
        description = title.find_element(By.CSS_SELECTOR, "[class*='styles-module-root']").text  #  * ставится когда требуется примерно сказать название элемента
        link = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
        price = title.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
        print(name, description, link, price)
        # time.sleep(second)
        # drive = get_url(link)
        # time.sleep(second)
        # drive.find_element(By.CSS_SELECTOR, '[data-marker="seller-link/link"]').click()
        # # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        # time.sleep(5)
        # sp = []
        #
        # sp_ad = driver.find_elements(By.CSS_SELECTOR, '[data-marker*="item_list_with_filters"]')
        # for item in sp_ad:
        #     name = item.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
        #     sp.count(name)
        # print(sp)

        # drive.close()

#
# def __save_data(self):
#     with open("items.json", 'w', encoding='utf-8') as f:
#         json.dump(self.data, f, ensure_ascii=False, indent=4)
#
# def parse(self):
#     self.__set_up()
#     self.__get_url()
#     self.__paginator()
#     self.__parse_page()
#
#
def main():
    url = 'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать'
    get = get_url(url)
    count = paginator(get)
    for page in range(1, count + 1): # Сделать закрытие страницы
        url = f'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p={page}&q=3d+печать'
        get = get_url(url)
        parse_page(get)
        time.sleep(second)


if __name__ == '__main__':
    main()
#     AvitoParse(url='https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать',
#                count=2,
#                version_main=116,
#                items=['3d печать']
#                ).parse()
#
#




# import json
#
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
#
#
# class AvitoParse:
#     def __init__(self, url: str, items: list, count=100, version_main=None):
#         self.url = url
#         self.items = items
#         self.count = count
#         self.version = version_main
#         self.data = []
#
#     def __set_up(self):
#         self.driver = uc.Chrome(version_main=self.version)  # write my version
#
#     def __get_url(self):
#         self.driver.get(self.url)
#
#     def __paginator(self):
#         while self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button/next]"):  # don't add count
#             self.__parse_page()
#             self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/next]").click()
#
#     def __parse_page(self):
#         titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
#         for title in titles:
#             name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
#             description = title.find_element(By.CSS_SELECTOR, "[class*='styles-module-root']").text  #  * ставится когда требуется примерно сказать название элемента
#             link = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
#             price = title.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
#             data = {
#                 'name':name,
#                 'descriptions'
#             }
#             self.__save_data()
#             print(name, description, link, price)
#
#     def __save_data(self):
#         with open("items.json", 'w', encoding='utf-8') as f:
#             json.dump(self.data, f, ensure_ascii=False, indent=4)
#
#     def parse(self):
#         self.__set_up()
#         self.__get_url()
#         self.__paginator()
#         self.__parse_page()
#
#
# if __name__ == '__main__':
#     AvitoParse(url='https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать',
#                count=2,
#                version_main=116,
#                items=['3d печать']
#                ).parse()


