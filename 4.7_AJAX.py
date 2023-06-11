# AJAX
# AJAX (Asynchronous Javascript and XML) - позволяет обновлять данные на сайте без перезагрузки страницы. Пример:
# вы работаете на сайте, изменяете информацию в текстовых полях, нажимаете на кнопки, обмениваетесь данными с
# сервером, при этом страница ни разу не обновилась, а данные на странице изменялись многократно. Такое поведение
# сайта обеспечивает технология AJAX. Так происходит, потому что AJAX подгружает не всю страницу целиком, а только ее часть.
# На AJAX построено огромное количество сайтов в интернете, вы встречали их неоднократно, просто не знали, что эта технология так называется.
#
# Вызовы AJAX в основном выполняются для API, который возвращает объект JSON, который может быть легко обработан библиотекой requests.
#
# Если перед вами есть кнопка, при нажатии на которую происходит загрузка данных, или это происходит при скроллинге страницы, то перед вами AJAX.
#
# Второй и более точный способ распознать AJAX - это заглянуть в инструменты разработчика и обнаружить в заголовках запроса ключ  'x-requested-with': 'XMLHttpRequest'.
#
# 'x-requested-with': 'XMLHttpRequest' - нестандартный заголовок, при запросах из JavaScript без перезагрузки страницы,  полезен для имитации AJAX.

# Если вы скопируете ссылку, которая находится в левой части на скриншоте выше, вы получите ошибку "Страница bitality.cc не найдена".
# Так происходит потому, что мы совершаем прямой запрос к серверу, где лежат данные, но мы не передаем ключ 'x-requested-with': 'XMLHttpRequest'.
#
# Давайте напишем скрипт и передадим с запросом ключ requested-with': 'XMLHttpRequest' и стандартный юзер-агент.

# import requests
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest'
# }
#
# url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
# response = requests.get(url=url, headers=headers).json()
# print(response)

# Передача параметров с AJAX запросом
# В прошлом уроке мы получали данные о цене с крипто-обменника, делали это по прямой ссылке на паре ETH-BTC.
# Но чаще всего мы хотим получать данные тех криптовалют, которые нас интересуют. Чтобы понять, как это сделать,
# необходимо посмотреть, какие параметры скрипт отправляет на сервер, после чего сделать то же самое.
#
# Посмотрим внимательнее на ссылку, которая возвращает данные в JSON формате.
#
# https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0
#
# Видим, что на сервер передаются 4 параметра:
#
# GiveName - передает имя конвертируемой криптовалюты;
# GetName - передает имя криптовалюты, в которую мы конвертируем GiveName;
# Sum - количество валюты GiveName(ETH), которую хотим предоставить на обмен в валюту GetName(BTC);
# Direction - направление обмена, определяет в какую сторону будет обмен, прямое направление=(0)ETH=>BTC или обратное направление=(1) BTC=>ETH.
# Эти данные понадобятся для того, чтобы сделать наш скрипт более универсальным.
#
# Модифицируем код с прошлого урока и добавим в запрос определенные выше параметры.

# import requests
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }
#
# data = {
#     "GiveName": "Monero",
#     "GetName": "Dash",
#     "Sum": 100,
#     "Direction": 0
# }
#
# url = "https://bitality.cc/Home/GetSum?"
# response = requests.get(url=url, headers=headers, params=data).json()
# print(response)

# >>> {'giveSum': '100', 'getSum': '332.11979261'}
# Добавили словарь data, в котором мы можем хранить и передавать с запросом те данные, которые нас интересуют. Подобный запрос формирует такую ссылку:
#
# https://bitality.cc/Home/GetSum?GiveName=Monero&GetName=Dash&Sum=100&Direction=0
#
# В ответ на этот запрос сервер нам формирует данные в формате JSON => {'giveSum': '100', 'getSum': '332.11979261'}. В таком виде с ними работать намного проще.
#
# Откройте сайт и потренируйтесь находить на этом сайте запросы AJAX, также потренируйтесь формировать данные в словаре data, постарайтесь понять, как формируется такая ссылка.
#
# И напишите в комментариях, если столкнетесь с проблемами при работе с этим сайтом.