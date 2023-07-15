# from bs4 import BeautifulSoup
# import requests
#
# # Открываем сайт
# # Проходимся по всем страницам в категории мыши (всего  4 страницы)
#
# # find all chunk of url, which have information about names of mouses
# url = 'https://3dtoday.ru/' #
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
#
# p1 = soup.find('class')
# print(p1)


import requests
from random import choice

url = 'https://3dtoday.ru/'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)
