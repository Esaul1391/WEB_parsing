#
# #           task1
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/1/index.html')
#
#
#     for i in range(500):
#         browser.refresh()
#         g = browser.find_element(By.ID, 'result')
#         print(g.text)
# import time
# res = sum([int(i.text) for i in g])
# i = browser.find_element(By.ID, "input_result").send_keys(res)
# cl = browser.find_element(By.CLASS_NAME, 'btn')
# cl.click()
# time.sleep(8)


#           cookie
# get all cookie from page

from pprint import pprint
from selenium import webdriver

# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies() # all cookie
#     pprint(cookies)


#           .get_cookie(name_cookie)
# cookie and meaning

#
# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     for cookie in cookies:
#         print(cookie['name']) # или cookie['value'] чтобы получить их значение


# 'expiry': 1722507931, Время истечения срока жизни cookie


# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     for cookie in cookies:
#         print(cookie['expiry'])
#     time.sleep(10)


#           task2


# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/3/index.html')
#     cookies = webdriver.get_cookies()
#     total = 0
#     for cookie in cookies:
#         total += int(cookie['value'])
#
# print(total)


#           task3

# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/3/index.html')
#     cookies = webdriver.get_cookies()
#     total = 0
#     for cookie in cookies:
#         if int(cookie['name'].split('_')[-1])%2 == 0:
#            total += int(cookie['value'])
#
# print(total)


#           task4

# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     for i in range(1,43):
#         webdriver.get(f'https://parsinger.ru/methods/5/{i}.html')
#         cookies = webdriver.get_cookies()
#
#         cookie_list = []
#         for cookie in cookies:
#             cookie_list.append(cookie['expiry'])
#     print(max(cookie_list))
#     for i in range(1,43):
#         webdriver.get(f'https://parsinger.ru/methods/5/{i}.html')
#         cookies = webdriver.get_cookies()
#         if cookie['expiry'] == max(cookie_list):
#             print(cookie['expiry'])


