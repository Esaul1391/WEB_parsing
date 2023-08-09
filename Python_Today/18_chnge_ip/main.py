import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36'
}
def get_location(url):
    s = requests.session()
    response = s.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    ip = soup.find('div', class_='ip').find('span').text.strip()
    location = soup.find('div', class_='value value-country').text.strip()
    print(ip, location)

def main():
    get_location(url='https://2ip.ru/')


if __name__ == "__main__":
    main()
