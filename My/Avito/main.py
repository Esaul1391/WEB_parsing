import undetected_chromedriver as uc

driver = uc.Chrome(version_main=116)  # wride my version
driver.get('https://avito.ru')


class AvitoParse:
    def __init__(self, url: str, items: list, count=100, version_main=None):
        self.url = url
        self.items = items
        self.count = count
        self.version = version_main

    def __set_up(self):
        ...

    def __paginstor(self):
        pass

    def __parse_page(self):
        pass

    def parse(self):
        pass
