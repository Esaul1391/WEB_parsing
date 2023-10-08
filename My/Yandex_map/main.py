import requests
from bs4 import BeautifulSoup
import json

# URL веб-сайта, с которого вы хотите получить данные
url = 'https://yandex.ru/maps/213/moscow/search/больницы/?ll=37.505673%2C55.731559&sll=37.505673%2C55.731559&sspn=0.476532%2C0.149752&z=12'

# Отправляем GET-запрос на сайт
cookies = {
    'maps_los': '0',
    'i': 'gYKmcaeKFtDGCwJG8QSzEF/M8lg995NofZmuZ5kvGsymQJdPpIrU97nAJFtPrBen7hYBDmWlzJrK5jCvCWQulhigEBM=',
    'yandexuid': '2544707141696606517',
    'yuidss': '2544707141696606517',
    'ymex': '2011966523.yrts.1696606523',
    'gdpr': '0',
    'is_gdpr': '0',
    'is_gdpr_b': 'CJbqDxDC0gEoAg==',
    'yashr': '8556205601696606523',
    '_ym_uid': '1696606524686162400',
    'Session_id': '3:1696606558.5.0.1696606558154:H5mSwsBu0hPcaoqBcBMAKg:1e.1.2:1|141646791.0.2.3:1696606558|3:10276803.345471.w16FDKuf5omNi5Z-fgtE9ZjzX3k',
    'sessar': '1.1182.CiD8AGRWkXXxuL3BE9e_QmPkmesz0y8qOXAphQwLoLuTKw.11SRYKPoNmIBztBwdRRmlwHRmcy9CkIJJnn6S9fRT1E',
    'sessionid2': '3:1696606558.5.0.1696606558154:H5mSwsBu0hPcaoqBcBMAKg:1e.1.2:1|141646791.0.2.3:1696606558|3:10276803.345471.fakesign0000000000000000000',
    'L': 'aVcIYGt6cwZAB2VrX2FecwBffAdAaHBba1c3BjgrPFM=.1696606558.15487.327379.6dca9341a678d20ee3f0bd88823fed50',
    'yandex_login': 'Roninnn1',
    'bh': 'EjwiQ2hyb21pdW0iO3Y9IjExNiIsICJOb3QpQTtCcmFuZCI7dj0iMjQiLCAiWWFCcm93c2VyIjt2PSIyMyIaBSJ4ODYiIgwiMjMuOS4xLjk2MiIqAj8wMgIiIjoHIkxpbnV4IkIHIjYuMi4wIkoEIjY0IlJVIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjE4OCIsICJOb3QpQTtCcmFuZCI7dj0iMjQuMC4wLjAiLCAiWWFCcm93c2VyIjt2PSIyMy45LjEuOTYyIloCPzA=',
    '_ym_isad': '1',
    'cycada': 'c3loArfz7oeQNHuvPnYDf1+Y3/HCo6Ty6jWTo+7EFdk=',
    'sae': '0:be925935-7c4c-4be0-89e0-bf87703BF96A:p:23.9.1.962:l:d:EN-US:20231006',
    '_ym_d': '1696736536',
    'bh': 'EjoiQ2hyb21pdW0iO3Y9IjExNiIsIk5vdClBO0JyYW5kIjt2PSIyNCIsIllhQnJvd3NlciI7dj0iMjMiGgUieDg2IiIMIjIzLjkuMS45NjIiKgI/MDoHIkxpbnV4IkIHIjYuMi4wIkoEIjY0IlJUIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjE4OCIsIk5vdClBO0JyYW5kIjt2PSIyNC4wLjAuMCIsIllhQnJvd3NlciI7dj0iMjMuOS4xLjk2MiIi',
    '_yasc': 'jGPSAWStKucW+b7LlyZFtggX+GwmCNRvcvFIdhLpxJ6rCtgDLPAP0dAv7cWxhQUkGhZzKWvZJ1cBi4+Fqw==',
    'ys': 'svt.1#def_bro.1#ead.2FECB7CF#wprid.1696736807231379-12967696952869565635-balancer-l7leveler-kubr-yp-vla-152-BAL-1412#ybzcc.ru#newsca.native_cache',
    'yp': '1696822765.uc.us#1696822765.duc.us#1728142558.cld.2574584#2011966558.udn.cDpSb25pbm5uMQ%3D%3D#2012096808.pcs.0#1697211462.szm.1:1920x1080:1872x893#1699285172.hdrc.1#1696909695.gpauto.55_595607:37_616252:140:0:1696736885',
}

