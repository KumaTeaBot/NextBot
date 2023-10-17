import os


if os.name == 'nt':
    pwd = 'D:\\GitHub\\NextBot'
else:
    pwd = '/home/kuma/bots/rbsk'

url_regex = r'https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|' \
            r'www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|' \
            r'https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|' \
            r'www\.[a-zA-Z0-9]+\.[^\s]{2,}'

cmd_re = r'^/\w+(@\w+)?\s'

gpt_inst = ("You are ChatGPT. "
            "You're in a group chat. "
            "You must reply in their language. "
            "Reply should be short, casual and relaxed. "
            "Be like a friend, not an assistant.")

multiuser_inst = (f'{gpt_inst} '
                  f'Format is "@username: message", '
                  f'your reply must start with "@ChatGPT: ".')


dm_start = (
    'Thank you for using Kuma Next bot!\n'
    'You may see commands sending "/help".'
)
dm_help = (
    '/start: wake me up\n'
    '/help: display this message\n'
    '/ping: check for delay\n'
    '/say: say something\n'
)
unknown_message = "I can't understand your message or command. You may try /help."

gpt_data_dir = os.path.join(pwd, 'data/gpt')
gpt_users_file = os.path.join(gpt_data_dir, 'users.txt')

group_help = (
    '/rp: repeat\n'
    '/title: manage titles\n'
    '`/help poll`: show poll help\n'
    '/ping: check for delay\n'
    '/debug: display debug info\n'
)

gpt_auth_info = (
    '本 bot 由不愿透露姓名的莱姆老师赞助，'
    '你目前还不在名单中，'
    '请等待一位管理员批准申请……'
)
