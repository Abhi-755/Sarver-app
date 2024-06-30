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

url = 'https://mbasic.facebook.com/login.php'

def findtextchat(curl):
	r = browser.open(curl)
    
def sendtextconvo(comment):
	browser.select_form(nr = 1)
	browser.form['body'] = comment
	r = browser.submit()
	
	
    
    
print("\033[1;36;40m", end = "")     

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    
    
    
 
    

print ("[---[ TH3 J9CKS0N x'D - :D ]---]")

print ("[---[  J9CKS0N  ]---]")

emailx=str(input("➣Enter email : "))

pwx =str(input("➣Enter pswrd : "))

aclass()

os.system('clear')

sys.stdout.flush()

print("\033[1;33;40m", end = "")

cid = str(input("➣Enter your convo or inbox I'd link : "))
curl = 'https://m.facebook.com/messages/t/' + str(cid)
np1 = str(input("➣Enter Your Name : "))
np = str(input("➣Enter notepad : "))
f = open(np, 'r')
lines = f.readlines()
f.close()
t = int(input("➣Enter TIME : "))

os.system('clear')

sys.stdout.flush()

print("\033[1;34;40m", end = "")

print('J9CKS0N 0N FIIR3')


print ('THIIS T00L IS CR34T3D BY J9CKS0N ', '\n')

count = 0

while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(str(np1) + line)
            e = datetime.datetime.now()
            print("\033[1;32;40m", end = "")
            print(" --> Convo Or Inbox I'd Link  :--", cid)            
            print (e.strftime("--> th3 F9IISU x'D :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))            
            print("--> Message Successfully Sent   :v ::-->> ", np1, line, "\n")
            count += 1
            if count % 10 == 0:
                sleep(1)
