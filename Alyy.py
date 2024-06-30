from urllib import response
import mechanize
import os
from time import sleep
import datetime
import sys
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = https://www.facebook.com/profile.php?id=100093358688045


def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

   
    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()
      
      
      
    r = browser.open(url)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

  
    





def poct(comment):

    browser.select_form(nr = 0)
    print("\033[1;37;40m")
    	
    browser.form['comment_text'] = comment
        
    r = browser.submit()
    
    print("\033[1;37;40m")
    e = datetime.datetime.now()
    print (e.strftime("»» %d/%m/%Y   %I:%M:%S %p"))
logo = ("""\033[97;1m
    
\033[97;1m
▄ ▅ ▆ ▇ █      ☠️𝗙𝗨𝗖𝗞 𝗢𝗙𝗙☠️      █ ▇ ▆ ▅ ▄


\033[95;1m█.------..------..------.\033[93;1m█
\033[94;1m█|A.--. ||L.--. ||Y.--. |\033[99;1m█
\033[98;1m█| (\/) || :/\: || (\/) |\033[91;1m█
\033[96;1m█| :\/: || (__) || :\/: |\033[92;1m█
\033[95;1m█| '--'A|| '--'L|| '--'Y|\033[94;1m█
\033[92;1m█`------'`------'`------'\033[97;1m█
                                                                 

                                       

                                           
[[💻<<———★ 𝗦𝗛𝗢𝗢𝗧𝗘𝗥 ★ ———>>💻]]

\033[94;1m[[💻══|| 𝗖𝗛𝗢𝗗𝗨 𝗡𝗔𝗠𝗘 †══⌨══† 𝗩𝗜𝗥𝗨𝗦 𝗔𝗟𝗬 ||══💻]]

\033[91;1m[[💻═════† 𝗧𝗢𝗢𝗟†════⌨════† 𝗣𝗢𝗦𝗧 💀̂› 𝗪𝗘𝗔𝗣𝗢𝗡 ||═════💻]]
                                                         

    
    
    
    
\033[1;93m""")
os.system('clear')
print(logo)
 
print ("[-[ TH3 T00L CR34T3 BY ALY  ]-]")

emailx=str(input("➣T0K3N ENT3R  : "))

pwx =str(input("➣P9SSW0RD ENT3R : "))

aclass()

msg4=str(input("➣Enter post link : "))

msg5=str(input("➣Enter notpad link : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Enter TIME : "))

os.system('clear')

sys.stdout.flush()

print("\033[1;37;40m")
e = datetime.datetime.now()
print(e.strftime("Start Time = %d/%m/%Y   %I:%M:%S %p"))
print()
count = 0
while True:
    for line in lines:
        if len(line) > 0:
            if count != 0:
            	sleep(msg6)
            openlink(msg4)
            poct(line)
            print("\033[1;33;40m", end = "")
            print('BSDKA COMMENT GAYA - ', line)
            print("\033[1;37;40m")
            count += 1
            if count % 50 == 0:
            	sleep(1)