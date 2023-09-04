import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep


headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36'
}

def download(url):
    resp = requests.get(url, stream=True)   # Добавляю потоковую передачу файла
    r = open(r'/home/esaul/PycharmProjects/Parsing/PR_HUB/imges' + url.split('/')[-1], 'wb')    #   прописываю как должен сохраниться файл
    for value in resp.iter_content(1024 * 1024):    #   1 мегабайт за один проход
        r.write(value)
    r.close()

#   создаю список страниц
def get_url():
    for count in range(1, 7):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        request = requests.get(url, headers=headers)
        soup = BeautifulSoup(request.text, 'lxml')
        data = soup.find_all('div', class_='w-full rounded border')
        # for i in data:
        #     name = i.find('h4').text.replace('\n', '')
        #     price = i.find('h5').text
        #     link = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')   #использую для скачивания картинки
        #     print(name, price, link)
        for i in data:
            card_link = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_link    #    Генератор списков

#
def array():
    for card_url in get_url():
        request = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(request.text, 'lxml')
        data = soup.find('div', class_='my-8 w-full rounded border')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4', class_='my-4 card-price').text
        text = data.find('p', class_='card-description').text
        url_img = 'https://scrapingclub.com' + data.find('img').get('src')
        download(url_img)
        yield name, price, text, url_img



