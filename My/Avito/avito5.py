import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import csv
from collections import Counter
import os

# Устанавливаем случайное время ожидания между запросами
min_delay = 1  # Минимальное время задержки в секундах
max_delay = 7  # Максимальное время задержки в секундах


def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()


def save_to_csv(data):
    file_exists = os.path.isfile('data.csv')

    # Открываем CSV файл для записи (если он не существует, он будет создан)
    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
        # Создаем объект writer для записи данных в файл
        writer = csv.writer(file)

        if not file_exists:
            # Записываем заголовки только если файл не существует
            writer.writerow(['Name', 'ID', 'Data_time', 'View', 'Имя магазина', 'reiting'])

        # Записываем данные в файл
        for item in data:
            writer.writerow(item)

def get_url(url):
    useragent = UserAgent()

    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--headless')
    driver = uc.Chrome(version_main=117, options=options)
    driver.get(url)

    return driver


def parse_page(driver):

    try:
        pagination = int(driver.find_elements(By.CLASS_NAME, 'styles-module-text-InivV')[-1].text)

        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
        print(pagination)

        for item in range(1, pagination):
            print('*' * 10, f"page {item} from pages {pagination}")
            url = f"https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p={item}&q=3d+печать"
            driver.get(url)

            # прохожусь по объявлениям
            try:
                names = driver.find_elements(By.XPATH, "//h3[@itemprop='name']")
                for name in names:  # Изменено на обработку только первой записи
                    data_save = []
                    time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
                    name.click()
                    time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
                    driver.switch_to.window(driver.window_handles[1])

                    # Поиск нужных данных
                    name_ad = driver.find_element(By.CSS_SELECTOR, '[data-marker="item-view/title-info"]').text
                    print(name_ad)
                    id = driver.find_element(By.CSS_SELECTOR, '[data-marker="item-view/item-id"]').text
                    print(id)
                    data_item = driver.find_element(By.CSS_SELECTOR, '[data-marker="item-view/item-date"]').text
                    print(data_item)
                    view = driver.find_element(By.CSS_SELECTOR, '[data-marker="item-view/total-views"]').text
                    print(view)

                    # Обработка информации о продавце
                    top_rating = process_seller(driver)

                    # Запись в csv

                    data_save.append([name_ad, id, data_item, view, top_rating])
                    time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
                    if top_rating != "Не кликается":
                        save_to_csv(data_save)
            except Exception as ex:
                print("Ошибка при проходе по страницам")
                print(ex)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def process_seller(driver):
    try:
        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
        driver.find_element(By.CSS_SELECTOR, '[data-marker="seller-link/link"]').click()
        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка

        rating = driver.find_element(By.CSS_SELECTOR, '[data-marker="profile/summary"]').text
        print(rating)
        driver.find_element(By.CSS_SELECTOR, '[data-marker="profile/summary"]').click()
        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
        rating_list = []
        # Скролл к кнопке "Показать еще отзывы"
        while True:
            try:
                # Скролл к кнопке "Показать еще отзывы" и кликнуть на нее
                more_reviews_button = driver.find_element(By.CSS_SELECTOR, '[data-marker="rating-list/moreReviewsButton"]')

                scroll_to_element(driver, more_reviews_button)
                more_reviews_button.click()
                time.sleep(random.uniform(min_delay, max_delay))
            except Exception as e:
                break  # Выход из цикла при отсутствии кнопки "Показать еще отзывы"
                # Поиск элементов с классом "desktop-35wlrd"
            desktop_elements = driver.find_elements(By.CLASS_NAME, 'desktop-35wlrd')

            # Преобразуем элементы в их текстовое представление перед подсчетом
            element_texts = [rating_list.append(element.text) for element in desktop_elements]
        element_counts = Counter(rating_list)

        # Находим три самых повторяющихся элемента
        top_elements = element_counts.most_common(3)
        print(top_elements)
        return top_elements
    except:
        print("Нет оценок")
        return "Не кликается"

def main():
    url = 'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать'
    open_page = get_url(url)
    parse_page(open_page)


if __name__ == "__main__":
    main()
