import requests
import datetime
d = datetime.date.today()
tomm = datetime.datetime.isoweekday(d) + 1

from Functions import *

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
        if 'расписание' in update[0][6]:
            if tomm == 8:
                write_msg(user_id, 'Технология, '
                                   'география, '
                                   'алгебра, '
                                   'физика, '
                                   'химия, '
                                   'физра')
            elif tomm == 2:
                write_msg(user_id, 'Литра, '
                                   'черчение, '
                                   'общество, '
                                   'инглиш, '
                                   'биология, '
                                   'геометрия, '
                                   'кл. час')
            elif tomm == 3:
                write_msg(user_id, 'Русский, '
                                   'инглиш, '
                                   'физра, '
                                   'история, '
                                   'алгебра, '
                                   'химия')
            elif tomm == 4:
                write_msg(user_id, 'Физика, '
                                   'география, '
                                   'русский, '
                                   'инглиш, '
                                   'обж, '
                                   'геометрия')
            elif tomm == 5:
                write_msg(user_id, 'Музыка, '
                                   'изо, '
                                   'инфа, '
                                   'биология, '
                                   'русский, '
                                   'история')
            elif tomm == 6:
                write_msg(user_id, 'Литра, '
                                   'геометрия, '
                                   'физра, '
                                   'история, '
                                   'спб, '
                                   'алгебра')
            elif tomm == 7:
                write_msg(user_id, 'завтра мы не учимся')
