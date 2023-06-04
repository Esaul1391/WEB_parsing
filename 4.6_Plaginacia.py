from bs4 import BeautifulSoup
import requests

# Открываем сайт
# Проходимся по всем страницам в категории мыши (всего  4 страницы)

# find all chunk of url, which have information about names of mouses
url = 'https://parsinger.ru/html/index3_page_1.html' #
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# url_chunks = (tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a'))
div = soup.find('div', {'class': 'pagen'}).find_all('a')
lik_list = []
shema = 'https://parsinger.ru/html/'
for i in div:
    lik_list.append(f"{shema}{i['href']}")


print(lik_list)
# На каждой странице посещаем каждую карточку с товаром (всего 32 товаров)
# В каждой карточке извлекаем при помощи bs4 артикул <p class="article"> Артикул: 80244813 </p>
# Складываем(плюсуем) все собранные значения
# Вставляем получившийся результат в поле ответа
m = []
total = []
for j in lik_list:
    response = requests.get(url=j)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    a = soup.find_all('a', {'class': 'name_item'})
    for c in a:
        m.append(c['href'])
    for link in m:
        response = requests.get(url=f'https://parsinger.ru/html/{link}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        total.append(int(soup.find('p', {'class': 'article'}).text.split()[1]))

print(len(total))

# from bs4 import BeautifulSoup
# import requests
#
#
# # find all chunk of url, which have information about names of mouses
# url = 'https://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# url_chunks = (tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a'))
#
# # find articles of products on pages of website
# t = []
#
# for c in url_chunks:
#     response = requests.get(url=f'https://parsinger.ru/html/{c}')
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     mouses = (tag['href'] for tag in soup.find_all('a', {'class': 'name_item'}))
#     for link in mouses:
#         response = requests.get(url=f'https://parsinger.ru/html/{link}')
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         t.append(int(soup.find('p', {'class': 'article'}).text.split()[1]))
#
#
# print(len(t))