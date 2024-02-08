from pyrogram import Client
import time
import random

api_id = 11961648
api_hash = "dfbfb5b6c1978efc9a3ab9350e80a303"

app = Client("account", api_id=api_id, api_hash=api_hash, system_version="4.16.30-vxmy_text")

groups = ["@nablokestore_chat", "@ua_store_chat", "@dizmoral_chat"]
text = "Дам тутор + данные для добавления ссылки в тикток аккаунт. Любое кол-во подписчиков . Данные многоразовые , то есть вы можете купив 1 раз использовать их БЕСКОНЕЧНО. Цена 35грн , писать в лс, бан - реакция"

def send_messages():
    with app:
        while True:
            for group in groups:

                app.send_photo(group, "photo2.jpg", caption=text)
                print(f"Sended to {group}")
                time.sleep(random.randint(30, 55))


while True:
    command = int(input("1 - Старт\n"))
    if command == 1:
        send_messages()


    
