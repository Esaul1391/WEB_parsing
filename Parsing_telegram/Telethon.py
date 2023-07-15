# pip3 install telethon


# from telethon import TelegramClient, events, sync, connection

# from telethon import TelegramClient, events, sync, connection
#
#
# api_id = 20067941 # Тут укажите полученый ранее api
# api_hash = '7180ad59d17a64bba1f9448d0b6a113c' # Тут укажите полученый ранее hash
#
# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
# print(client.get_me())
# client.disconnect()


#   Получаю данные о себе


from telethon import TelegramClient, events, sync, connection


api_id = 20067941 # Тут укажите полученый ранее api
api_hash = '7180ad59d17a64bba1f9448d0b6a113c' # Тут укажите полученый ранее hash

client = TelegramClient('session_name2', api_id, api_hash)
client.start()
print(client.get_me())