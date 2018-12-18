import requests

from Functions import *

while True:
    new_ts = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
    ts = new_ts['ts']
    long_poll = requests.get('https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                                            act='a_check',
                                                                                            key=key,
                                                                                            ts=ts)).json()
   
    update = long_poll['updates']
    #if update[0][0] == 4 and update[0][6] == 'привет' or 'Привет':
    #    print('1')
    #    user_id = update[0][3]
    #    user_name = vk_bot.method('users.get', {'user_ids': user_id})
    #    write_msg(user_id, 'привет, ' + (user_name[0]['first_name']))
    if update[0][0] == 4 and  update[0][3] == 321056236 and '!дз' in update[0][6] and update[0][6] != '!дз':
        school_subject = update[0][6].split(':')[1]
        print(school_subject)
        str(school_subject)
        if str(school_subject) in homework:
            print(1)
            homework[school_subject] = update[0][6].split(':')
            print(homework[school_subject])