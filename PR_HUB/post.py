from requests import Session
from bs4 import BeautifulSoup
import lxml
from time import sleep

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36'
}

work = Session()

work.get("https://quotes.toscrape.com/", headers=headers)  # Имитация посещения сайта

response = work.get("https://quotes.toscrape.com/login", headers=headers)  # press button

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')

data = {"csrf_token": token, "username": 'naname', 'password': 'password'}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)
