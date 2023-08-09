import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


with webdriver.Chrome() as browser:
    try:
        browser.maximize_window()
        browser.get('https://vk.com')
        time.sleep(5)

        email_input = browser.find_element(By.ID, 'index_email')
        email_input.clear()
        email_input.send_keys('+79879878987')
        email_input.send_keys(Keys.ENTER)
        time.sleep(6)
        browser.execute_script('window.scrollBy(0,document.body.scrolHeight)')
    except Exception as ex:
        print(ex)
