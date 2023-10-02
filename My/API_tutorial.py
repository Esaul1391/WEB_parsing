# Импортируем необходимые библиотеки
from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
import json


# Функция для захвата URL-адресов
def show_requests_urls(driver, target_url):
    # Открываем указанный URL в веб-драйвере
    driver.get(target_url)
    urls = []
    # Проходим по всем запросам, сделанным во время загрузки страницы
    for request in driver.requests:
        # Добавляем URL в список
        urls.append({"url": request.url})
    return urls


# Функция для захвата ответов на запросы
def show_response(driver, target_url):
    # Открываем указанный URL в веб-драйвере
    driver.get(target_url)
    resps = []
    # Проходим по всем запросам, сделанным во время загрузки страницы
    for request in driver.requests:
        try:
            # Декодируем ответ и парсим его как JSON
            data = decodesw(
                request.response.body,
                request.response.headers.get("Content-Encoding", "identity")
            )
            resp = json.loads(data.decode('utf-8'))
            # Добавляем ответ в список
            resps.append(resp)
        except:
            pass  # Если не удается декодировать или распарсить ответ, игнорируем его
    return resps


# Основная функция
def main():
    # Устанавливаем ключевые слова для поиска в URL
    keywords = ["api", "v1"]

    # Инициализируем веб-драйвер для Chrome с определенными опциями SeleniumWire
    driver = webdriver.Chrome(seleniumwire_options={"disable_encoding": True})

    # Указываем URL, с которым будем работать
    target_url = "https://www.adidas.co.uk/terrex"

    # Захватываем URL-адреса с использованием ключевых слов
    urls = show_requests_urls(driver, target_url)

    # Захватываем ответы на запросы с декодированием и парсингом JSON
    resps = show_response(driver, target_url)

    # Выводим совпадающие URL-адреса
    for url in urls:
        for kw in keywords:
            if kw in url["url"]:
                print(url)

    # Сохраняем ответы в JSON-файл
    with open('data.json', 'w') as f:
        json.dump(resps, f)

    # Закрываем веб-драйвер
    driver.close()


# Проверяем, выполняется ли скрипт напрямую
if __name__ == '__main__':
    main()