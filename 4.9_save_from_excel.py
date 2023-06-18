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

# import csv
# import requests
# from bs4 import BeautifulSoup
#
# # 1 ------------------------------------------------------
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# url = 'http://parsinger.ru/html/index3_page_2.html'
#
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
# price = [x.text for x in soup.find_all('p', class_='price')]
# # 3 ------------------------------------------------------
#
# # 4------------------------------------------------------
#
# for item, price, descr in zip(name, price, description):
#     flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
#
#     file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(flatten)
# file.close()
# print('Файл res.csv создан')


#           task 4

# import csv
# import requests
# from bs4 import BeautifulSoup
#
# # 1 ------------------------------------------------------
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
#
# name = []
# description = []
# price = []
#
# for i in range(1, 4):
#     url = f"https://parsinger.ru/html/index4_page_{i}.html"
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     # name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#     for x in soup.find_all('a', class_='name_item'):
#         name.append(x.text.strip())
#     # description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#     for x in soup.find_all('div', class_='description'):
#         description.append(x.text.split('\n'))
#     # price = [x.text for x in soup.find_all('p', class_='price')]
#     for x in soup.find_all('p', class_='price'):
#         price.append(x.text)
#
# for item, price, descr in zip(name, price, description):
#     flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
#
#     file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(flatten)
# file.close()
# print('Файл res.csv создан')

#               task 5

# import csv
# import requests
# from bs4 import BeautifulSoup
#
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
#
# name = []
# description = []
# price = []
#
# for i in range(1, 6):
#     url = f"https://parsinger.ru/html/index{i}_page_1.html"
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     url_chunks = [tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a')]
#
#     print(url_chunks)
#     # find articles of products on pages of website
#
#     for c in url_chunks:
#         url = f'https://parsinger.ru/html/{c}'
#         response = requests.get(url=url)
#         print(url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         link = [tag['href'] for tag in soup.find_all('a', {'class': 'name_item'})]
#         for x in soup.find_all('a', class_='name_item'):
#             name.append(x.text.strip())
#         #description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#         for x in soup.find_all('div', class_='description'):
#             description.append(x.text.split('\n'))
#         # price = [x.text for x in soup.find_all('p', class_='price')]
#         for x in soup.find_all('p', class_='price'):
#             price.append(x.text)
#         # for j in link:
#         #     url = f"https://parsinger.ru/html/{link}"
#         #
#         #     response = requests.get(url=url)
#         #     response.encoding = 'utf-8'
#         #     soup = BeautifulSoup(response.text, 'lxml')
#         # name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#         #     for x in soup.find_all('a', class_='name_item'):
#         #         name.append(x.text.strip())
#         #         print(x.text.strip())
#         #     description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#         #     for x in soup.find_all('div', class_='description'):
#         #         description.append(x.text.split('\n'))
#         # # price = [x.text for x in soup.find_all('p', class_='price')]
#         #     for x in soup.find_all('p', class_='price'):
#         #         price.append(x.text)
# print(name)
# print(price)
# print(description)
# for item, price, descr in zip(name, price, description):
#     flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
#
#     file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(flatten)
# file.close()
# print('Файл res.csv создан')


#           task6

import csv
import requests
from bs4 import BeautifulSoup


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    # writer.writerow([
    #     'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип',
        'Технология экрана', 'Материал корпуса', 'Материал браслета',
        'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
        'Ссылка на карточку с товаром'])

name = []
article = []
brand = []
model = []
type_ = []
scrin_t = []
material_frame = []
material_bracer = []
size = []
site_ = []
availability = []
price = []
old_price = []
url_ = []
for i in range(1, 33):
    url = f'https://parsinger.ru/html/watch/1/1_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name.append(soup.find('p', id='p_header').text.split('\n'))
    article.append(int(''.join(filter(str.isdigit, str(soup.find('p', class_='article').text.split('\n'))))))
    brand.append(soup.find('li', id='brand').text.split(' ')[1])
    model.append(soup.find('li', id='model').text.split(' ')[1])
    type_.append(soup.find('li', id='type').text.split(' ')[1])
    scrin_t.append(soup.find('li', id='display').text.split(' ')[1])
    material_frame.append(soup.find('li', id='material_frame').text.split(' ')[1])
    material_bracer.append(soup.find('li', id='material_bracer').text.split(' ')[1])
    size.append(soup.find('li', id='size').text.split(' ')[1])
    site_.append(soup.find('li', id='site').text.split(' ')[1])
    availability.append(soup.find('span', id='in_stock').text.split(' ')[1])
    price.append(soup.find('span', id='price').text)
    price.append(soup.find('span', id='old_price').text)
    url_.append(url)
    # # price = [x.text for x in soup.find_all('p', class_='price')]
    # for x in soup.find_all('p', class_='price'):
    #     price.append(x.text)
    # for j in link:
    #     url = f"https://parsinger.ru/html/{link}"
    #
    #     response = requests.get(url=url)
    #     response.encoding = 'utf-8'
    #     soup = BeautifulSoup(response.text, 'lxml')
    # name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    #     for x in soup.find_all('a', class_='name_item'):
    #         name.append(x.text.strip())
    #         print(x.text.strip())
    #     description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    #     for x in soup.find_all('div', class_='description'):
    #         description.append(x.text.split('\n'))
    # # price = [x.text for x in soup.find_all('p', class_='price')]
    #     for x in soup.find_all('p', class_='price'):
    #         price.append(x.text)
print(name)
# print(price)

for item, price, url_ in zip(name, price, url_):
    flatten = item, price, url_

    file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(flatten)
file.close()
print('Файл res.csv создан')
