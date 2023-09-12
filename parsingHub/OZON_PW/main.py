import time

from playwright.sync_api import sync_playwright


class OzonSellerParse:
    def __init__(self, keyword:str):
        self.keyword = keyword
        self.list_seller_name = []

    def __page_down(self):
        pass

    def __get_links(self):
        self.page.wait_for_selector('#paginatorContent')
        self.__page_down()
        self.page.wait_for_selector(f':text("Дальше")')

        seaech_resault = self.page.query_selector()



    def parse(self):
        with sync_playwright() as playwright:
            brwser = playwright.chromium.launch(headless=False)
            self.context = brwser.new_context()
            self.page = self.context.new_page()
            self.page.goto('https://www.ozon.ru/')
            self.page.get_by_placeholder('Искать на Ozon').type(text=self.keyword, delay=0.3)
            self.page.query_selector('button[type="submit"]').click()
            self.__get_links()

if __name__ == '__main__':
    OzonSellerParse('пластик для 3d принтера').parse()
    time.sleep(10)
