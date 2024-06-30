from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
from bs4 import BeautifulSoup

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
logo =  """\033[1;39;40m     
\033[1;39;40m      
──╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗╔═╗─╔╗ 
──║║║╔═╗║║╔═╗║║║║╔╝║╔═╗║║╔═╗║║║╚╗║║ 
──║║║║─║║║║─╚╝║╚╝╝─║╚══╗║║─║║║╔╗╚╝║ 
╔╗║║║╚═╝║║║─╔╗║╔╗║─╚══╗║║║─║║║║╚╗║║ 
║╚╝║║╔═╗║║╚═╝║║║║╚╗║╚═╝║║╚═╝║║║─║║║ 
╚══╝╚╝─╚╝╚═══╝╚╝╚═╝╚═══╝╚═══╝╚╝─╚═╝ 

                              
\033[0;91m 
╔══╗─╔═══╗╔═══╗╔═╗─╔╗╔═══╗ 
║╔╗║─║╔═╗║║╔═╗║║║╚╗║║╚╗╔╗║ 
║╚╝╚╗║╚═╝║║║─║║║╔╗╚╝║─║║║║ 
║╔═╗║║╔╗╔╝║╚═╝║║║╚╗║║─║║║║ 
║╚═╝║║║║╚╗║╔═╗║║║─║║║╔╝╚╝║ 
╚═══╝╚╝╚═╝╚╝─╚╝╚╝─╚═╝╚═══╝ 


 > \033[0;92mDEVELOPER     : J4CKS0N BR4ND
 > \033[0;95mFACEBOOK ID   : https://www.facebook.com/muhammad.khudaji
 > \033[0;41mWHATSAPP      : +923023767433
 \033[0;96m> JIG3RX       : J4CKS0N X ST4RC X M4RCUS <3
 > \033[0;97mWARNING       : DONT USE FOR ILLEGAL WORK     
\033[1;32m---------J4CKS0N X M4RCUS X ST4RC 0WNFIR3--------
"""
        
        
def login():
    response = browser.open(url)
    soup = BeautifulSoup(response, 'html.parser')
    
    if soup.find('input', {'name': 'approvals_code'}):
        print("\Your account is stuck on verification\Please do it and then re-run the program.")
        exit(1)
    elif soup.find('input', {'name': 'submit[This was me]'}):
        print("\Facebook wants to review your recent actions.\Please fix that and then re-run the program.")
        exit(1)
    elif soup.find('input', {'name': 'submit[This was not me]'}):
        print("\Your account got locked, recover it kindly and re-run the script.")
        exit(1)
    else:
        browser.select_form(nr=0)
        browser.form['email'] = USERNAME
        browser.form['pass'] = PASSWORD
        r = browser.submit()
        f = open("login.html", "wb")
        f.write(r.read())
        f.close()

def findtextchat(curl):
    while True:
        try:
            r = browser.open(curl)
            x = browser.title()
            if x == "Review recent login":
                print("\Facebook wants to review your recent actions.\Please fix that and then re-run the program.")
                exit(1)
            if x == "Login approval needed":
                print("\Your account is stuck on verification\Please do it and then re-run the program.")
                exit(1)
            if x == "Epsilon":
                print("\Your account got locked, recover it kindly and re-run the script.")
                exit(1)
            break
        except mechanize.URLError as e:
            print("Error connecting to the server:", str(e))
            print("Retrying in 10 seconds...")
            sleep(10)

def poct(comment):
    try:
        browser.select_form(nr=1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occurred while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occurred while filling text, please check your account")
        exit(1)
    try:
        r = browser.submit()
        e = datetime.datetime.now()
        print(e.strftime("MSG SENDING :: Date - %d/%m/%Y   Time - %I:%M:%S %p"))
        print(">MSG SEND :: ", yyy+ ' ' +line, "\n")
        print(47*'\033[1;35;40m-')
    except Exception as e:
        print("Error sending message:", str(e))
        print(47*'\033[1;35;40m-')

os.system('clear')
sys.stdout.flush()
print(logo)

print(47*'\033[1;35;40m-')
print("Enter Your Email / Number");
print(47*'\033[1;35;40m-')
USERNAME = str(input('Enter Email - Number :'))
print(47*'\033[1;35;40m-')
print("Enter Your  Facebook Password")
print(47*'\033[1;35;40m-')
PASSWORD = str(input('Enter Your Password:'))
login()
print(47*'\033[1;35;40m-')
print(47*'\033[1;35;40m-')
print(" Enter Post Link")
print(47*'\033[1;35;40m-')
cid = str(input('Enter Link : '))
print(47*'\033[1;35;40m-')
print(47*'\033[1;35;40m-')
print('Enter Notepad File Name :')
print(47*'\033[1;35;40m-')
np = str(input('Enter Notepad Link :'))
print(47*'\033[1;35;40m-')
f = open(np, 'r')
lines = f.readlines()
f.close()
print(47*'\033[1;35;40m-')
print("Enter Your Haters Name")
yyy= str(input('Haters Name :'))
print(47*'\033[1;35;40m-')
print(47*'\033[1;35;40m-')
print("Enter the delay time in second")
print(47*'\033[1;35;40m-')
t = int(input('Enter Seconds :'))
print(47*'\033[1;35;40m-')

clear()
print(logo)

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            try:
                findpoct(curl)
                sendtextpoct(yyy+ ' ' +line)
                count += 1
                if count % 10 == 0:
                    sleep(1)
                    clear()
                    print(47*'\033[1;35;40m-')
            except mechanize.URLError as e:
                print("Error connecting to the server:", str(e))
                print("Retrying in 10 seconds...")
                sleep(10)
                continue