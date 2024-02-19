
import os
import requests
from tests.parsing import GITSpider
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
teleg = GITSpider()

for item in teleg.parse(next(teleg.start_urls)):
    message = f"Результаты тестов: {item}"
    send_message(token, chat_id, message)

# send_message(token, chat_id, message)


