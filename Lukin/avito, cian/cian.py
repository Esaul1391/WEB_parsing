import requests
import json
def get_json():
    cookies = {
        '_CIAN_GK': '732ac201-83d7-4c84-a538-4cf1ecd4e12c',
        'session_region_id': '1',
        '__cf_bm': 'xFIymp4g6R_ZlUDF5CUU4xn8CA1J8f8q2aBil9FtDMo-1694229473-0-Ac/rvWprbHb0BST/AHiN7GaUZpGYl+Is3oWYq5yzFXbYFZVjjnBUx3tHaO1OPVU8LO3AOQ5yw3GqIBj/VKitUHw=',
        'adb': '1',
        '_gcl_au': '1.1.1446704131.1694229468',
        'tmr_lvid': 'bc99076ac457c4fe3f7def93c4f0e1fa',
        'tmr_lvidTS': '1689671002137',
        'login_mro_popup': '1',
        'sopr_utm': '%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
        'sopr_session': 'cc53b2bd62454870',
        'uxfb_usertype': 'searcher',
        '_ym_uid': '1689671003222889986',
        '_ym_d': '1694229469',
        '_gid': 'GA1.2.646497176.1694229469',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'afUserId': '45016ce9-c329-4610-8972-5ea04003f109-p',
        'AF_SYNC': '1694229469174',
        'session_main_town_region_id': '1',
        'viewpageTimer': '436.68899999999996',
        '_ga': 'GA1.2.309077661.1694229468',
        '_dc_gtm_UA-30374201-1': '1',
        '_ga_3369S417EL': 'GS1.1.1694229468.1.1.1694230016.60.0.0',
    }

    headers = {
        'authority': 'api.cian.ru',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_CIAN_GK=732ac201-83d7-4c84-a538-4cf1ecd4e12c; session_region_id=1; __cf_bm=xFIymp4g6R_ZlUDF5CUU4xn8CA1J8f8q2aBil9FtDMo-1694229473-0-Ac/rvWprbHb0BST/AHiN7GaUZpGYl+Is3oWYq5yzFXbYFZVjjnBUx3tHaO1OPVU8LO3AOQ5yw3GqIBj/VKitUHw=; adb=1; _gcl_au=1.1.1446704131.1694229468; tmr_lvid=bc99076ac457c4fe3f7def93c4f0e1fa; tmr_lvidTS=1689671002137; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D; sopr_session=cc53b2bd62454870; uxfb_usertype=searcher; _ym_uid=1689671003222889986; _ym_d=1694229469; _gid=GA1.2.646497176.1694229469; _ym_isad=1; _ym_visorc=b; afUserId=45016ce9-c329-4610-8972-5ea04003f109-p; AF_SYNC=1694229469174; session_main_town_region_id=1; viewpageTimer=436.68899999999996; _ga=GA1.2.309077661.1694229468; _dc_gtm_UA-30374201-1=1; _ga_3369S417EL=GS1.1.1694229468.1.1.1694230016.60.0.0',
        'origin': 'https://www.cian.ru',
        'referer': 'https://www.cian.ru/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36',
    }

    json_data = {
        'jsonQuery': {
            '_type': 'flatsale',
            'sort': {
                'type': 'term',
                'value': 'creation_date_desc',
            },
            'engine_version': {
                'type': 'term',
                'value': 2,
            },
            'region': {
                'type': 'terms',
                'value': [
                    1,
                ],
            },
            'price': {
                'type': 'range',
                'value': {
                    'gte': 5000000,
                    'lte': 8000000,
                },
            },
            'currency': {
                'type': 'term',
                'value': 2,
            },
            'foot_min': {
                'type': 'range',
                'value': {
                    'lte': 30,
                },
            },
            'only_foot': {
                'type': 'term',
                'value': '2',
            },
            'room': {
                'type': 'terms',
                'value': [
                    1,
                    2,
                ],
            },
            'total_area': {
                'type': 'range',
                'value': {
                    'gte': 30,
                },
            },
            'only_flat': {
                'type': 'term',
                'value': True,
            },
        },
    }

    response = requests.post(
        'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"jsonQuery":{"_type":"flatsale","sort":{"type":"term","value":"creation_date_desc"},"engine_version":{"type":"term","value":2},"region":{"type":"terms","value":[1]},"price":{"type":"range","value":{"gte":5000000,"lte":8000000}},"currency":{"type":"term","value":2},"foot_min":{"type":"range","value":{"lte":30}},"only_foot":{"type":"term","value":"2"},"room":{"type":"terms","value":[1,2]},"total_area":{"type":"range","value":{"gte":30}},"only_flat":{"type":"term","value":true}}}'
    # response = requests.post(
    #    'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    # )
    data = response.json()
    with open('data_cian.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

    return data
def get_offers(data):
    offers = []

    for item in data['data']['offersSerialized']:

        offer = {}
        offer["price"] = item["bargainTerms"]["priceRur"]
        offer["address"] = item["geo"]["userInput"]
        offer["area"] = item["totalArea"]
        offer["rooms"] = item["roomsCount"]
        offer["floor"] = item["floorNumber"]
        offer["total_floor"] = item["building"]["floorsCount"]
        offers.append(offer)
        print(offer)
    return offers

def main():
    data = get_json()
    # print(data)
    get_offers(data)
    # 'https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&foot_min=30&maxprice=8000000&minprice=5000000&mintarea=30&offer_type=flat&only_flat=1&only_foot=2&region=1&room1=1&room2=1&sort=creation_date_desc'

if __name__ == '__main__':
    main()