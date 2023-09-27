import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from fake_useragent import UserAgent

second = random.randint(20, 30)
useragent = UserAgent()

options = uc.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome()
def get_url(url):
    driver = uc.get(url)

def main():
    url = "https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать"
    get_url(url)

if __name__ == "__main__":
    main()