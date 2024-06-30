W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

logo =  """\033[1;35;40m     
\033[1;35;40m      
 \033[1;31m█████╗ ██╗   ██╗ █████╗ ███╗   ██╗
\033[1;32m██╔══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║
\033[1;33m███████║ ╚████╔╝ ███████║██╔██╗ ██║
\033[1;34m██╔══██║  ╚██╔╝  ██╔══██║██║╚██╗██║
\033[1;35m██║  ██║   ██║   ██║  ██║██║ ╚████║
\033[1;31m╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;31m__________________________________________  
\033[1;33m -----------------------------------------------
\033[0;91m   OWNER\033[1;39m    : \033[1;32mAYAN D0N
 \033[0;91mFACEBOOK \033[1;39m  : \033[1;32m AYAN NAME SERCH KAR LODE
 \033[0;91mWHATS APP\033[1;39m  : \033[1;32m LAND LELO MERA
 \033[0;91m IF YOU THINK YOUR ARE BAD THEN I AM YOUR DAD
\033[1;33m -----------------------------------------------"""

def menu():
	os.system('clear')
	print(logo)
	print('[1] Random Uid Crack')
	print('[2] Contact To Owner')
	print('[0] Exit')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		md()
	elif opt =='2':
		Contact()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()

def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1m\033[36m", end = "")
    print(47*'\033[1;35;40m-')
    sp("\033[1;37;1m[?] Enter the 2 factor code by google authenticator\n")
    print(47*'\033[1;37;1m-')
    apr = str(input('\033[1;37;1m[?] Enter Code : '))
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
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

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;35;40m",end = "")
    print (e.strftime("Account Ok :: Date - %d/%m/%Y  Time - %I:%M:%S %p"))
    print(">> Chla Gya Tera msg :: ", yyy+ ' ' +line, "\n")

print("\033[1;33;40m", end = "")
os.system('clear')
print(logo)
sp("\033[1m\033[36m[+] Login With Email/Number \n")
print(47*'\033[1;35;40m-')
USERNAME = str(input('[?] Enter Email/Number : '))
print("\033[1;33;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[+] Enter Your Facebook Password\n")
print(47*'\033[1;35;40m-')
PASSWORD = str(input('[?] Enter your password : '))
login()
print("\033[1;34;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Enter Chat/inbox Link\n")
print(47*'\033[1;35;40m-')
cid = str(input('\033[1;37;1m[?] Enter Link : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Enter Notepad File Name\n")
print(47*'\033[1;35;40m-')
np = str(input('\033[1;37;1m[?] Enter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
print("\033[1;34;40m", end = "")
sp('\33[1m'"\nEnter your Haters name :►\n")
yyy= str(input())
print("\033[1;34;40m", end = "")

print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Enter The Time Delay In Seconds\n")
print(47*'\033[1;35;40m-')
t = int(input('\033[1;37;1m[?] Enter Time : '))

os.system('clear')
print(logo)

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(yyy+ ' ' +line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
               
                