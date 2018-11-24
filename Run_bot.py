import requests

from Config import *
import vk_api

vkBot = vk_api.VkApi(token=ACCSESS_TOKEN)
response = vkBot.method('users.get', {'user_ids': MY_ID})

vkBot.method('messages.send', {'user_id': MY_ID, 'message': 'привет', 'random_id': 123})
response = requests.get(API_URL + 'users.get?user_id=' + MY_ID + '&v=5.52&access_token=' + ACCSESS_TOKEN)
print(response.text)
response = requests.get(API_URL + 'users.get', {'user_id': MY_ID, 'v': 5.74, 'access_token': ACCSESS_TOKEN})
print(response.text)