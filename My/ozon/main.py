import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
# Установите минимальное и максимальное время задержки
min_delay = 1
max_delay = 3

def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

def get_url(url):
    useragent = UserAgent()

    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)
    driver.get(url)
    time.sleep(random.uniform(min_delay, max_delay))

    return driver

def parse_page(driver):
    try:
        # Реализуйте здесь вашу логику парсинга
        # Например, найдите элементы и выполните действия
        names = driver.find_elements(By.CLASS_NAME, 'tile-hover-target.ir3.r3i')
        for name in names[2]:
            time.sleep(random.uniform(min_delay, max_delay))
            name.click()
            time.sleep(random.uniform(min_delay, max_delay))
            driver.back()

    except (TimeoutException, NoSuchElementException) as ex:
        print(f"Произошло исключение: {ex}")
    finally:
        driver.close()
        driver.quit()

def main():
    url = 'https://www.ozon.ru/search/?from_global=true&text=пылеотводы'
    open_page = get_url(url)
    parse_page(open_page)

if __name__ == "__main__":
    main()