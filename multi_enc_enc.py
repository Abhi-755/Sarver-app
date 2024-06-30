import json
import requests
import time
import os
import sys
import random
from datetime import datetime
os.system('clear')

def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id =str(os.geteuid()) +'→'.join(uuid)+str(os.getlogin())
  try:
    httpCaht = requests.get(f"https://pastebin.com/jWTX5QeL").text
    if id in httpCaht:
      print(f"\033[1;92m YOUR KEY WAS SUCCESSFULLY APPROVED BY OWNER ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      print(f"\x1b[1;92m THIS TOOL NEED APPROVAL TO OWNER❤️ ")
      Nam = input(" WHAT IS YOUR NAME BRO: ")
      tks = 'DEAR%20MAFIYA%20SIR%20MY%20NAME%20IS%20' +Nam + '%20PLEASE%20APPROVED%20MY%20KEY%20AND%20MY%20KEY%20IS%20:%20'+id
      print(f"MR [{Nam}] Your Key Is : {id}")
      print(f" TOOL OWNER MR. MAFIYA")
      print(f"    Send payment to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open https://wa.me/+919971945685?text=' +tks)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
menu_apikey()
def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
   



 /$$      /$$ /$$$$$$$                                                    
| $$$    /$$$| $$__  $$                                                   
| $$$$  /$$$$| $$  \ $$                                                   
| $$ $$/$$ $$| $$$$$$$/                                                   
| $$  $$$| $$| $$__  $$                                                   
| $$\  $ | $$| $$  \ $$                                                   
| $$ \/  | $$| $$  | $$ /$$                                               
|__/     |__/|__/  |__/|__/                                               
                                                                          
                                                                          
                                                                          
             /$$      /$$  /$$$$$$  /$$$$$$$$ /$$$$$$ /$$     /$$ /$$$$$$ 
            | $$$    /$$$ /$$__  $$| $$_____/|_  $$_/|  $$   /$$//$$__  $$
            | $$$$  /$$$$| $$  \ $$| $$        | $$   \  $$ /$$/| $$  \ $$
            | $$ $$/$$ $$| $$$$$$$$| $$$$$     | $$    \  $$$$/ | $$$$$$$$
            | $$  $$$| $$| $$__  $$| $$__/     | $$     \  $$/  | $$__  $$
            | $$\  $ | $$| $$  | $$| $$        | $$      | $$   | $$  | $$
            | $$ \/  | $$| $$  | $$| $$       /$$$$$$    | $$   | $$  | $$
            |__/     |__/|__/  |__/|__/      |______/    |__/   |__/  |__/
                                                                          
                                                                          
                                                                          
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
print('''\033[1;33m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
==================================================
\033[1;37;1m[ 🌝 ] COOKIE TO JSON CONVERTER TOOL MADE BY MAFIYA 
==================================================

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()
print('''\033[1;32m[#] _ KATTAR HINDU == > [ Jai Shree Ram ❤️💪]\n''')
if int:
    print('''\033[1;36m===================================================\n''')
    print('''\033[1;35m-=[ THIS TOOL IS ONLY FOR COOKIE TO JSON CONVERTER  ]=-''')
    print('''\033[1;36m===================================================\n''')
    print('''\033[1;33m-=[ SCRIPT MADE BY MAFIYA X3 PAWAN/]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] SYSTEM STARTED TIME ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ IITX Y0UR D9D == > [ MR. M9FIY9 ]\n''')
    print("\033[1;36;40m", end = "")
# Prompt Password 
import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'M9FIY9' and password == 'M9FIY9':
        print(' \033[0;95mYOUR USERNAME ND PASSWORD ARE CORRECT.')
        os.system('espeak -a 300 " WELCOME,  TO,  MR,  MAFIYA,  COOKIE, CONVERTER,  TOOL "')
        break
    else:
        print(' YOUR USERNAME OR PASSWORD INCORRECT... TRY AGAIN..!! ')
        os.system('espeak -a 300 " INCORRECT,  PASSWORD,  PLEASE,  TRY,  AGAIN..."')
        Name = input("ENTER YOUR NAME BRO: ")
        tks = ('Hello%20Sir%20I%20AM%20' + Name + '%20Please%20Send%20Me%20Your%20Tool%20Password%20')
        os.system("am start https://wa.me/+919971945685?text="+tks)
        attemps += 1
        continue
os.system('clear')
pass
os.system('clear')
logo()
cookie_string = input('Paste your cookies here: ')

print('')
print('')
print('-------------------------------------------------')

cookie_list = cookie_string.split('; ')
cookies_dict = {}

for cookie in cookie_list:
    key, value = cookie.strip().split('=')
    cookies_dict[key] = value

cookies_json = json.dumps(cookies_dict, indent=2)

print('\x1b[32m' + cookies_json)