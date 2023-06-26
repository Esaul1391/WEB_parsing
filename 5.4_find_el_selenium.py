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

#           task6

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     button = browser.find_elements(By.TAG_NAME, "p")
#     time.sleep(2)
#     print(sum([int(i.text) for i in button]))

#           task7

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     button = browser.find_elements(By.CLASS_NAME, "text")
#     #links = browser.find_elements(By.CSS_SELECTOR, '.text p:nth-child(2)')
#     time.sleep(2)
#     print(sum([int(i.text.split('\n')[1]) for i in button]))



#           task7

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/4/4.html')
#     button = browser.find_elements(By.CLASS_NAME, "check")
#     #links = browser.find_elements(By.CSS_SELECTOR, '.text p:nth-child(2)')
#     print(len(button))
#     for i in range(len(button)):
#         button[i].click()
#     res = browser.find_element(By.CLASS_NAME, "btn").click()
#     res1 = browser.find_element(By.ID, "result")
#     time.sleep(20)
#     print(res1.text)


#           task8

# Когда вам необходимо получить значение атрибута. Вы можете использовать метод
# .get_attribute('attribute'), Где attribute - это имя требуемого вам атрибута.
#
# Если необходимо получить значение value="" мы напишем следующий код.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/5/5.html')
#     checkbox = browser.find_elements(By.CLASS_NAME, 'check')
#     for item in checkbox:
#         print(item.get_attribute('value'))



from selenium import webdriver
from selenium.webdriver.common.by import By
numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5/5.html')
    checkbox = browser.find_elements(By.CLASS_NAME, 'check')
    for i in range(len(checkbox)):
        if int(checkbox[i].get_attribute('value')) in numbers:
            #print(checkbox[i])
            checkbox[i].click()
    res = browser.find_element(By.CLASS_NAME, "btn").click()
    res1 = browser.find_element(By.ID, "result")
    time.sleep(20)
    print(res1.text)