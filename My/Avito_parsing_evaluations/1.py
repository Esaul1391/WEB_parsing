from collections import defaultdict
from selenium import webdriver
from selenium_stealth import stealth
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
max_delay = 6  # Максимальное время задержки в секундах


def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()


def save_to_csv(data):
    file_exists = os.path.isfile('3d.csv')

    # Открываем CSV файл для записи (если он не существует, он будет создан)
    with open('3d.csv', mode='a', newline='', encoding='utf-8') as file:
        # Создаем объект writer для записи данных в файл
        writer = csv.writer(file)

        if not file_exists:
            # Записываем заголовки только если файл не существует
            writer.writerow(['Name', 'ID', 'Data_time', 'View', 'Имя магазина', 'reiting'])

        # Записываем данные в файл
        for item in data:
            writer.writerow(item)

def get_url():
    useragent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument(f"user-agent={useragent.random}")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    # driver.get(url)

    return driver




def parser_evaluation(driver, url):
    rating_list = []
    rating_dikt = defaultdict(int)
    driver.get(url)
    time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
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
        for element in desktop_elements:
            rating_dikt[element.text]+=1
    print(sorted(rating_dikt.items(),key=lambda item: item[1], reverse=True))
    element_counts = Counter(rating_list)

    # Находим три самых повторяющихся элемента
    top_elements = element_counts.most_common(3)
    print(top_elements)
    return top_elements
    # while True:
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
    #     rating_list = []
    #     more_reviews_button = driver.find_element(By.CSS_SELECTOR, '[data-marker="rating-list/moreReviewsButton"]')
    #
    #     scroll_to_element(driver, more_reviews_button)
    #     more_reviews_button.click()
    #     time.sleep(random.uniform(min_delay, max_delay))


def main():
    url = 'https://www.avito.ru/user/af09798cca3c2477ec9881cda9d3699b/profile?id=2844385983&src=item&page_from=from_item_card_button&iid=2844385983#open-reviews-list'
    open_page = get_url()
    parser_evaluation(open_page, url)



if __name__ == "__main__":
    main()
