import csv
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

ua = UserAgent
proxi = {
    'http': 'http://162.223.94.164'
}


def get_data(url):
    s = requests.session()
    response = s.get(url=url, headers={'user-agent': f'{ua.random}'}, proxies=proxi)
    with open(file='index.html', mode='w') as file:
        file.write(response.text)

    with open(file="index.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('table', id='')

    data_th = table.find('thead').find_all('tr')[-1].find_all('th')
    table_head = []
    for dth in data_th:
        dth = dth.text.strip()
        table_head.append(dth)

    with open(file='3d.csv', mode='w') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                table_head
            )
        )
def main():
    get_data(url="https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm")


if __name__ == "__main__":
    main()
