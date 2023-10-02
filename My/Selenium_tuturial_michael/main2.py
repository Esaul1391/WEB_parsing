import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

# Генерируем случайный User-Agent
useragent = UserAgent()
user_agent = useragent.random

# Опции Chrome WebDriver
chrome_options = ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")

# Инициализируем WebDriver и настраиваем ждущее ожидание
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# URL для парсинга
url = "https://www.thingiverse.com/"

# Функция для записи данных в JSON
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

try:
    driver.get(url)
    next_page = True

    while next_page:
        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'SearchResult__searchResultItem--ktZn0')))

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
            next_button = driver.find_element(By.CLASS_NAME, 'Pagination__right--fIUIM')
            ActionChains(driver).move_to_element(next_button).click().perform()
            time.sleep(2)  # Можно использовать ожидание, если необходимо
        except Exception as e:
            print(e, 'Error here')
            next_page = False

except Exception as ex:
    print(ex)
finally:
    driver.quit()