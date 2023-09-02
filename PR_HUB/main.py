import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

resource = requests.get(url)
soup = BeautifulSoup(resource.text, 'lxml')
data = soup.find('div', class_='w-full rounded border')
name = data.find('h4')
print(name.text.replace('\n', ''))