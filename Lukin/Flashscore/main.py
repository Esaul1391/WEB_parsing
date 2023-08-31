import json

import requests

headers = {
    'authority': 'local-ruua.flashscore.ninja',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'origin': 'https://www.flashscorekz.com',
    'referer': 'https://www.flashscorekz.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36',
    'x-fsign': 'SW9D1eZo',
    'x-geoip': '1',
}

response = requests.get('https://local-ruua.flashscore.ninja/46/x/feed/f_1_0_-1_ru-kz_1', headers=headers)
data = response.text.split('¬')

data_list = [{}]
for item in data[:10]:
    key = item.split('÷')[0]
    value = item.split('÷')[-1]
    if '~' in key:
        data_list.append({key: value})
    else:

        data_list[-1].update({key: value})


for elements in data_list:
    print(json.dumps(elements,ensure_ascii=False, indent=2))


