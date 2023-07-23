import requests
from bs4 import BeautifulSoup
import json

# person_url_list = []
# for i in range(0, 740, 20):
#     url = f"{i}"
#
#     q = requests.get(url)
#     results = q.content
#
#     soup = BeautifulSoup(results, 'lxml')
#     persons = soup.find_all(class_ = 'need_tag')
#
#     for person in persons:
#         persons_page_url = person.get('href')
#         person_url_list.append(persons_page_url)
#
#
# with open('person_url_list.txt', "a") as file:
#     for line in person_url_list:
#         file.write(f"{line}\n")



with open('person_url_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]


    data_dict = []
    for line in lines:
        q = requests.get(line)
        result = q.content

    soup = BeautifulSoup(result, 'lxml')
    person = soup.find(class_='...').find('h3').text
    person_name_company = person.strip().split(',')
    person_name = person_name_company[0]
    person_name_company = person_name_company[1].strip()

    social_networks = soup.find_all(class_= '...')
    social_networks_urls = []
    for item in social_networks:
        social_networks_urls.append(item.get('href'))


    data = {
        'p': person_name,
        'c': person_name_company,
        'n': social_networks_urls
    }

    data_dict.append(data)

    with open('data.json', 'w') as json_file:
        json.dump(data_dict, json_file, indent=4, )