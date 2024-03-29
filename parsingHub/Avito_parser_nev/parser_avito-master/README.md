# Avito Parser

Находит объявления на avito.ru по ключевым словам. Присылает уведомления в telegram и сохраняет результат в csv файл.

### Внимание! Настоятельно не рекомендую обновлять Chrome до версии 115. Возможны проблемы

### Обновление, версия 1.08

- Исправлена ошибка при работе с Chrome 115, обновите зависимости. При установке зависимостей используйте виртуальное окружение

### Обновление, версия 1.07

- Исправлены  ошибки касательно минимальной и максимальной цены при запуске без графического интерфейса

#### Добавлено:
 - Новый графический интерфейс, теперь всё стало выглядеть более современно. Спасибо https://github.com/Genone22. Не забудьте обновить зависимости



### Обновление, версия 1.06

#### Исправлены  ошибки:

- Дублирование объявления при отправке в telegram, если Вы нажимали кнопку test 
- Иногда не отправлялись логи в telegram, хотя данные были заполнены и кнопка test работала
- Определение версии установленного браузера теперь переложена на Seleniumbase
- Кодировки

#### Добавлено:

- Переход на Seleniumbase (не забудьте обновить зависимости)
- Ускорена работа
- Улучшена стабильность
- Проверка keywords теперь работает и для названия объявления (ранее проверялось только описание)
- Обнаружение бана по IP со стороны Авито


### Обновление, версия 1.05
 
#### Исправлены  ошибки:

- Ошибка при попытке прочитать описание (selector "[class*='item-description']")
- Дублирование объявления при отправке в telegram
- Иногда не работала кнопка test (тестирование отправки сообщений в telegram) без перезапуска скрипта
- Другие мелкие баги
 #### Добавлено:

- С сайта парсится теперь больше информации:  "Название",
                    "Цена",
                    "Ссылка",
                    "Описание",
                    "Просмотров",
                    "Дата публикации",
                    "Продавец"

- Результат сохраняется в csv файл в папке result (более удобно работать)
- Браузер использует случайный юзер-агент из файла user_agent_pc.txt, можете добавить большее количество самостоятельно (но это необязательно)
- Сильно улучшена стабильность работы
- Оставлена возможность запуска скрипта без графического интерфейса, все настройки задаются в файле settings.ini
- Увеличено максимальное количество уже просмотренных сообщений до 5000 (хранится в файле viewed.txt и очищается автоматически при достижении лимита)
- Увеличено окно вывода результата и переделан сам вывод

### Обновление, версия 1.02

- Исправлены старые ошибки и добавлены новые)
- Добавлено поле минимальная цена, теперь можно указывать верхнюю и нижнюю границу цены
- Исправлен баг, связанный с отсутствием viewed.txt
- Улучшена стабильность работы
- Добавлена возможность запуска скрипта без графического интерфейса, все настройки задаются в файле settings.ini. После
  нужно запустить parser_cls.py, таким образом, удобно запускать скрипт на удаленном сервере

### Обновление, версия 1.01

- Исправлена ошибка когда на страницы нет кнопки "Далее"
- Добавлено поле максимальная цена, теперь можно искать не только бесплатные объявления

## Youtube (как это работает)

Первая версия (создание самого парсера) https://youtu.be/pbzPkZcVOx0

Вторая версия (обзор нововведений: графический интерфейс, уведомления и как это работает) https://youtu.be/OjId94hYWnc

## Установка

Для работы требуется Python 3.5+. Скопируйте проект и установите зависимости:

```bash
  pip install -r requirements.txt
```

У Вас также должен быть установлен браузер Google Chrome любой более менее свежей версии. Скрипт тестировался на версиях
108-112

Запустите **AvitoParser.py**

```bash
  python AvitoParser.py
```

#### Если Вам необходимо получать уведомления о новых объявлениях в telegram:

- Перейдите в диалог с **https://t.me/BotFather**
- Введите команду **/newbot**, придумайте name и username для бота
- Скопируйте token и вставьте в первое поле скрипта
- Перейдите в диалог с Вашим ботом по ссылке из прошлого шага, ссылка имеет формат: **t.me/your_bot**
- Напишите **@get_id_bot** и скопируйте **chat_id** вашего диалога, вставьте его во второе поле данного скрипта
- При нажатии на кнопку Test в скрипте, Вам должно прийти сообщение. Если нет, перезагрузите скрипт и попробуйте еще раз

## Возможности

- Удобное управление с помощью графического интерфейса
- Проверка новых объявлений
- Установка количества проверяемых страниц
- Установка паузы между повторами
- Уведомление в telegram как опция, также результат сохраняется в result/keyword*.json и выводится в окно
- Хранение уже просмотренных объявлений, т.е. дубли игнорируются
- Присылает только объявление, у которых цена = 0, рекламные объявления отсекаются
- Установка слов-ключей, которые должны быть в описании объявления
- Больше не нужно вводить версию Chrome, скрипт сам её определит (работает для Linux и Windows)

### Проблемы

При обнаружении ошибок, ждем в https://github.com/Duff89/parser_avito/issues


### Поддержка развития проекта
Поддержать разработку можно по ссылке: https://yoomoney.ru/to/410014382689862
или 2204 1201 0103 5539


Если понадобятся хорошие прокси для подобных скриптов, рекомендую: https://proxy6.net/?r=54545 (купон для скидки
SdSq8wCwJA)
