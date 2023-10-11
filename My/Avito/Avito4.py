import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from collections import Counter

# Устанавливаем случайное время ожидания между запросами
min_delay = 1  # Минимальное время задержки в секундах
max_delay = 3  # Максимальное время задержки в секундах


def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()


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
        while True:
            names = driver.find_elements(By.XPATH, "//h3[@itemprop='name']")
            for name in names:  # Изменено на обработку только первой записи
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
                process_seller(driver)
                time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка

            try:
                # Используем CSS селектор для кнопки "Следующая страница"
                driver.find_element(By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]').click()
                time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
            except Exception as e:
                print(e)
                break  # Выход из цикла при отсутствии кнопки "Следующая страница"
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
                more_reviews_button = driver.find_element(By.CSS_SELECTOR,
                                                          '[data-marker="rating-list/moreReviewsButton"]')
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

    except:
        print("Нет оценок")


def main():
    url = 'https://www.avito.ru/moskva?q=пылеотвод'
    open_page = get_url(url)
    parse_page(open_page)


if __name__ == "__main__":
    main()
