from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
from fake_useragent import UserAgent
import json

with open('data.json', 'w') as f:
    json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        #   First we load existing data into a dict
        file_data = json.load(file)
        #   Join new_data with file_data inside emp_details
        file_data.append(new_data)
        #   Sets file's current position at offset
        file.seek(0)
        #   convert back to json.
        json.dump(file_data, file, indent=4)

useragent = UserAgent()
                                #   options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

url = "https://www.thingiverse.com/"
driver = webdriver.Chrome(options=options)     #   write path connect webdriver

                                #   general block
try:
    next_page = False
    driver.get(url=url)
    while not next_page:

        time.sleep(3)
        items = driver.find_elements(By.CLASS_NAME, 'SearchResult__searchResultItem--ktZn0')
        for item in items:
            img = 'No found'
            try:
                img = item.find_element(By.CLASS_NAME, 'ThingCardBody__cardBodyWrapper--BLLzJ').find_element(By.TAG_NAME, 'img').get_attribute('src')
            except:
                pass

            link = item.find_element(By.CLASS_NAME, 'ThingCardBody__cardBodyWrapper--BLLzJ').get_attribute('href')
            title = item.find_element(By.CLASS_NAME, 'ThingCardHeader__cardNameWrapper--VgmUP').text
            feedback = item.find_element(By.CLASS_NAME, 'CardActionItem__itemContainer--Jjw5X').find_element(By.CLASS_NAME, 'CardActionItem__text--Regp7').text
            print(title, feedback)
            print(img)
            print(link)

            write_json({
                "title": title,
                "img": img,
                "link": link
            })
        try:
            driver.find_element(By.CLASS_NAME, 'Pagination__right--fIUIM').click()
            time.sleep(4)
        except Exception as e:
            print(e, 'Error hear')
            next_page = True

except Exception as ex:
    print(ex)
finally:                        # important close proces
    driver.close()
    driver.quit()

