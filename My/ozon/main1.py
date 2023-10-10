import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import time
import random
import csv

min_delay = 1
max_delay = 5


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
    link_list = []
    try:
        i = 0
        while True:
            names = driver.find_elements(By.CSS_SELECTOR, "a.tile-hover-target")
            for name in names:
                link = name.get_attribute('href')
                link_list.append(link)
            time.sleep(random.uniform(min_delay, max_delay))
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, 'div.pe5.a2427-a a.a2427-a4')
                scroll_to_element(driver, next_page)
                next_page.click()
                time.sleep(random.uniform(min_delay, max_delay))
            except NoSuchElementException:
                break
            i += 1
        return link_list
    except (TimeoutException, NoSuchElementException) as ex:
        print(f"Произошло исключение: {ex}")
    finally:
        driver.close()
        driver.quit()


def write_to_csv(data, csv_file):
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['org', 'title', 'id', 'link_store', 'name'])  # Записываем заголовки
    for item in data:
        csv_writer.writerow(item)


def parse_list(link_list, driver, csv_writer):
    for link in link_list:
        try:
            driver.get(link)
            time.sleep(random.uniform(min_delay, max_delay))
            button = driver.find_element(By.CSS_SELECTOR, '[class="d4145-a n7j j3p"]')
            button.click()
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            org = soup.find('p', class_='pj3').text.split(' ')[0]
            if org == 'Самозанятый':
                title = soup.find('h1', class_='kz5').text
                link_store = soup.find_all('a', class_='p2j')[-1]['href']
                name = soup.find_all('a', class_='p2j')[-1].text
                id = soup.find('span', attrs={'data-widget': 'webDetailSKU'}).text.split(' ')[-1]
                print(org, title, id, link_store, name)
                # Записываем данные в CSV на каждом проходе цикла
                csv_writer.writerow([org, title, id, link_store, name])
                time.sleep(random.uniform(min_delay, max_delay))
            driver.back()
        except:
            print('Не нашел')

def main():
    url = 'https://www.ozon.ru/search/?text=воздуховол+для+асика&from_global=true'
    open_page = get_url(url)

    # Открываем CSV-файл для записи
    with open('output.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['org', 'title', 'id', 'link_store', 'name'])  # Записываем заголовки

        parse_list(parse_page(open_page), open_page, csv_writer)

if __name__ == "__main__":
    main()