# Импортируем необходимые библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
from fake_useragent import UserAgent
import json

# Создаем пустой JSON-файл для хранения данных
with open('data.json', 'w') as f:
    json.dump([], f)

# Функция для добавления данных в JSON-файл
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Загружаем существующие данные в словарь
        file_data = json.load(file)
        # Добавляем новые данные к существующим
        file_data.append(new_data)
        # Устанавливаем текущую позицию файла на начало
        file.seek(0)
        # Записываем обновленные данные в JSON-файл
        json.dump(file_data, file, indent=4)

# Генерируем случайный User-Agent с помощью библиотеки fake_useragent
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

# Указываем URL, с которым будем работать
url = "https://www.thingiverse.com/"

# Инициализируем веб-драйвер Chrome с определенными опциями
driver = webdriver.Chrome(options=options)

try:
    next_page = False
    driver.get(url=url)
    while not next_page:

        time.sleep(3)
        # Находим все элементы, содержащие результаты поиска
        items = driver.find_elements(By.CLASS_NAME, 'SearchResult__searchResultItem--ktZn0')
        for item in items:
            img = 'No found'
            try:
                # Пытаемся найти изображение внутри элемента
                img = item.find_element(By.CLASS_NAME, 'ThingCardBody__cardBodyWrapper--BLLzJ').find_element(By.TAG_NAME, 'img').get_attribute('src')
            except:
                pass

            # Получаем ссылку на элемент, его название и обратную связь
            link = item.find_element(By.CLASS_NAME, 'ThingCardBody__cardBodyWrapper--BLLzJ').get_attribute('href')
            title = item.find_element(By.CLASS_NAME, 'ThingCardHeader__cardNameWrapper--VgmUP').text
            feedback = item.find_element(By.CLASS_NAME, 'CardActionItem__itemContainer--Jjw5X').find_element(By.CLASS_NAME, 'CardActionItem__text--Regp7').text
            print(title, feedback)
            print(img)
            print(link)

            # Записываем данные в JSON-файл
            write_json({
                "title": title,
                "img": img,
                "link": link
            })
        try:
            # Пытаемся перейти на следующую страницу результатов
            driver.find_element(By.CLASS_NAME, 'Pagination__right--fIUIM').click()
            time.sleep(4)
        except Exception as e:
            print(e, 'Error hear')
            next_page = True

except Exception as ex:
    print(ex)
finally:
    # Важно закрыть процесс веб-драйвера после завершения
    driver.close()
    driver.quit()