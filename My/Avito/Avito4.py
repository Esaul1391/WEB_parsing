import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import random
import time

# Устанавливаем случайное время ожидания между запросами
min_delay = 1  # Минимальное время задержки в секундах
max_delay = 3  # Максимальное время задержки в секундах


def get_url(url):
    useragent = UserAgent()

    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(options=options)
    driver.get(url)

    return driver


def parse_page(driver):
    try:
        while True:
            names = driver.find_elements(By.XPATH, "//h3[@itemprop='name']")
            for name in names[:1]:  # Изменено на обработку только первой записи
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

                #
                try:
                    time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
                    driver.find_element(By.CSS_SELECTOR, '[data-marker="rating-caption/rating"]').click()
                except:
                    print("Нет оценок")



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


def main():
    url = 'https://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать'
    open_page = get_url(url)
    parse_page(open_page)


if __name__ == "__main__":
    main()