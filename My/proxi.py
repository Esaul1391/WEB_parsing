# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()

useragent = UserAgent()


options.add_argument(f'user-agent={useragent.random}')


# set proxi

options.add_argument('--proxi-server=45.12.31.230:80')

driver = webdriver.Chrome(
    options=options
)

try:
    driver.get(url='https://2ip.ru')
    time.sleep(5)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()