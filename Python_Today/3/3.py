import json

import requests
from bs4 import BeautifulSoup


# Создаю копию HTML странцы для удобства работы, после закоментировать
def get_data(url):
        # req = requests.get(url)
        #
        # with open('elecktronick.html', 'w') as file:
        #     file.write(req.text)

    with open('elecktronick.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find_all('div', class_='entry-box clearfix')

    project_url = []
    for artickle in articles:
        pr_url = artickle.find('p', class_='more-link-box').find('a').get("href")
        project_url.append(pr_url)

    projects_data_list = []
    for proj_url in project_url:
        req = requests.get(proj_url)
        project_name = proj_url.split('/')[-2]

        with open(f"date/{project_name}.html", "w") as file:
            file.write(req.text)

        with open(f"date/{project_name}.html") as file:
            src = file.read()

        try:
            soup = BeautifulSoup(src, "lxml")
            project_data = soup.find('h1').text
            pr_content = soup.find('div', id="toc_container").find_all('a')
            tx = ''
            for i in pr_content:
                tx = tx + i.text + '\n'
        except:
            project_data = 'No project info'

        projects_data_list.append(
            {
                "Имя проекта": project_data,
                "Содержание":tx
            }
        )
    with open("date/projects_data.json", "a", encoding='utf-8') as file:
        json.dump(projects_data_list, file, indent=4, ensure_ascii=False)



get_data("https://www.ruselectronic.com/")
