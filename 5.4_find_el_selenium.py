#       Локаторы

# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR –поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – Поиск ссылки по частичному совпадению текста.


# Два универсальный метода find_element() and find_elements() возвращают один элемент или список элементов
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button").click()
#
# time.sleep(10)

#       Автоматическое закрытие браузера

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button")
# time.sleep(2)
# button.click()
# time.sleep(2)
# browser.quit() # Автоматически закроет браузер


# Автматическое закрытие при совершение ошибки
#
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = browser.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)
# finally:
#     browser.quit()

# Метод чтобы ни очем не думать

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = browser.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)

# browser.close() - Закрывает текущее окно браузера, если во время работы вы
# открыли новое окно\вкладку
#
# browser.quit() - Закрывает все окна, вкладки, процессы вебдрайвера, которые
# были запущены во время сессии.


#   link = browser.find_element(By.CSS_SELECTOR, 'p:nth-child(2)')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'http://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     link = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#     print([i.text for i in link])


#          task4

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/1/1.html')
#     input_form = browser.find_elements(By.CLASS_NAME, 'form')
#     for i in input_form:
#         i.send_keys('Text')
#     time.sleep(5)

    #  Можно использовать библиотеку Faker


#           task5


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/2/2.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     link = browser.find_element(By.LINK_TEXT, "16243162441624")
# with webdriver.Chrome() as browser:
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, "16243162441624")
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    button = browser.find_element(By.LINK_TEXT, "16243162441624").click()
    time.sleep(10)

