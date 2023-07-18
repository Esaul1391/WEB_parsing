#     https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import csv
import time
import random

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
# ua = UserAgent
# fake_ua = {'user-agent': ua.random}
# req = requests.get(url)
# req.encoding = 'utf-8'
#
#
# src = req.text
#
#
# # 1  Сохраняю страницу в файл
#
# with open("index.html", "w") as file:
#     file.write(src)

# with open("index.html") as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_ = 'mzr-tc-group-item-href')
#
# all_categorits_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item['href']
#
#     all_categorits_dict[item_text] = item_href
# #
# #
# # 2          Сохраняем в JSON  файл
# #
# with open("all_categorits_dict.json", "w") as file:
#     json.dump(all_categorits_dict, file, indent=4, ensure_ascii=False)

# indent= отступы               ensure_ascii=False Неэкранирует


#   3

with open("all_categorits_dict.json") as file:
    all_categories = json.load(file)


interation_count = int(len((all_categories))) - 1
#    4
count = 0
for category_name, category_href in all_categories.items():

    rep = [',', ' ', '-', "'"]   # Меняю символы на  "_"
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')

    req = requests.get(url=category_href)
    req.encoding = 'utf-8'
    src = req.text
    with open(f"data/{count}_{category_name}.html", "w") as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    alert_block = soup.find(class_='uk-alert uk-alert-danger uk-h1 uk-text-center mzr-block mzr-grid-3-column-margin-top')
    if alert_block is not None:
        continue

    # Собираю заголовки таблицы

    table_head = soup.find(class_ = "uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )


    products_data = soup.find(class_ = "uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find("tbody").find_all("tr")

    product_info = []

    for item in products_data:
        product_tds = item.find_all('td')
        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Интерация {count}. {category_name} записана...")
    interation_count = interation_count - 1

    if interation_count == 0:
        print("Работа законченна")
        break

    print(f"Осталось интераций: {interation_count}")
    time.sleep(random.randrange(2, 4))



