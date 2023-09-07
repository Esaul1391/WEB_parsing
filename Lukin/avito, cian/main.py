import requests
from selectolax.parser import HTMLParser # like Selenium, instead


def get_html(url):
    response = requests.get(url=url)
    html = response.text

    tree = HTMLParser(html)
    # items = tree.css('div[data-marker="item"]')
    scripts = tree.css('script')
    for script in scripts:
        if 'window.__initialData__' in script.text():
            print(script.text().split(';')[0].split('=')[-1].strip())




def main():
    url = 'https://www.avito.ru/moskva/kvartiry/prodam/ipoteka-ASgBAQICAUSSA8YQAUDm6w4UAg?f=ASgBAQECAkSSA8YQwMENuv03BkDKCCSAWYJZ5hYU5vwBrL4NFKTHNY7eDhQCkN4OFALm6w4UAgJFhAkVeyJmcm9tIjozMCwidG8iOm51bGx9xpoMHXsiZnJvbSI6NTAwMDAwMCwidG8iOjgwMDAwMDB9'
    get_html(url)
if __name__ == '__main__':
    main()