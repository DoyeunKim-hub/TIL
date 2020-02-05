from decouple import config
import requests

token = config("TELEGRAM_BOT_TOKEN")
app_url = f'https://api.telegram.org/bot{token}'

set_webhook_url = f'{app_url}/setWebhook?url=https://doyeun1994.pythonanywhere.com/{token}'
                                           # http://127.0.0.1:5000 을 바꾼 것
response = requests.get(set_webhook_url)
print(response)