from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from fake_useragent import UserAgent
import pickle


useragent = UserAgent()
                                #   options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

#   headless mode
# options.add_argument("--headless")  #   method 1
options.headless = True               #   method 2


url = "https://vk.com/"
driver = webdriver.Chrome(options=options)     #   write path connect webdriver

                                #   general block
try:
    pass

except Exception as ex:
    print(ex)
finally:                        # important close proces
    driver.close()
    driver.quit()