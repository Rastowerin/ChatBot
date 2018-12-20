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

    if update[0][0] == 4 and '!дз' in update[0][6] and '!!дз' not in update[0][6] and update[0][6] != '!дз':
        subject = update[0][6].split(': ')[1]
        if '%s' % subject in homework:
            write_msg(update[0][3], homework['%s' % subject])
    elif update[0][0] == 4 and  update[0][3] == 321056236 and '!!дз' in update[0][6] and update[0][6] != '!!дз':
        subject = update[0][6].split(': ')[1]
        print(subject)
        if '%s' % subject in homework:
            homework['%s' % subject] = update[0][6].split(': ')[2]
            print(homework['%s' % subject])