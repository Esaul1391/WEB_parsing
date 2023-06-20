#           part1

# import requests
# from bs4 import BeautifulSoup
# import json
#
# # 1 ------------------------------------------------------
# url = 'http://parsinger.ru/html/mouse/3/3_11.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# result_json = {
#     'name': soup.find('p', id='p_header').text,
#     'price': soup.find('span', id='price').text}
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# # 3 ------------------------------------------------------
#
#
# >>> {
#     "name": "Мышь Logitech G PRO HERO Black USB проводная",
#     "price": "5100 руб"
# }
#
#
# Методы JSON:
# json.dump() - преобразует объекты python (в нашем примере это словарь)
# в соответствующий объект JSON. Метод .dump() первым параметром ожидает
# словарь, который мы будем записывать в файл, а вторым параметром - файл,
# куда мы будем записывать наш словарь.
#
# indent=4 улучшает читаемость файла json, и обозначает отступ в пробелах;
# ensure_ascii=False - если не указать, могут возникнуть проблемы с кодировкой.
# Если установить значение True, то кириллические символы будут отображены в ascii,
# примерно вот так \u041c\u044b\u0448\u044c.
#
# json.dumps() - отличается лишь тем, что кодирует наши данные в Python string
# и служит для преобразования примитивных типов данных. В ваших парсерах вы, скорее
# всего, будете использовать именно первый вариант;
#
# json.load() - метод считывает файл в формате JSON и возвращает объекты Python, про
# метод load() подробнее мы поговорим позже когда, будем считывать json-файлы;
#
# json.loads() - метод считывает строку в формате JSON и возвращает объекты Python.


#           part2

# import requests
# from bs4 import BeautifulSoup
# import json
#
# # 1 ------------------------------------------------------
# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
# price = [x.text for x in soup.find_all('p', class_='price')]
# # 2 ------------------------------------------------------
#
# result_json = []
# # 3 ------------------------------------------------------
# for list_item, price_item, name in zip(description, price, name):
#     result_json.append({
#         'name': name,
#         'brand': [x.split(':')[1] for x in list_item][0],
#         'type': [x.split(':')[1] for x in list_item][1],
#         'connect': [x.split(':')[1] for x in list_item][2],
#         'game': [x.split(':')[1] for x in list_item][3],
#         'price': price_item
#
#         #           рациональный вариант
#         # 'brand': list_item[0].split(': ')[1],
#         # 'type': list_item[1].split(': ')[1],
#         # 'connect': list_item[2].split(': ')[1],
#         # 'game': list_item[3].split(': ')[1],
#     })
#
# #           simple
# for item in soup.find_all('div', class_='item'):
#     name = item.find('a', class_='name_item').text.strip()
#     price = item.find('p', class_='price').text
#     description = [value.text.split(':')[1].strip() for value in item.find_all('li')]
#     dict_ = {
#         'name': name,
#         'brand': description[0],
#         'type': description[1],
#         'connect': description[2],
#         'game': description[3],
#         'price': price
#     }
#     result_json.append(dict_)
# # 3 ------------------------------------------------------
#
# # 4 ------------------------------------------------------
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# # 4 ------------------------------------------------------


# import requests
# from bs4 import BeautifulSoup
# import json
#
# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
#
# name = [x.text.strip()for x in soup.find_all('a', class_='name_item')]
# price = [x.text for x in soup.find_all('p', class_='price')]
# description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
#
# result_json = []
#
# for list_item, price_item, name in zip(description, price, name):
#     result_json.append({
#         'name': name,
#         'brand': list_item[0].split(':')[1].strip(),
#         'type': list_item[1].split(':')[1].strip(),
#         'connect': list_item[2].split(':')[1].strip(),
#         'game': list_item[3].split(':')[1].strip(),
#         'price': price_item
#
#     })
#
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)



#           part3
#extract the attribute value


# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# description = soup.find('ul', id='description').find_all('li')
#
# #for li in description:
# #    print(li['id'])
#
# li_id = [x['id'] for x in description]
# print(li_id)



#           task1

# import requests
# from bs4 import BeautifulSoup
# import json
#
# result_json = []
# for i in range(1, 5):
#     url = f'http://parsinger.ru/html/index3_page_{i}.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#
#
#
#     name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#     description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
#     price = [x.text for x in soup.find_all('p', class_='price')]
#
#
#
#
#     for list_item, price_item, name in zip(description, price, name):
#         result_json.append({
#             'name': name,
#             'brand': [x.split(':')[1] for x in list_item][0],
#             'type': [x.split(':')[1] for x in list_item][1],
#             'connect': [x.split(':')[1] for x in list_item][2],
#             'game': [x.split(':')[1] for x in list_item][3],
#             'price': price_item
#
#         })
#
#
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)



#           task2

# import requests
# from bs4 import BeautifulSoup
# import json
#
# result_json = []
# for j in range(1, 6):
#     for i in range(1, 5):
#         url = f'http://parsinger.ru/html/index{j}_page_{i}.html'
#         response = requests.get(url=url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#
#
#
#         name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#         description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
#         price = [x.text for x in soup.find_all('p', class_='price')]
#
#
#
#
#         for list_item, price_item, name in zip(description, price, name):
#             result_json.append({
#                 'name': name,
#                 'brand': [x.split(':')[1] for x in list_item][0],
#                 'type': [x.split(':')[1] for x in list_item][1],
#                 'connect': [x.split(':')[1] for x in list_item][2],
#                 'game': [x.split(':')[1] for x in list_item][3],
#                 'price': price_item
#
#             })
#
#
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)


#           task3

import requests
from bs4 import BeautifulSoup
import json

# 1 ------------------------------------------------------
url = 'https://parsinger.ru/html/mouse/3/3_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
categories = 'maus'
name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
description = [x.text.strip().split('\n') for x in soup.find_all('ul', id='description')]
count = [x.text for x in soup.find_all('span', id='in_stock')]
price = [x.text for x in soup.find_all('span', id='price')]
old_price = [x.text for x in soup.find_all('span', id='old_price')]
link = url
# 2 ------------------------------------------------------

result_json = []
# 3 ------------------------------------------------------
for list_item, count, price, old_price, name, link in zip(description, count, price, old_price, name, url):
    result_json.append({
        'categories': 'mouse',
        'name': name,
        'description' : {'brand': [x.split(':')[1] for x in list_item][0],
                         'model': [x.split(':')[1] for x in list_item][1],
                         'type': [x.split(':')[1] for x in list_item][2],
                         'purpose': [x.split(':')[1] for x in list_item][3],
                         'light': [x.split(':')[1] for x in list_item][4],
                         'size': [x.split(':')[1] for x in list_item][5],
                         'dpi': [x.split(':')[1] for x in list_item][6],
                         'site': [x.split(':')[1] for x in list_item][7]
                                  },
        'count': count,
        'price': price,
        'old_price' : old_price,
        'link' : url
    })

# 3 ------------------------------------------------------

# 4 ------------------------------------------------------
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
# 4 ------------------------------------------------------