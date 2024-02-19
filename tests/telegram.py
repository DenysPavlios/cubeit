
import os
import requests

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Используйте значения секретов из переменных окружения
token = os.environ.get('BOT_TOKEN')
chat_id = os.environ.get('CHAT_ID')
message = "Результаты тестов: SUCCESS/FAILURE"

send_message(token, chat_id, message)


