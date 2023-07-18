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


# import requests
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
# import lxml
# import time
#
# url = 'https://3dtoday.ru/'
# ua = UserAgent()
#
#
# fake_ua = {'user-agent': ua.random}
# response = requests.get(url=url, headers=fake_ua)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# pagen = soup.find('div', class_='posts-list').find_all('a')
# # pr = soup.find('title')
# # print(pr)
#
# #print(response.text)



from bs4 import BeautifulSoup
import requests
import re

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find_all(re.compile(''))
print(pagen)
print(response.text)

