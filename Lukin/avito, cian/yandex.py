import requests


'https://realty.ya.ru/moskva/kupit/kvartira/?priceMin=5000000&priceMax=8000000&roomsTotal=1&roomsTotal=2&roomsTotal=STUDIO&areaMin=30&lastFloor=YES&floorExceptFirst=YES&apartments=NO'


def get_json():
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
        'Referer': 'https://realty.ya.ru/moskva/kupit/kvartira/?priceMin=5000000&priceMax=8000000&roomsTotal=1&roomsTotal=2&roomsTotal=STUDIO&areaMin=30&lastFloor=YES&floorExceptFirst=YES&apartments=NO',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get(
        'https://realty.ya.ru/_crpd/mnfKY5957/219479_G/W0rAX7szyGjU2RNtNsOI75Jwb3aBfvCJQYYFOFPMIkAYZMHsJM7IHoueTPDuzdDuyJjH0e0hXu3UbHGqQ7xtVQgoM5k9VUvLdegD7cNSzP7mhR5HMs1Q',
        headers=headers,
    )
    data = response.texts
    print(data)
def main():
    get_json()

if __name__ == '__main__':
    main()