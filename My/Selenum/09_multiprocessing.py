from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from fake_useragent import UserAgent
from multiprocessing import Pool         #   библиотека этого урока


useragent = UserAgent()
                                #   options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

url_list = ["https://www.tradeinn.com/trekkinn/ru", 'https://3dtoday.ru/', 'https://www.pepper.ru/']
                                #   general block
def get_data(url):
    try:
        driver = webdriver.Chrome(options=options)  # write path connect webdriver
        driver.get(url=url)
        time.sleep(5)
        driver.get_screenshot_as_file(f'media/{url.split("//")[1]}.png')
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    p = Pool(processes=2)
    #     p.map(get_data, urls_list)