
#           CSV

# CSV (Comma Separated Values) - «значения, разделенные запятыми». Это один из самых
# простых способов хранения информации в виде обычного текста. Данные представлены в
# табличной форме, где каждая строка является строкой записи таблицы.


# import csv
#
# lst = ['one', 'two', 'three']
#
# with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(lst)


#           часть 2

# import csv
# import requests
# from bs4 import BeautifulSoup
#
# # 1 ------------------------------------------------------
# # В первом блоке мы создали файл res.csv и определили в нем первые 12 ячеек для заголовков
#
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file: # если флаг 'w' то запишится заново
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Артикул', 'Бренд', 'Модель',
#         'Тип', 'Игровая', 'Размер', 'Подсветка', 'Разрешение',
#         'Сайт производителя', 'В наличии', 'Цена'])
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# # Стандартный запрос к сайту
#
# url = 'http://parsinger.ru/html/mouse/3/3_11.html'
#
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# #   сохраняем заначение в переменные
# name = soup.find('p', id='p_header').text
# article = soup.find('p', class_='article').text.split(': ')[1]
# brand = soup.find('li', id='brand').text.split(': ')[1]
# model = soup.find('li', id='model').text.split(': ')[1]
# type = soup.find('li', id='type').text.split(': ')[1]
# purpose = soup.find('li', id='purpose').text.split(': ')[1]
# light = soup.find('li', id='light').text.split(': ')[1]
# size = soup.find('li', id='size').text.split(': ')[1]
# dpi = soup.find('li', id='dpi').text.split(': ')[1]
# site = soup.find('li', id='site').text.split(': ')[1]
# in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
# price = soup.find('span', id='price').text.split(' ')[0]
# # 3 ------------------------------------------------------
#
# # 4 ------------------------------------------------------
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file: # 'a' - 'append'
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         name, article, brand, model,
#         type, purpose, light, size, dpi,
#         site, in_stock, price])
# # 4 ------------------------------------------------------

#           part 3

import csv
import requests
from bs4 import BeautifulSoup

# 1 ------------------------------------------------------
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
url = 'http://parsinger.ru/html/index3_page_2.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
price = [x.text for x in soup.find_all('p', class_='price')]
# 3 ------------------------------------------------------

# 4------------------------------------------------------

for item, price, descr in zip(name, price, description):
    flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]

    file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(flatten)
file.close()
print('Файл res.csv создан')