# from selenium import webdriver
#
# url = 'https://stepik.org/a/104774'
# browser = webdriver.Chrome()
# browser.get(url)


# import time
# from selenium import webdriver
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(50)


#           launching the browser in hidden mode
# .add_argument()
# --headless

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))
#
# Преимущества запуска браузера в фоновом режиме.
#
# Отсутствует отрисовка содержимого, тем самым потребляется меньше ресурсов.
# Работает быстрее, т.к. не нужно ничего отрисовывать) Использование --headless может
# значительно ускорить работу парсера на относительно слабых машинах.
# Не занимает место на экране, и не мешает вашей работе во время выполнения скрипта.


# Если вам потребуется запустить браузер с расширениями  и в режиме
# --headless, то необходимо прописать options.add_argument("--headless=chrome")

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')
#
#
# options_chrome.add_argument('--headless=chrome')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(5)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))


#           Перенос профиля с основного браузера Chrome в браузер под управлением Selenium
#           transferring a profile from one chrome browser to a browser selenium

# import time
# from selenium import webdriver
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(10)


