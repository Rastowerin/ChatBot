import vk_api
import random
from Config import *

vk_bot = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
memes_id = vk_bot.method('photos.get', {'owner_id': -66138380, 'album_id': '255161524'})
meme_id = 'https://vk.com/photo' + memes_id['items']['owner_id'] + '_' + memes_id['items'][random.randint(0, memes_id['count'])]
vk_bot_user = vk_api.VkApi(token=ACCESS_TOKEN)
print('готов к работе')
print(meme_id)


def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})


def write_msg_attach(user_id, text, att_url):
    vk_bot.method('messages.send',
                  {'user_id': user_id, 'attachment': att_url, 'message': text, 'random_id': random.randint(0, 1000)})


def get_last_post(owner_id, count, offset, filter):
    response = vk_bot_user.method('wall.get', {'owner_id': owner_id, 'count': count, 'offset': offset, 'filter': filter})
    return response['items'][0]['id']
