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



                    #method 2
