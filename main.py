from pyrogram import Client
import time


api_id = 123456 #Заменить на свой api_id
api_hash = "your_api_hash" #Заменить на свой api_hash
app = Client("my_account", api_id, api_hash)

chat_list = open("chat_list.txt", 'r', encoding='utf-8').readlines()
messages = open("messages.txt", 'r', encoding='utf-8').readlines()
interval = 5 #Интервал между отправкой сообщений в разные чаты
cooldown = 1800 #Интервал между сменой сообщения

with app:
    while True:
        for message in messages:
            message = message.split("+")
            for chat in chat_list:
                app.send_message(chat, "\n".join(i.strip() for i in message))
                print(f"Сообщение отправлено в {chat}: {message}")
                time.sleep(interval)
            time.sleep(cooldown)