headers = {
    'authority': 'yandex.ru',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': 'maps_los=0; i=gYKmcaeKFtDGCwJG8QSzEF/M8lg995NofZmuZ5kvGsymQJdPpIrU97nAJFtPrBen7hYBDmWlzJrK5jCvCWQulhigEBM=; yandexuid=2544707141696606517; yuidss=2544707141696606517; ymex=2011966523.yrts.1696606523; gdpr=0; is_gdpr=0; is_gdpr_b=CJbqDxDC0gEoAg==; yashr=8556205601696606523; _ym_uid=1696606524686162400; Session_id=3:1696606558.5.0.1696606558154:H5mSwsBu0hPcaoqBcBMAKg:1e.1.2:1|141646791.0.2.3:1696606558|3:10276803.345471.w16FDKuf5omNi5Z-fgtE9ZjzX3k; sessar=1.1182.CiD8AGRWkXXxuL3BE9e_QmPkmesz0y8qOXAphQwLoLuTKw.11SRYKPoNmIBztBwdRRmlwHRmcy9CkIJJnn6S9fRT1E; sessionid2=3:1696606558.5.0.1696606558154:H5mSwsBu0hPcaoqBcBMAKg:1e.1.2:1|141646791.0.2.3:1696606558|3:10276803.345471.fakesign0000000000000000000; L=aVcIYGt6cwZAB2VrX2FecwBffAdAaHBba1c3BjgrPFM=.1696606558.15487.327379.6dca9341a678d20ee3f0bd88823fed50; yandex_login=Roninnn1; bh=EjwiQ2hyb21pdW0iO3Y9IjExNiIsICJOb3QpQTtCcmFuZCI7dj0iMjQiLCAiWWFCcm93c2VyIjt2PSIyMyIaBSJ4ODYiIgwiMjMuOS4xLjk2MiIqAj8wMgIiIjoHIkxpbnV4IkIHIjYuMi4wIkoEIjY0IlJVIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjE4OCIsICJOb3QpQTtCcmFuZCI7dj0iMjQuMC4wLjAiLCAiWWFCcm93c2VyIjt2PSIyMy45LjEuOTYyIloCPzA=; _ym_isad=1; cycada=c3loArfz7oeQNHuvPnYDf1+Y3/HCo6Ty6jWTo+7EFdk=; sae=0:be925935-7c4c-4be0-89e0-bf87703BF96A:p:23.9.1.962:l:d:EN-US:20231006; _ym_d=1696736536; bh=EjoiQ2hyb21pdW0iO3Y9IjExNiIsIk5vdClBO0JyYW5kIjt2PSIyNCIsIllhQnJvd3NlciI7dj0iMjMiGgUieDg2IiIMIjIzLjkuMS45NjIiKgI/MDoHIkxpbnV4IkIHIjYuMi4wIkoEIjY0IlJUIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjE4OCIsIk5vdClBO0JyYW5kIjt2PSIyNC4wLjAuMCIsIllhQnJvd3NlciI7dj0iMjMuOS4xLjk2MiIi; _yasc=jGPSAWStKucW+b7LlyZFtggX+GwmCNRvcvFIdhLpxJ6rCtgDLPAP0dAv7cWxhQUkGhZzKWvZJ1cBi4+Fqw==; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1696736807231379-12967696952869565635-balancer-l7leveler-kubr-yp-vla-152-BAL-1412#ybzcc.ru#newsca.native_cache; yp=1696822765.uc.us#1696822765.duc.us#1728142558.cld.2574584#2011966558.udn.cDpSb25pbm5uMQ%3D%3D#2012096808.pcs.0#1697211462.szm.1:1920x1080:1872x893#1699285172.hdrc.1#1696909695.gpauto.55_595607:37_616252:140:0:1696736885',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1',
    'ect': '4g',
    'referer': 'https://yandex.ru/maps/213/moscow/?ll=37.562561%2C55.728567&z=12',
    'rtt': '50',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"23.9.1.962"',
    'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "YaBrowser";v="23.9.1.962"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"6.2.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.962 YaBrowser/23.9.1.962 Yowser/2.5 Safari/537.36',
    'viewport-width': '892',
    'x-retpath-y': 'https://yandex.ru/maps/213/moscow/?ll=37.562561%2C55.728567&z=12',
}

