import json
import requests


def main():

    try:
        URL = "http://httpbin.org/status/200"
        response = requests.delete(URL)
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("")

    # offset = 0
    # while True:
    #     # url = 'https://наш.дом.рф/сервисы/api/erz/main/filter'
    #     # params = (
    #     #           ('offset', offset),
    #     #           ('limit', 100),
    #     #           ('sortFiled', 'devShortNm'),
    #     #           ('sortType', 'asc')
    #     #           )
    #     # response = requests.get(url=url, params=params)
    #     # reestr = response.json()
    #
    #
    #
    #     offset += 100



if __name__ == '__main__':
    main()
