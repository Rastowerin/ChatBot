import requests

from Config import *
import vk_api

vkBot = vk_api.VkApi(token=ACCSESS_TOKEN)
response = vkBot.method('users.get', {'user_ids': MY_ID})
print(response)
response = response[0]
print(response)
print(response['first_name'])

response = vkBot.method('users.get', {'users_ids': MY_ID})
print((response[0])['first_name'])

vkBot.method('messages.send', {'user_id': MY_ID, 'message': 'привет', 'random_id': 123})

response = requests.get(API_URL + 'users.get?user_id=' + MY_ID + '&v=5.52&access_token=' + ACCSESS_TOKEN)
print(response.text)
response = requests.get(API_URL + 'users.get', {'user_id': MY_ID, 'v': 5.74, 'access_token': ACCSESS_TOKEN})
print(response.text)

vkBot = vk_api.VkApi(token=ACCSESS_TOKEN)
response = vkBot.method('users.get', {'user_ids': MY_ID})
print(response)
response = requests.get('{url}users.get?users_id = {id}&v = {v}&access_token = {ac_t}'.format(url=API_URL, id=MY_ID, v=5.74,ac_t=ACCSESS_TOKEN))