params = {
    'add_type': 'direct',
    'ajax': '1',
    'client_usecase': 'suggest',
    'csrfToken': '481a26a3ea920bc0d9877d3462af251659dde6ae:1696736893',
    'direct_page_id': '670942',
    'experimental_business_show_exp_features[0]': 'only_byak_prod',
    'experimental_business_show_exp_features[1]': 'cbrf',
    'experimental_rearr[0]': 'scheme_Local/Geo/Collections/Peredelkino=1',
    'internal_pron[addPhotoButtonOnMap]': 'true',
    'internal_pron[centralBankCollaboration]': 'true',
    'internal_pron[extendConfig][banner][blockIds][home][hd]': 'R-I-142300-323',
    'internal_pron[extendConfig][banner][blockIds][home][sd]': 'R-I-142300-324',
    'internal_pron[extendConfig][business][enableHotelsBooking]': 'false',
    'internal_pron[extendConfig][business][enableRealty]': '',
    'internal_pron[flyover]': 'true',
    'internal_pron[flyoverAttractionsMskSpb]': 'true',
    'internal_pron[graphicsFpsMeter]': 'true',
    'internal_pron[groupSuggestBackend]': 'true',
    'internal_pron[groupSuggestDesktop]': 'true',
    'internal_pron[groupSuggestParanjaDesktop]': 'true',
    'internal_pron[isMoreSpaceInReviewForm]': 'true',
    'internal_pron[isUgcVideoShowing]': 'true',
    'internal_pron[isVideoShowingInReviews]': 'true',
    'internal_pron[isVideoUploadingToReviews]': 'true',
    'internal_pron[lightUgcAchievements]': 'true',
    'internal_pron[portalProductsTab]': 'true',
    'internal_pron[tile3dPing]': 'true',
    'internal_pron[toponymSearchNearby]': 'true',
    'internal_pron[ugcUserStats]': 'true',
    'internal_pron[ugcUserStatsPage]': 'true',
    'internal_pron[vectorGraphics]': 'true',
    'internal_pron[vectorRichModelsEnabled]': 'true',
    'lang': 'ru_RU',
    'll': '37.562561,55.728567',
    'origin': 'maps-form',
    'parent_reqid': '1696736895546607-62739714-addrs-upper-yp-95',
    'results': '25',
    's': '4188797374',
    'sessionId': '1696736893555_763951',
    'snippets': 'masstransit/2.x,panoramas/1.x,businessrating/1.x,businessimages/1.x,photos/2.x,videos/1.x,experimental/1.x,subtitle/1.x,visits_histogram/2.x,tycoon_owners_personal/1.x,tycoon_posts/1.x,related_adverts/1.x,related_adverts_1org/1.x,city_chains/1.x,route_point/1.x,topplaces/1.x,metrika_snippets/1.x,place_summary/1.x,online_snippets/1.x,building_info_experimental/1.x,provider_data/1.x,service_orgs_experimental/1.x,business_awards_experimental/1.x,business_filter/1.x,histogram/1.x,attractions/1.x,potential_company_owners:user,pin_info/1.x,lavka/1.x,bookings/1.x,bookings_personal/1.x,trust_features/1.x,plus_offers_experimental/1.x,toponym_discovery/1.x,relevant_discovery/1.x,visual_hints/1.x,fuel/1.x,realty_experimental/2.x,matchedobjects/1.x,discovery/1.x,topobjects/1.x,hot_water/1.x,neurosummary,mentioned_on_site/1.x,showtimes/1.x,afisha_json_geozen/1.x,encyclopedia/2.x/pb,stories_experimental/1.x,realty_buildings/1.x',
    'spn': '0.140076,0.149763',
    'test-buckets': '883661,0,61;681842,0,8;878599,0,53;663874,0,22;663860,0,57;881201,0,77;875212,0,68;753240,0,98;877731,0,61;877853,0,76',
    'text': 'больницы',
    'ull': '37.616253,55.595608',
    'yandex_gid': '120581',
    'z': '12',
}

# response = requests.get('https://yandex.ru/maps/api/search', params=params, cookies=cookies, headers=headers)
#
# # Проверяем успешность запроса
# if response.status_code == 200:
#     # Используем BeautifulSoup для анализа HTML-страницы
#     json_data = response.json()
#
#     # Определите имя файла, в который вы хотите записать JSON-данные
#     filename = 'data.json'
#
#     # Открываем файл для записи данных
#     with open(filename, 'w', encoding='utf-8') as json_file:
#         # Записываем JSON-данные в файл
#         json.dump(json_data, json_file, ensure_ascii=False, indent=4)
#
#     print(f'Данные успешно записаны в файл {filename}')
#
# else:
#     print(f'Ошибка при запросе к странице. Код состояния: {response.status_code}')


with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Проверяем наличие ключа 'data' и 'items' в JSON-данных
if 'data' in data and 'items' in data['data']:
    # Получаем данные из 'data' и 'items'
    data_data = data['data']['items']


    # Теперь у вас есть доступ к информации в 'data' и 'items'
    # Можете выполнять операции с этими данными

    # Пример вывода первого элемента в 'items'
    print(data_data[1])
    for item in data_data:
        print(item['title'])
        print(item['fullAddress'])
        phone_numbers = [phone['value'] for phone in item['phones'] if 'value' in phone]
        print(phone_numbers)
        r = item["ratingData"]
        print(r['ratingCount'], round(r['ratingValue'], 1))



else:
    print('Отсутствуют ключи "data" или "items" в JSON-данных')


