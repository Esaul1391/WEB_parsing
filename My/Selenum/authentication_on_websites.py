from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from fake_useragent import UserAgent



useragent = UserAgent()
                                #   options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

url = "https://vk.com/"
driver = webdriver.Chrome(options=options)     #   write path connect webdriver

                                #   general block
try:
    driver.get(url=url)
    time.sleep(3)

    email_input = driver.find_element(By.CLASS_NAME, 'VkIdForm__input')     #   ищу по имени класса, не забываю установить расширение
    email_input.clear()     #   очищаю поле ввода
    email_input.send_keys('88002001010')        #   Передаю информацию в поле ввода
    time.sleep(3)
    email_input.send_keys(Keys.ENTER)   #   нажимаю клавишу, не забываю про установку расширения
    # button = driver.find_element(By.CLASS_NAME, 'FlatButton__in')     #
    # button.click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:                        # important close proces
    driver.close()
    driver.quit()