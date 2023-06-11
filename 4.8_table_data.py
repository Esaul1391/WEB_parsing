#           task1

# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://parsinger.ru/table/1/index.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# table_set = sum({float(str(i)[4:-5]) for i in soup.find_all('td')}) # нахожу все элементы td и делаю из них множество уникальных элементов
# print(table_set)


#           task2
# find all items from the first column
# soup.select('table tr td:nth-of-type(1)')
# soup.select('td:first-child')

from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/table/2/index.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
data_list_total = sum([float(str(i)[4:-5]) for i in soup.select('td:first-child')])
print(data_list_total)
