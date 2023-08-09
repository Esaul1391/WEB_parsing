import requests
import os
import csv
import json
from datetime import datetime


def get_data():
    cookies = {
        '__js_p_': '631,1800,0,1,0',
        '__jhash_': '1092',
        '__jua_': 'Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20YaBrowser%2F23.5.1.667%20Yowser%2F2.5%20Safari%2F537.36',
        '__hash_': '9bbf3a15d739135d775273e6480c1516',
        '__lhash_': '165fd87fdb920ca5ea9205a7d036ad9c',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod1',
        '_gid': 'GA1.2.1063126713.1691464636',
        '_ym_uid': '1691464636452681862',
        '_ym_d': '1691464636',
        '_sp_ses.d61c': '*',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        'partnerSrc': 'yandex',
        '__SourceTracker': 'yandex__organic',
        'admitad_deduplication_cookie': 'yandex__organic',
        '__cpatrack': 'yandex_organic',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '1e433ea9965a7245bb422a88f1d811f1',
        'tmr_lvidTS': '1691464639557',
        'uxs_uid': '157db660-359a-11ee-ae2b-4bafc86f5ca5',
        'advcake_track_id': '5b04f9ec-6336-6b24-3993-023b33dbee4a',
        'advcake_session_id': '04bd74b2-bb40-7a30-46cc-a2ffed2546d0',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex',
        'advcake_utm_partner': 'yandex',
        'advcake_utm_webmaster': '',
        'advcake_click_id': '',
        'flocktory-uuid': '8aad07d3-beef-4f45-a5d1-34a472740c73-1',
        'afUserId': '68fb8b44-5059-4a79-9683-23085f3e3690-p',
        'AF_SYNC': '1691464647351',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
        'bIPs': '434929338',
        '_ga': 'GA1.2.1654867660.1691464636',
        'tmr_detect': '1%7C1691465232448',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_sp_id.d61c': 'c2327dc2-e2f3-43aa-9315-5d5e95c73c97.1691464636.1.1691465307..f977393c-f088-4973-863f-f1c4868ff353..fa914c9b-f381-4743-aa3f-41e3d50fb950.1691464636081.68',
        'gsscgib-w-mvideo': 'g16o20TG/ursiXeB4yatolBj3o9L9I6rFl4S2MBXBTFHGUuyTI4JG1STkKNGBk2GpLjKbhIolNy98o3aXGlHUDURDHH9bNxIMleHolR1sObG4sEwgRb6RPKTIVz+q/vBzQ3pnhKopQv37N14oPvL+s2lqlA96J3Pk4QHxZ3wV3TxwmehQYO8G5r+NX3m/KrVdfNydc1XUQxKfubbVxapXsNt5my3HAz6Or83b+G4bkTrFuQNGC28XJzPCIcFyCkRWLI=',
        'gsscgib-w-mvideo': 'g16o20TG/ursiXeB4yatolBj3o9L9I6rFl4S2MBXBTFHGUuyTI4JG1STkKNGBk2GpLjKbhIolNy98o3aXGlHUDURDHH9bNxIMleHolR1sObG4sEwgRb6RPKTIVz+q/vBzQ3pnhKopQv37N14oPvL+s2lqlA96J3Pk4QHxZ3wV3TxwmehQYO8G5r+NX3m/KrVdfNydc1XUQxKfubbVxapXsNt5my3HAz6Or83b+G4bkTrFuQNGC28XJzPCIcFyCkRWLI=',
        'fgsscgib-w-mvideo': 'qcQ7a5525a2254b3c816cc2c08629c0990587903',
        'fgsscgib-w-mvideo': 'qcQ7a5525a2254b3c816cc2c08629c0990587903',
        'gssc218': '',
        'cfidsgib-w-mvideo': 'PcpLTmrmIeeZQqSR8V55KNNMRV2RaiEVUK4f0oNHMXrouCY8XSpg/SNtsu9/PGyojiTWLoA9cwH82ABITQFwAuyzdWVttGDRa+0XjLoO99dfqESAVIu2HMETQ795t6rW6i7VqiS/NxGuNGE3ZtfjGpHutbsBt076OVRFjQ==',
        '_ga_CFMZTSS5FM': 'GS1.1.1691464636.1.1.1691465363.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1691464636.1.1.1691465363.20.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=72dbbbf3fc2c48448187f7e967e1876b,sentry-sample_rate=0.5,sentry-transaction=%2F,sentry-sampled=true',
        # 'cookie': '__js_p_=631,1800,0,1,0; __jhash_=1092; __jua_=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20YaBrowser%2F23.5.1.667%20Yowser%2F2.5%20Safari%2F537.36; __hash_=9bbf3a15d739135d775273e6480c1516; __lhash_=165fd87fdb920ca5ea9205a7d036ad9c; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_MINDBOX_DYNAMICALLY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod1; _gid=GA1.2.1063126713.1691464636; _ym_uid=1691464636452681862; _ym_d=1691464636; _sp_ses.d61c=*; _ym_isad=1; _ym_visorc=w; partnerSrc=yandex; __SourceTracker=yandex__organic; admitad_deduplication_cookie=yandex__organic; __cpatrack=yandex_organic; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=1e433ea9965a7245bb422a88f1d811f1; tmr_lvidTS=1691464639557; uxs_uid=157db660-359a-11ee-ae2b-4bafc86f5ca5; advcake_track_id=5b04f9ec-6336-6b24-3993-023b33dbee4a; advcake_session_id=04bd74b2-bb40-7a30-46cc-a2ffed2546d0; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex; advcake_utm_partner=yandex; advcake_utm_webmaster=; advcake_click_id=; flocktory-uuid=8aad07d3-beef-4f45-a5d1-34a472740c73-1; afUserId=68fb8b44-5059-4a79-9683-23085f3e3690-p; AF_SYNC=1691464647351; flacktory=no; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; bIPs=434929338; _ga=GA1.2.1654867660.1691464636; tmr_detect=1%7C1691465232448; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=c2327dc2-e2f3-43aa-9315-5d5e95c73c97.1691464636.1.1691465307..f977393c-f088-4973-863f-f1c4868ff353..fa914c9b-f381-4743-aa3f-41e3d50fb950.1691464636081.68; gsscgib-w-mvideo=g16o20TG/ursiXeB4yatolBj3o9L9I6rFl4S2MBXBTFHGUuyTI4JG1STkKNGBk2GpLjKbhIolNy98o3aXGlHUDURDHH9bNxIMleHolR1sObG4sEwgRb6RPKTIVz+q/vBzQ3pnhKopQv37N14oPvL+s2lqlA96J3Pk4QHxZ3wV3TxwmehQYO8G5r+NX3m/KrVdfNydc1XUQxKfubbVxapXsNt5my3HAz6Or83b+G4bkTrFuQNGC28XJzPCIcFyCkRWLI=; gsscgib-w-mvideo=g16o20TG/ursiXeB4yatolBj3o9L9I6rFl4S2MBXBTFHGUuyTI4JG1STkKNGBk2GpLjKbhIolNy98o3aXGlHUDURDHH9bNxIMleHolR1sObG4sEwgRb6RPKTIVz+q/vBzQ3pnhKopQv37N14oPvL+s2lqlA96J3Pk4QHxZ3wV3TxwmehQYO8G5r+NX3m/KrVdfNydc1XUQxKfubbVxapXsNt5my3HAz6Or83b+G4bkTrFuQNGC28XJzPCIcFyCkRWLI=; fgsscgib-w-mvideo=qcQ7a5525a2254b3c816cc2c08629c0990587903; fgsscgib-w-mvideo=qcQ7a5525a2254b3c816cc2c08629c0990587903; gssc218=; cfidsgib-w-mvideo=PcpLTmrmIeeZQqSR8V55KNNMRV2RaiEVUK4f0oNHMXrouCY8XSpg/SNtsu9/PGyojiTWLoA9cwH82ABITQFwAuyzdWVttGDRa+0XjLoO99dfqESAVIu2HMETQ795t6rW6i7VqiS/NxGuNGE3ZtfjGpHutbsBt076OVRFjQ==; _ga_CFMZTSS5FM=GS1.1.1691464636.1.1.1691465363.0.0.0; _ga_BNX5WPP3YK=GS1.1.1691464636.1.1.1691465363.20.0.0',
        'referer': 'https://www.mvideo.ru/product-list-page?q=%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82&category=planshety-195',
        'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '72dbbbf3fc2c48448187f7e967e1876b-9ee987ba54c12a0e-1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36',
        'x-set-application-id': 'b623ae15-e7d3-4b58-8ff5-b337841bf2a3',
    }

    params = {
        'productIds': '30065629,30063160,30067583,30065770,30066794,30065628,30064042,30064044,30066792,30064063,400075550,30067813,30067810,30064327,30066790,30064026,30065627,30067460,30067584,30065783,30064028,30064024,30066075,400113927',
    }

    response = requests.get(
        url='https://www.mvideo.ru/bff/product-details/list',
        params=params, cookies=cookies, headers=headers)

    products_ids = response.get('body').get('pr')




def main():
    get_data()


if __name__ == "__main__":
    main()
