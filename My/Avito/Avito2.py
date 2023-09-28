import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
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
        time.sleep(sek)
        name = driver.find_elements(By.XPATH, "//h3[@itemprop='name']")
        for item in range(0, 3):
            time.sleep(sek)

            name[item].click()
            time.sleep(sek)

            time.sleep(sek)
            driver.switch_to.window(driver.window_handles[1])
            title = driver.find_element(By.CSS_SELECTOR, '[data-marker="item-view/title-info"]').text
            views = driver.find_element(By.CSS_SELECTOR, '[data-marker="item-view/total-views"]').text
            print(title, views)
            time.sleep(sek)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(sek)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def pagination(driver):
    pagiation_page = driver.find_elements(By.CSS_SELECTOR, '[class*="styles-module-listItem-_La42"]')  # don't add count
    pag = int(pagiation_page[-2].text)
    time.sleep(sek)
    driver.close()
    return pag
def main():
    count_url = 1
    url = f'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p={count_url}&q=3d+печать'
    count_url = pagination(get_url(url))
    for item in range(1, count_url + 1):
        url = f'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p={item}&q=3d+печать'
        parse_page(get_url(url))



if __name__ == "__main__":
    main()
