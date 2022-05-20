import requests
import time
import random

id_channel_ds = str(input("Введи id сервера: "))
channelID = str(id_channel_ds)
name_file_words = str(input("Введи название файла с сообщениями: "))
with open(str(name_file_words), 'r') as file:
    words = [row.strip() for row in file]
token = str(input("Введи свой токен дискорд: "))
headers = {
    'authorization': token
}
stop_send = int(input("Введи задержку между сообщениями в секундах: "))
while True:
    message = {
        'content': random.choice(words)
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages?limit=50", data = message, headers = headers)
    time.sleep(stop_send)