import requests

from Functions1 import *

while True:
    new_ts = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
    ts = new_ts['ts']
    long_poll = requests.get('https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                                            act='a_check',
                                                                                            key=key,
                                                                                            ts=ts)).json()
    update = long_poll['updates']
    if update[0][0] == 4 and  update[0][3] != 321056236 and update[0][6] == 'привет' or 'Привет':
        user_id = update[0][3]
        user_name = vk_bot.method('users.get', {'user_ids': user_id})
        write_msg(user_id, 'привет, ' + (user_name[0]['first_name']))
    elif update[0][0] == 4 and  update[0][3] != 321056236 and 'картинк' in update[0][6]:
        write_msg_attach(user_id, None, random.choice(memes_id))
    elif update[0][0] == 4 and  update[0][3] != 321056236 and 'красив' in update[0][6]:
        group_id = -35684707
        post_id = get_last_post(group_id, 1, 1, 'owner')
        attach = 'wall' + str(group_id) + '_' + str(post_id)
        write_msg_attach(user_id, None, attach)