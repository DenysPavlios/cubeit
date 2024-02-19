


import requests

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

token = "6990056464:AAHTNehh0TSIU7TrDx-3ubikJJ_ucoDDQnQ"
chat_id = "679677453"
message = "Результаты тестов: SUCCESS/FAILURE"

send_message(token, chat_id, message)
