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

# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://parsinger.ru/table/2/index.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# data_list_total = sum([float(str(i)[4:-5]) for i in soup.select('td:first-child')])
# print(data_list_total)


#           task3
# find all items in the table wreite bold font

# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://parsinger.ru/table/3/index.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# data_list_total = sum([float(str(i)[3:-4]) for i in soup.select('b')])
# print(data_list_total)


#           task4
# find all items in the table green cells
# ('td', class_='green')

# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://parsinger.ru/table/4/index.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# data_list_total = sum([float(str(i)[18:-5]) for i in soup.find_all('td', attrs={'class': 'green'})])
# print(data_list_total)


#           task5
# find multiply orange items and blue items, after count total

# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://parsinger.ru/table/5/index.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# data_list_orange = [float(str(i)[19:-5]) for i in soup.find_all('td', class_='orange')]
# print(data_list_orange)
#
# # 1 option
# # count = 0
# # for i in soup.find('table').find_all('td'):
# #     count += 1
# #     if count == 15:
# #         print(i)
# #         count = 0
#
# # 2 option
# data_list_blue = [float(str(i)[4:-5]) for i in soup.find('table').select('td:last-child')]
# print(data_list_blue)
#
# res = sum([data_list_orange[i] * data_list_blue[i] for i in range(64)])
# print(res)


#           task5
#


from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
data_list_th = [str(i) for i in soup.find_all('th')]
print(data_list_th)
data_list_td = [0] * 15
count = 0
for i in soup.find('table').find_all('td'):
    print(str(i)[4:-5])
print(data_list_td)