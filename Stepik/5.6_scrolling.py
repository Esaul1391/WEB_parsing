                    #method 1 execute_script()

# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     for i in range(10):
#         browser.execute_script("window.scrollBy(0,5000)")
#         time.sleep(2)

#calculate the height of the visible part of the site
#вычислить высоту видимой части сайта
# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script("return document.body.scrollHeight")
#     time.sleep(2)
#     print(height)

# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script("return window.innerHeight") # get height
#     print(height)
#     width = browser.execute_script("return window.innerWidth")  # get width
#     print(width)

# scroll to the last pixel
# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # last pixel
#     time.sleep(2)

# При написании парсеров, часто необходимо сперва совершить необходимое количество
# скроллинга, чтобы загрузилась вся необходимая вам информация. После того как вся
# нужная инфа появилась на странице, мы собираем всё при помощи .find_elements(),
# но об этом мы будем говорить далее.


# .execute_script()
# Синтаксис webdriver.execute_script(script, *args).
#
# В .execute_script() можно использовать следующие полезные параметры.
#
# Посмотреть все события можно тут и тут, ниже приведены те, которые
#                     чаще всего используются при написании парсеров.
#
# .execute_script("return arguments[0].scrollIntoView(true);", element) -
#                     прокручивает родительский контейнер элемента таким образом, чтобы element, для которого вызывается scrollIntoView , был виден пользователю ;
# .execute_script("window.open('http://parsinger.ru', 'tab2');") - создаст н
#                     овую вкладку с именем "tab2";
#
# .execute_script("return document.body.scrollHeight") - вернет значение высоты
#                     элемента<body>;
#
# .execute_script("return window.innerHeight") - вернет значение высоты окна браузера;
#
# .execute_script("return window.innerWidth") - вернет значение ширину окна браузера;
#
# .execute_script("window.scrollBy(X, Y)") - прокручивает документ на заданное число
#                     пикселей;
#
# X - смещение в пикселях по горизонтали;
# Y - смещение в пикселях по вертикали.
# .execute_script("alert('Ура Selenium')") - вызывает модальное окно Alert;
#
# .execute_script("return document.title;") - вернет title открытого документа;
#
# .execute_script("return document.documentURI;") - возвращает URL документа;
#
# .execute_script("return document.readyState;") - возвращает состояние загрузки
#                     страницы, вернет complete если страница загрузилась;
#
# .execute_script("return document.anchors;") - возвращает список всех якорей;
#
# [x.tag_name for x in browser.execute_script("return document.anchors;")] - такой код
#                     даст возможность получить список всех тегов c якорями.
#                     Очень полезная инструкция, используется, если при скроллинге
#                     мы не можем найти элемент, за который можно "зацепится" ;
# .execute_script("return document.cookie;")  - возвращает список файлов cookie,
#                     разделенных точкой с запятой;
#
# .execute_script("return document.domain;") - возвращает домен текущего документа;
#
# .execute_script("return document.forms;") - вернет список форм;
#
# window.scrollTo(x-coord, y-coord) - прокрутка документа до указанных координат;
#
# x-coord пиксель по горизонтальной оси документа, будет отображен вверху слева;
# y-coord пиксель по вертикальной оси документа, будет отображен вверху слева.
# .execute_script("return document.getElementsByClassName('container');")  -
#                     возвращает список всех элементов с заданным классом
#                     class="container";
#
# .execute_script("return document.getElementsByTagName('container');") - возвращает
#                     список всех элементов с заданным именем name="container".


#           task2

import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/scroll/4/index.html')
#     button = browser.find_elements(By.CLASS_NAME, "btn")
#     res = []
#     for bt in range(len(button)):
#         browser.execute_script("return arguments[0].scrollIntoView(true);", button[bt])
#         button[bt].click()
#         res1 = browser.find_element(By.ID, "result").text
#         res.append(int(res1))
# print(sum(res))
    #links = browser.find_elements(By.CSS_SELECTOR, '.text p:nth-child(2)')
    # print(len(button))
    # for i in range(len(button)):
    #     button[i].click()
    # res = browser.find_element(By.CLASS_NAME, "btn").click()
    # res1 = browser.find_element(By.ID, "result")
    # time.sleep(20)
    # print(res1.text)

                    #method 2
#           use class Key

# from selenium.webdriver import Keys
#
# или
#
# from selenium.webdriver.common.keys import Keys



# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     tag_p = browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
#     time.sleep(10)
# На открывшемся сайте получим первый выделенный элемент <input>



# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     tags_input = browser.find_elements(By.TAG_NAME, 'input')
#
#     for input in tags_input:
#         input.send_keys(Keys.DOWN)
#         time.sleep(1)


# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#
#     list_input = []
#     while True:
#         input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
#         for tag_input in input_tags:
#             if tag_input not in list_input:
#                 tag_input.send_keys(Keys.DOWN)
#                 tag_input.click()
#                 time.sleep(1)
#                 list_input.append(tag_input)



#           methods 3
#           ActionChains()
#from selenium.webdriver.common.action_chains import ActionChains

# ActionChains(webdriver) - принимает единственный объект, объект webdriver'a.
#
# .perform() - выполняет запуск цепочки действий, написание этого метода в конце
# каждой цепочки , просто необходимо для его запуска

# menu = driver.find_element(By.CSS_SELECTOR, ".nav")
# hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
#
# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     target = browser.find_element(By.ID, 'like')
#     actions = ActionChains(browser).move_to_element(target).click().perform()


import time
from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     target = browser.find_element(By.ID, 'like')
#     actions = ActionChains(browser)
#     "тут может находиться любой код, от time.sleep() до перехода в новую вкладку и т.д"
#     actions.move_to_element(target)
#     "тут может находиться любой код, от time.sleep() до перехода в новую вкладку и т.д"
#     actions.click()
#     "тут может находиться любой код, от time.sleep() до перехода в новую вкладку и т.д"
#     actions.perform()



#           method4
#           scroll_by_amount()

#scroll_by_amount(delta_x, delta_y) -
# - delta_x: расстояние по оси X для прокрутки с помощью колеса.
#                     Отрицательное значение прокручивается влево.
# - delta_y: расстояние по оси Y для прокрутки с помощью колеса.
#                     Отрицательное значение прокручивается вверх.



# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
#     while True:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
#     for x in range(10):
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()




#               Task4

#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/scroll/training_task_3/')
#     actions = ActionChains(browser)
#     klick = browser.find_elements(By.CLASS_NAME, 'checkbox_class')
#     print(klick)
#     total = 0
#     for k in range(len(klick)):
#         actions.scroll_to_element(klick[k]) # important the method
#         klick[k].click()
#         time.sleep(1)
#         el = browser.find_element(By.ID, f'result{k+1}').text
#         if el != '':
#             total += int(el)
#
#     print(total)



#               Task 4

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/scroll/3/')
#     actions = ActionChains(browser)
#     klick = browser.find_elements(By.CLASS_NAME, 'checkbox_class')
#     print(len(klick))
#     total = 0
#     for k in range(len(klick)):
#         actions.scroll_to_element(klick[k]) # important the method
#         klick[k].click()
#
#
#         el = browser.find_element(By.ID, f'result{k+1}').text
#         if el != '':
#             total += int(el)
#             print(el)
#     time.sleep(20)
#     print(total)




#               Task5
#
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    actions = ActionChains(browser)
    k = browser.find_elements(By.TAG_NAME, 'input')

    print([i.text for i in k])


#.move_to_element(to_element)


