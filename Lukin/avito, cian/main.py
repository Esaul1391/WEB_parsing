import requests
from selectolax.parser import HTMLParser # like Selenium, instead
from urllib.parse import unquote
import json

def get_html(url):
    response = requests.get(url=url)
    html = response.text

    tree = HTMLParser(html)
    # items = tree.css('div[data-marker="item"]')
    scripts = tree.css('script')
    for script in scripts:
        if 'window.__initialData__' in script.text():
            jsontext = script.text().split(';')[0].split('=')[-1].strip()
            jsontext = unquote(jsontext)
            jsontext = jsontext[1:-1]
            data = json.loads(jsontext)
            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)


def get_offer(data):
    for key in data:
        if 'single-page' in key:
            items = data[key]['data']['catalog']["items"]
            for item in items:
                if item.get('id'):  # if element don't none, print element
                    price = item["priceDetailed"]['value']
                    title = item['title']
                    url = item['urlPath']
                    time = item['sortTimeStamp']
                    print(price)



def main():
    # url = 'https://www.avito.ru/moskva/kvartiry/prodam/ipoteka-ASgBAQICAUSSA8YQAUDm6w4UAg?f=ASgBAQECAkSSA8YQwMENuv03BkDKCCSAWYJZ5hYU5vwBrL4NFKTHNY7eDhQCkN4OFALm6w4UAgJFhAkVeyJmcm9tIjozMCwidG8iOm51bGx9xpoMHXsiZnJvbSI6NTAwMDAwMCwidG8iOjgwMDAwMDB9'
    # get_html(url)

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        get_offer(data)

if __name__ == '__main__':
    main()