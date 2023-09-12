import requests


def get_url():
    url = "https://www.ozon.ru/api/composer-api.bx/page/json/v2" \
         "?url=/product/avtomaticheskaya-kofemashina-inhouse-rozhkovaya-coffee-arte-icm1507-seryy-397529235/"
    response = requests.get(url=url)
    print(response.status_code)


def main():
    get_url()

if __name__ == "__main__":
    main()