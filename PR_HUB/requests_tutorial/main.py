import requests

response = requests.get('https://cdovgltu.ru/login/index.php')

# print(response.status_code)

# print(response.headers)

print(response.text)