import requests
import json

def gert_data():
    url = "https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=1"

    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    r = requests.get(url=url, headers=headers)


    # with open("index.html", "w") as file:
    #     file.write(r.text)

    # print(r.json())
    with open ("r.json", "w") as file:
        json.dump(r.json(), file, indent=4, ensure_ascii=False)

    page_count = r.json()["pageCount"]

    for page in range(1, page_count + 1):
        url = f"https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1={page}"

        r = requests.get(url=url, headers=headers)
        data = r.json()
        items = data["items"]


        for item in items:
            item_name = item["name"]
            ite




def main():
    gert_data()

if __name__ == '__main__':
    main()