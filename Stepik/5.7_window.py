# Основные функции применяемые к модальным окнам.
#
# .switch_to - переключает фокус на модальное окно;
#
# .accept() - нажимает на кнопку "OK" в модальном окне;
#
# .dismiss() - нажимает на кнопку "Отмена" в модальном окне;
#
# .send_keys() - отправляет текст в текстовое поле в модальном окне;
#
# .text - возвращает title модального окна.

# Переключение на все виды модальных окон выполняется
# командой browser.switch_to.alert
#
# Alert - выводит пользователю сообщение, содержит кнопку "ОК"
#
# Prompt - запрашивает у пользователя ввод каких-либо текстовых
# данных, содержит кнопки "ОК" и "Отмена";
#
# Confirm - выводит окно с вопросом, содержит кнопки "ОК" и "Отмена".



# Модальное окно Alert
# Код ниже, выполнит клик на кнопку с id="alert", вызвав тем самым модальное окно alert,
# переключит на него свой фокус функцией browser.switch_to.alert и в принте распечатает
# содержимое title этого окна.

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'alert').click()
#     time.sleep(1)
#     alert = browser.switch_to.alert # Если вы планируете что-то делать с этим событием
#                                     # , можно добавить его в переменную
#     print(alert.text)
#     time.sleep(1)
#     alert.accept()



#               Модальное окно Prompt
# В модальное окно prompt мы можем отправлять текст при помощи функции .send_keys("")

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'prompt').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert    #переключает внимание на окно
#     prompt.send_keys('Введёный текст')  #   Вводит текст в текстовое поле
#     prompt.accept()     #   нажимает на кнопку принять
#     time.sleep(.5)
#     print(browser.find_element(By.ID, 'result').text)



#           Модальное окно Confirm
#   Модальное окно confirm имеет всего 2 кнопки, "Ok" и "Отмена", взаимодействовать
#   с которыми мы можем функциями .accept()  и .dismiss().

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'confirm').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert
#     prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
#     time.sleep(.5)
#Код выше, нажимает на кнопку Confirm и в появившемся окне нажимает на кнопку "Ok"


#           task1

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/blank/modal/2/index.html')
#     sp = browser.find_elements(By.TAG_NAME, 'input')
#     print(len(sp))
#     for i in range(len(sp)):
#         sp[i].click()
#         ac = browser.switch_to.alert
#         ac.accept()
#         # time.sleep(3)
#         cod = browser.find_element(By.ID, 'result').text
#         print(cod)



#           task2

import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/blank/modal/3/index.html')
#     sp = browser.find_elements(By.CLASS_NAME, 'buttons')
#     #print(len(sp))
#     for i in range(len(sp)):
#         sp[i].click()
#         ac = browser.switch_to.alert
#         rr = int(ac.text)
#         #print(rr)
#         ac.accept()
#         window = browser.find_element(By.ID, 'input')
#         window.send_keys(rr)
#         check_1 = browser.find_element(By.ID, 'check')
#         check_1.click()
#         res = browser.find_element(By.ID, 'result').text
#         if res != 'Неверный пин-код':
#             print(res)



#           task3


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/4/index.html')
    sp = browser.find_elements(By.CLASS_NAME, 'pin')
    #print(len(sp))
    check = browser.find_element(By.ID, 'check')
    for i in range(len(sp)):
        tx = sp[i].text
        print(tx)
        check.click()
        prompt = browser.switch_to.alert
        prompt.send_keys(tx)
        time.sleep(0.1)
        prompt.accept()
        time.sleep(0.1)

        res = browser.find_element(By.ID, 'result').text
        if res != 'Неверный пин-код':
            print(res)



# from selenium import webdriver
#
# url = 'https://stepik.org/a/104774'
# browser = webdriver.Chrome()
# browser.get(url)
