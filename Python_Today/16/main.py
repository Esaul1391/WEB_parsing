import json

import requests

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36'
}


def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    with open("index.html", 'w') as file:
        file.write(response.text)


def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("result.json", 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def collect_data():
    s = requests.Session()
    response = s.get(url="https://www.salomon.com/en-us/shop/men/shoes/shopby/11_5_men_s_53862/standard_17509.html?p=2&is_scroll=1")

    data = response.json()
    pagination_count = data.get("pagination").get('pageCount')

    for page_count in range(1, pagination_count + 1):
        url = f"https://www.salomon.com/en-us/shop/men/shoes/shopby/11_5_men_s_53862/standard_17509.html?p=2&is_scroll={page_count}"
        r = s.get(url=url, headers=headers)

        data = r.json()
        
def main():
    get_page(url="https://www.salomon.com/en-us/shop/men/shoes.html")
    get_json(url='https://www.salomon.com/en-us/shop/men/shoes/shopby/11_5_men_s_53862/standard_17509.html?p=2&is_scroll=1')

if __name__ == "__main__":
    main()
