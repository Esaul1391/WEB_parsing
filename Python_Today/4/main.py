import requests
from bs4 import BeautifulSoup
import json
import lxml

#collectios all festival
fest_urls_list = []

headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36'
}

for i in range(0, 170, 24):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=23%20Jul%202023&to_date=&maxprice=500&o={i}&bannertitle=July"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]

    with open(f"data/index_{i}.html", "w") as file:
        file.write(html_response)

    with open(f"data/index_{i}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    cards = soup.find_all('a', class_='card-details-link')

    #take url from href
    for item in cards:
        fest_url = 'https://www.skiddle.com' + item.get("href")
        fest_urls_list.append(fest_url)

#   take info from every url
for url in fest_urls_list:

    req = requests.get(url=url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        fest_name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text.strip()
        fest = soup.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol')
        data_fest = fest[0].find('span').text
        local_fest = fest[1].find('span').text
        # price_fest = fest[2].find('span').text
        # local_fest = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 css-2re0kq').find('span', style="font-weight:600")

        # get contakt
    except Exception as ex:
        print(ex)
        print("Damp... There was some error...")

