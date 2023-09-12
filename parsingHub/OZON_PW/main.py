import time

from playwright.sync_api import sync_playwright


class OzonSellerParse:
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.list_seller_name = []

    def __page_down(self):
        self.page.evaluate('''
                                        const scrollStep = 200; // Размер шага прокрутки (в пикселях)
                                        const scrollInterval = 100; // Интервал между шагами (в миллисекундах)

                                        const scrollHeight = document.documentElement.scrollHeight;
                                        let currentPosition = 0;
                                        const interval = setInterval(() => {
                                            window.scrollBy(0, scrollStep);
                                            currentPosition += scrollStep;

                                            if (currentPosition >= scrollHeight) {
                                                clearInterval(interval);
                                            }
                                        }, scrollInterval);
                                    ''')

    def _get_sellet_name(self, url: str):
        self.page2 = self.context.new_page()
        self.page2.goto(url=url)



    def __get_links(self):
        self.page.wait_for_selector('#paginatorContent')
        self.__page_down()
        self.page.wait_for_selector(f':text("Дальше")')

        search_resault = self.page.query_selector('#paginatorContent')
        links = search_resault.query_selector_all('.tsBody500Medium')  # if class put point
        print(len(links))

        for count, link in enumerate(links):
            if count > 5:
                break
            url = 'https://ozon.ru' + link.get_attribute('href')
            self._get_sellet_name(url)

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
