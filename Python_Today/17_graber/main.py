import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36'
}


def get_articles_url(url):
    s = requests.session()
    response = s.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(soup.find('ul', class_="pager centered pager-new").find_all('a')[-2].text)
    articles_url_list = []
    for page in range(1, 3):
        response = s.get(url=f"https://3dtoday.ru/category/novosti?page={page}")
        soup = BeautifulSoup(response.text, "lxml")
        article_find = soup.find_all("span", class_='title_bg')
        for ur in article_find:
            art = ur.find('a').get('href')
            articles_url_list.append(art)

        time.sleep(randrange(2, 5))

    with open('articles_urls.txt', "w") as file:
        for url in articles_url_list:
            file.write(f'{url}\n')
    # with open("index.html", 'w') as file:
    #     file.write(response.text)

    return "job is done"


def get_data(file_path):
    with open(file_path) as file:
        url_list = [line.strip() for line in file.readlines()]  # cut \n
    s = requests.session()
    result_data = []
    for url in url_list:
        response = s.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('div', class_="main_col").find('h1').text
        post_data = soup.find('div', class_='post_list_item_date').text
        text = soup.find('div', class_='blog_post_body').text.strip()
        result_data.append(
            {
                'title': title,
                'post_data': post_data,
                "text": text
            }
        )
    with open("result.json", 'w') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    # get_articles_url("https://3dtoday.ru/category/novosti")
    get_data('articles_urls.txt')


if __name__ == "__main__":
    main()
