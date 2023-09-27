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

url = "https://www.thingiverse.com/"
driver = webdriver.Chrome(options=options)     #   write path connect webdriver

                                #   general block
try:
    driver.get(url=url)
    time.sleep(3)

    items = driver.find_elements(By.CLASS_NAME, 'SearchResult__searchResultItem--ktZn0')

    for item in items:
        title = item.find_element(By.CLASS_NAME, 'ThingCardHeader__cardNameWrapper--VgmUP').text
        feedback = item.find_element(By.CLASS_NAME, 'CardActionItem__itemContainer--Jjw5X').find_element(By.CLASS_NAME, 'CardActionItem__text--Regp7').text
        print(title, feedback)

except Exception as ex:
    print(ex)
finally:                        # important close proces
    driver.close()
    driver.quit()