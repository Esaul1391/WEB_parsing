import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


class AvitoParse:
    def __init__(self, url: str, items: list, count=100, version_main=None):
        self.url = url
        self.items = items
        self.count = count
        self.version = version_main

    def __set_up(self):
        self.driver = uc.Chrome(version_main=self.version)  # write my version

    def __get_url(self):
        self.driver.get(self.url)

    def __paginator(self):
        while self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button/next]"):  # don't add count
            self.__parse_page()
            self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/next]").click()

    def __parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='styles-module-root']").text  #  * ставится когда требуется примерно сказать название элемента
            link = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
            print(name, description, link, price)


    def parse(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()
        self.__parse_page()


if __name__ == '__main__':
    AvitoParse(url='https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать',
               count=2,
               version_main=116,
               items=['3d печать']
               ).parse()

