from urllib import response

from tests.parsing import GITSpider

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

# Создаем объект GITSpider и вызываем метод parse для получения результатов
git_spider = GITSpider()
git_spider.parse(response)  # Предполагается, что у вас есть объект response для парсинга

# Получаем результаты и строим сообщение
results = git_spider.get_results()
message = "Результаты тестов: "
for result in results:
    message += f"\n{result}"  # Добавляем каждый результат на новой строке

send_message(token, chat_id, message)






















