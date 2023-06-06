from bs4 import BeautifulSoup
import requests

# find all chunk of url, which have information about names of mouses
# url = 'https://parsinger.ru/html/index3_page_1.html'
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
url_chunks = [tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a')]

print(url_chunks)
# find articles of products on pages of website

total = 0
for c in url_chunks:
    response = requests.get(url=f'https://parsinger.ru/html/{c}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    mouses = [tag['href'] for tag in soup.find_all('a', {'class': 'name_item'})]
    print(mouses)
    for link in mouses:
        response = requests.get(url=f'https://parsinger.ru/html/{link}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        stock = int(soup.find('span', {'id': 'in_stock'}).text.split()[-1])
        price = int(soup.find('span', {'id': 'price'}).text.split()[0])
        total += stock * price
        print(total)
        # print(int(soup.find('p', {'class': 'article'}).text.split()[1]))
#
print(total)