import os
import requests
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:

    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN35')
        self.bot_chat_id = os.getenv('BOT_CHAT_35_ID')
        self.bot_endpoint = 'https://api.telegram.org/bot'

    def send_sms(self, message):
        send_sms = self.bot_endpoint + self.bot_token + '/sendMessage?chat_id=' + self.bot_chat_id + '&parse_mode=Markdown&text=' + message
        bot_response = requests.get(send_sms)
        bot_response.raise_for_status()