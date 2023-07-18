import requests
from bs4 import BeautifulSoup


# Создаю копию HTML странцы для удобства работы, после закоментировать
def get_data(url):
    #     req = requests.get(url)
    #
    #     with open('elecktronick.html', 'w') as file:
    #         file.write(req.text)

    with open('elecktronick.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find_all('div', class_='entry-box clearfix')
    project_url = []

    for artickle in articles:
        pr_url = artickle.find('p', class_='more-link-box').find('a').get("href")
        project_url.append(pr_url)
    print(project_url)

    for proj_url in project_url:
        req = requests.get(proj_url)
        project_name = proj_url.split('/')[-2]

        with open(f"data/{project_name}.html", "w") as file:
            file.write(req.text)

        with open(f"data/{project_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        project_data = soup.find('itemprop', "headline")
        print(project_data)


get_data("https://www.ruselectronic.com/")
