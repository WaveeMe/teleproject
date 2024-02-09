from pyrogram import Client
from pyrogram.errors import FloodWait
import time
import random

from config import *


app = Client("account", api_id=api_id, api_hash=api_hash, system_version="4.16.30-vxmy_text")


def send_messages():
    with app:
        while True:
            for group in groups:
                try:
                    app.send_message(group, text=text)
                    print(f"Sended to {group}")
                except FloodWait:
                    time.sleep(10)
                    app.send_message(group, text=text)
                    print(f"Sended to {group} with FloodWait Error")
                time.sleep(random.randint(min_sleep, max_sleep))

def check_info():
    print(f"\nГруппы в которые будет рассылка: {groups}\n"
          f"Текст: {text}\n"
          f"Минимальная задержка: {min_sleep}, максимальная {max_sleep}\n")
    
while True:
    command = int(input("1 - Старт\n"
                        "2 - Проверка данных\n"))
    
    if command == 1:
        send_messages()
    if command == 2:
        check_info()


    
