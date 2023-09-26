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
        for item in range(0, len(name) - 1):
            time.sleep(sek)

            name[item].click()
            time.sleep(sek)

            time.sleep(sek)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(sek)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(sek)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    url = 'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать'
    open_page = get_url(url)
    parse_page(open_page)



if __name__ == "__main__":
    main()
