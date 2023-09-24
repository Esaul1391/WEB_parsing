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

#       disable webdriwer mode
options.add_argument("--disable-blink-features=AutomationControlled")
url = "https://vk.com/"
driver = webdriver.Chrome(options=options)     #   write path connect webdriver

                                #   general block
try:
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')   #  опреляет что работаем из под вебдрайвера
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:                        # important close proces
    driver.close()
    driver.quit()