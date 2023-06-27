
#           task1

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')


    for i in range(500):
        browser.refresh()
        g = browser.find_element(By.ID, 'result')
        print(g.text)

    # res = sum([int(i.text) for i in g])
    # i = browser.find_element(By.ID, "input_result").send_keys(res)
    # cl = browser.find_element(By.CLASS_NAME, 'btn')
    # cl.click()
    # time.sleep(8)