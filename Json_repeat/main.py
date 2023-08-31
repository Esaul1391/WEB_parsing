# import json
#
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
#
# json_data = json.dump(data)            # сериализуем словарь data в json строку
#
# print(type(json_data))
# print(json_data)






import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

with open('countries.json', 'w') as file:
    json.dump(data, file)