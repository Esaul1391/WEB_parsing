from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from fake_useragent import UserAgent



useragent = UserAgent()
                                #   options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

url = "https://www.avito.ru/moskva/velosipedy?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLJSKk4sS02JL05NLErOULKuBQQAAP__IWhYLCkAAAA&q=велосипед+shulz"
driver = webdriver.Chrome(options=options)     #   write path connect webdriver

                                #   general block
try:
    driver.get(url)
    # print(driver.window_handles)
    print(driver.current_url)
    time.sleep(5)
    items = driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")      #   кликаю по картинке
    items[0].click()
    # print(driver.window_handles)
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])        #  переключаю на другую страницу
    time.sleep(3)
    print(driver.current_url)       #       пишу url
    username = driver.find_element(By.CLASS_NAME, 'styles-module-size_ms-EVWML')
    print(username.text)
    driver.close()      #   закрываю страницу
    driver.switch_to.window(driver.window_handles[0])       #       переключаю на первую страницу

    items[1].click()        #   кликаю по второй найденой ссылки
    time.sleep(4)

    driver.switch_to.window(driver.window_handles[1])       #
    div_element = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")       #

    # Extract the text from the span element inside the div
    name = div_element.find_element(By.TAG_NAME, "span").text       #
    print(name)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:                        # important close proces
    driver.close()
    driver.quit()