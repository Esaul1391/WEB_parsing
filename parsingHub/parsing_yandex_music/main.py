import requests
from pprint import pprint

cookies = {
    'i': 'yGkLgfuD8NoCNBTw8yG2Y6rVns8JVXQuz8UOz4u4Q6anx48Xn90HrwDs+UJSbB/ydrPLsF/dJSsg5ShbKbZSlaZEneU=',
    'yandexuid': '1954089821687403646',
    'yuidss': '1954089821687403646',
    'ymex': '2002763646.yrts.1687403646#2002763646.yrtsi.1687403646',
    'device_id': 'b591c287c9ea450b4fbb64fe77a6a7ea06d8b1ca7',
    'gdpr': '0',
    '_ym_uid': '1691723675829018450',
    '_ym_d': '1691723675',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'is_gdpr': '0',
    'is_gdpr_b': 'CMCmehD2xwE=',
    'bh': 'Ej8iTm90L0EpQnJhbmQiO3Y9Ijk5IiwiR29vZ2xlIENocm9tZSI7dj0iMTE1IiwiQ2hyb21pdW0iO3Y9IjExNSIaBSJ4ODYiIhAiMTE1LjAuNTc5MC4xMDIiKgI/MDoHIkxpbnV4IkIHIjYuMi4wIkoEIjY0IlJcIk5vdC9BKUJyYW5kIjt2PSI5OS4wLjAuMCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjExNS4wLjU3OTAuMTAyIiwiQ2hyb21pdW0iO3Y9IjExNS4wLjU3OTAuMTAyIiI=',
    '_yasc': 'WuRVZ99uEAu0M59r1Tu8IMzNQ7DKjLqaebNYW3HIjLBOFwCq50aT4qKJ58xdkTzg',
    'active-browser-timestamp': '1691724090629',
}

headers = {
    'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'i=yGkLgfuD8NoCNBTw8yG2Y6rVns8JVXQuz8UOz4u4Q6anx48Xn90HrwDs+UJSbB/ydrPLsF/dJSsg5ShbKbZSlaZEneU=; yandexuid=1954089821687403646; yuidss=1954089821687403646; ymex=2002763646.yrts.1687403646#2002763646.yrtsi.1687403646; device_id=b591c287c9ea450b4fbb64fe77a6a7ea06d8b1ca7; gdpr=0; _ym_uid=1691723675829018450; _ym_d=1691723675; _ym_visorc=b; _ym_isad=2; is_gdpr=0; is_gdpr_b=CMCmehD2xwE=; bh=Ej8iTm90L0EpQnJhbmQiO3Y9Ijk5IiwiR29vZ2xlIENocm9tZSI7dj0iMTE1IiwiQ2hyb21pdW0iO3Y9IjExNSIaBSJ4ODYiIhAiMTE1LjAuNTc5MC4xMDIiKgI/MDoHIkxpbnV4IkIHIjYuMi4wIkoEIjY0IlJcIk5vdC9BKUJyYW5kIjt2PSI5OS4wLjAuMCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjExNS4wLjU3OTAuMTAyIiwiQ2hyb21pdW0iO3Y9IjExNS4wLjU3OTAuMTAyIiI=; _yasc=WuRVZ99uEAu0M59r1Tu8IMzNQ7DKjLqaebNYW3HIjLBOFwCq50aT4qKJ58xdkTzg; active-browser-timestamp=1691724090629',
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https%3A%2F%2Fmusic.yandex.ru%2Fchart',
    'X-Yandex-Music-Client': 'YandexMusicAPI',
    'X-Yandex-Music-Client-Now': '2023-08-11T06:21:30+03:00',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'tracks': '115748634:26697445,115517682:26605629,112140181:25163882,112632320:25361122,115522025:26607707,112693028:25385537,115451099:26579125,114701796:26238268,113376105:26499893,109140203:24375438,113871114:25875093,50685843:7019257,116012279:26803721,104964266:22820453,115063213:26419633,113285377:25635984,114664869:26221804,50684233:7018993,114895248:26336809,113370433:25672468,110761858:24654032,115672310:26667711,113661081:25800222,107653457:23641665,115485659:26593713,112444127:25284420,29238706:10101,105406145:22820453,50685846:7019257,113680839:25808674,114336240:26084871,108205536:23837070,115433700:26571370,110081927:24402993,106246540:23135125,113294491:25639874,35505245:20559909,29238709:10101,115632229:26654240,115335620:26529556,114837104:26305205,111669627:24993584,115883706:26755011,106985401:23394439,93390818:18809983,3853787:124660,110788479:24663805,85192958:16230309,114345082:26088987,68348389:11322908,113690749:25813377,111556054:24945899,105944312:23018502,111857721:25058177,110944794:24720291,115450634:26578859,96477413:19764217,115710952:26680980,113843305:25863611,106314854:23211206,111276286:24844942,104263691:22820453,50688560:7019820,106339740:23164374,115901417:26762552,109989526:24375438,104102778:22347956,110761857:24654032,107314429:23521469,64072310:10252343,116079967:26830617,39958859:11999153,115597280:26639612,111888791:25068779,113847117:25864974,50685850:7019257',
    'withProgress': 'true',
    'external-domain': 'music.yandex.ru',
    'overembed': 'no',
    '__t': '1691724090911',
}

response = requests.get('https://music.yandex.ru/api/v2.1/handlers/tracks', params=params, cookies=cookies,
                        headers=headers)
# print(response.status_code)
# pprint(response.json())
count = 0
for trak in response.json():
    count = count + 1
    position = count

    track_name = trak['title']



    artist = ''
    for i in trak['artists']:
        artist += i['name'] + ', '

    print(f"N{position} - {artist.strip().strip(',')} - {track_name.strip()}")


