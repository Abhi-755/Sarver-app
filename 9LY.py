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
 
def openlink(msg4):
 
    r = browser.open(msg4)
 
def aclass():
 
    browser.open(url)
 
    browser.select_form(nr = 0)
 
    browser.form['email'] = emailx
 
    browser.form['pass'] = pwx
 
    r = browser.submit()
 
    browser.select_form(nr = 0)
 
    browser.form['name_action_selected'] = ['save_device']
 
    r = browser.submit()
 
    
 
    
 
def poct(comment):
 
    browser.select_form(nr = 0)
 
    browser.form['comment_text'] = comment
 
    r = browser.submit()
 
def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]

		x = """
\033[1;37;1m         
┈▄▄▄██▀▀▀┈┈▄▄▄┈┈┈┈┈┈┈▄████▄┈┈┈██┈▄█▀┈┈┈██████┈┈┈▒█████┈┈┈┈███▄┈┈┈┈█┈ 
┈┈┈▒██┈┈┈┈▒████▄┈┈┈┈▒██▀┈▀█┈┈┈██▄█▒┈┈▒██┈┈┈┈▒┈┈▒██▒┈┈██▒┈┈██┈▀█┈┈┈█┈ 
┈┈┈░██┈┈┈┈▒██┈┈▀█▄┈┈▒▓█┈┈┈┈▄┈▓███▄░┈┈░┈▓██▄┈┈┈┈▒██░┈┈██▒┈▓██┈┈▀█┈██▒ 
▓██▄██▓┈┈┈░██▄▄▄▄██┈▒▓▓▄┈▄██▒▓██┈█▄┈┈┈┈▒┈┈┈██▒┈▒██┈┈┈██░┈▓██▒┈┈▐▌██▒ 
┈▓███▒┈┈┈┈┈▓█┈┈┈▓██▒▒┈▓███▀┈░▒██▒┈█▄┈▒██████▒▒┈░┈████▓▒░┈▒██░┈┈┈▓██░ 
┈▒▓▒▒░┈┈┈┈┈▒▒┈┈┈▓▒█░░┈░▒┈▒┈┈░▒┈▒▒┈▓▒┈▒┈▒▓▒┈▒┈░┈░┈▒░▒░▒░┈┈░┈▒░┈┈┈▒┈▒┈ 
┈▒┈░▒░┈┈┈┈┈┈▒┈┈┈▒▒┈░┈┈░┈┈▒┈┈┈░┈░▒┈▒░┈░┈░▒┈┈░┈░┈┈┈░┈▒┈▒░┈┈░┈░░┈┈┈░┈▒░ 
┈░┈░┈░┈┈┈┈┈┈░┈┈┈▒┈┈┈░┈┈┈┈┈┈┈┈░┈░░┈░┈┈░┈┈░┈┈░┈┈┈░┈░┈░┈▒┈┈┈┈┈┈░┈┈┈░┈░┈ 
┈░┈┈┈░┈┈┈┈┈┈┈┈┈┈░┈┈░░┈░┈┈┈┈┈┈░┈┈░┈┈┈┈┈┈┈┈┈┈░┈┈┈┈┈┈┈░┈░┈┈┈┈┈┈┈┈┈┈┈┈░┈ 
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈░┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ 

\t    \033[1;37m\033[1;41m Author : J9CKS0N XD \033[0m\033[1;37m
\033[1;37;1m-----------------------------------------------
\033[1;37;1m ▶ Author   : JackSon xD
\033[1;37;1m ▶ Team     : JackSon xD
\033[1;37;1m ▶ Facebook :https://www.facebook.com/0WNFIR3.J9CKS0N.XD
\033[1;37;1m ▶ Virson   : 1.2.1
\033[1;37;1m-----------------------------------------------"""
 
emailx=str(input("➣Enter email : "))
 
pwx =str(input("➣Enter pswrd : "))
 
aclass()
 
msg4=str(input("➣Enter post link : "))
 
msg5=str(input("➣enter notpad link : "))
 
f=open(msg5, 'r')
 
lines = f.readlines()
 
f.close()
 
msg6= int(input("➣Enter TIME : "))
 
os.system('clear')
 
sys.stdout.flush()
 
print('kbaad v1.0')
 
count = 0
 
while True:
 
    for line in lines:
 
        if len(line) > 3:
 
            if count != 0:
 
                sleep(msg6)
 
            openlink(msg4)
 
            poct(line)
 
            print('COMMENT GONE - ', line)
 
            count += 1
 
            if count % 10 == 0:
 
                sleep(1)
 
                
 
                
 
                
 
 
