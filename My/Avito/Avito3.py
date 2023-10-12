import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains

import random
import time

sek = random.randrange(1, 3)


def get_url(url):
    useragent = UserAgent()

    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options)
    driver.get(url)
    return driver


def parse_page(driver):
    try:
        next_page = False
        while not next_page:
            name = driver.find_elements(By.XPATH, "//h3[@itemprop='name']")
            for item in range(0, 1):
                time.sleep(sek)

                name[item].click()
                time.sleep(sek)

                time.sleep(sek)
                driver.switch_to.window(driver.window_handles[1])
                # name_seller = driver.find_element(By.NAME, "seller-link/link")
                # print(name_seller)
                time.sleep(sek)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(sek)
            try:
                driver.find_element(By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]').click()
                time.sleep(sek)
            except Exception as e:
                print(e)
                next_page = True
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def pagination(driver):
    pagination_page = driver.find_elements(By.CSS_SELECTOR,
                                           '[class*="styles-module-listItem-_La42"]')  # don't add count
    print(pagination_page[-2].text)
    driver.close()
    return int(pagination_page[-2].text)


def main():
    url = 'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать'
    open_page = get_url(url)
    parse_page(open_page)


if __name__ == "__main__":
    main()
