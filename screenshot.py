import time
from bs4 import BeautifulSoup
import requests
token = "5353002254:AAEKDwHpqsfUJWuF1JIPJysWvXcLHfvyeuE"
url = "https://api.telegram.org/bot5353002254:AAEKDwHpqsfUJWuF1JIPJysWvXcLHfvyeuE/getUpdates"
chat_id = -671906770
message_url = "https://api.telegram.org/bot5353002254:AAEKDwHpqsfUJWuF1JIPJysWvXcLHfvyeuE/sendMessage?chat_id=-671906770&{text}"
proxies = {"https":"https://170.155.5.235:8080"}


def send_message(message):

    res = requests.get("https://api.telegram.org/bot5353002254:AAEKDwHpqsfUJWuF1JIPJysWvXcLHfvyeuE/sendMessage?chat_id=-671906770&text=\U0001F7E5".format(message))
    return res
# {"ok":true,"result":[{"update_id":234330700,
# "message":{"message_id":4,"from":{"id":1250630188,"is_bot":false,"first_name":"Muhammad Ammar","last_name":"Tanweer","username":"Ammar7370"},"chat":{"id":-671906770,"title":"Soccer \u26bd updates","type":"group","all_members_are_administrators":true},"date":1649938593,"text":"/my_id @Soccorfnbot","entities":[{"offset":0,"length":6,"type":"bot_command"},{"offset":7,"length":12,"type":"mention"}]}}]}
# a = send_message("This is testing message")
# print(a)
print()
print("\U0001f600")
print("\U0001F7E5")
print("🟥")
print("https://api.telegram.org/bot5353002254:AAEKDwHpqsfUJWuF1JIPJysWvXcLHfvyeuE/sendMessage?chat_id=-671906770&text=\U0001F7E5")