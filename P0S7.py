from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass

import base64
import json
import time
import sys,os,re,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'   # mode 31 = red forground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE  = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN  = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"
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
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.001)
logo()
testPY()

headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}
			

def comment_on_posts(posts):
	for i in ns:
		try:
			message = i
			url = "https://graph.facebook.com/v14.0/{0}/comments".format(profile_id+"_"+post_id)
			parameters = {'access_token' : access_token, 'message' : message}
			s = requests.post(url, data = parameters, headers=headers)
			tt = time.strftime("%Y-%m-%d %I:%M:%S %p")
			
			if s.ok:
				print(47*'\033[1;37;1m-');print ('[+] Time : \033[1;31;1m',datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'),"\n\033[1;37;1m[+] Your Comments : \033[1;32;1m" +message)
				time.sleep(timm)
			else:
				print(47*'\033[1;37;1m-');print('\033[1;31;1m[x] comments block '+tt,'\n','[×] Token error : id ud gai bhai')
				time.sleep(timm)
		except Exception as e:
			print(e)
			time.sleep(timm)
							   
def get_posts(): 
	try:
		url = "https://m.facebook.com"
	except HTTPError as e:
		print("HTTP Error")
	except URLError as e:
		print("URL Error")
		

if int:
	print("\033[1;37;1m[*] INPUT FACEBOOK TOKEN FILE NAME :)");print(47*'-');token = input("[+] Input Token File Name : \033[1;32;1m")
	with open(token, 'r') as f2:
		access_token = f2.read()
		payload = {'access_token' : access_token}
		a = "https://graph.facebook.com/v14.0/me"
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		if 'name' not in d:
			print(BOLD+RED+'\n\033[1;31;1m[x] Token Invalid ..!!')
			sys.exit()
		b = d['name']
		print(47*'\033[1;37;1m-')
		print('\033[1;37;1m[\033[1;32;1m✓\033[1;37;1m] Your Profile Name : \033[1;32;1m%s'%(b))
		print(47*'\033[1;37;1m-');print('[+] INPUT TARGET PROFILE ID LINK');print(47*'-');profile_id = input("[+] Input Profile Target ID : \033[1;32;1m")
		
		payload = {'access_token' : access_token}
		a = ("https://graph.facebook.com/v14.0/"+profile_id)
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		m = d['name']
		print(47*'\033[1;37;1m-')
		print('\033[1;37;1m[\033[1;32;1m✓\033[1;37;1m] Target Profile Name : \033[1;32;1m%s'%(m))
		print(47*'\033[1;37;1m-');print('\033[1;37;1m[+] NOTE - INPUT TARGET ID POST LINK');print(47*'-')
		post_id = input(BOLD+CYAN+"[+] Post ID Link : \033[1;32;1m")
		
		
		
		print(47*'\033[1;37;1m-');print('[+] NOTE - INPUT GALI WALI FILE NAME');print(47*'-');ms = input(BOLD+CYAN+"[+] Add Gali File Name : \033[1;32;1m")
		print(47*'\033[1;37;1m-');print('[+] NOTE - NO DALO JITNA BAR COMMENTS KARNI HO');print(47*'-');repeat = int(input(BOLD+CYAN+"[+] File Repeat No : \033[1;32;1m"))
		print(47*'\033[1;37;1m-');print('[+] NOTE - COMMENTS KI SPEED DALO');print(47*'-');timm = int(input(BOLD+CYAN+"[+] Input Speed : \033[1;32;1m"))
		os.system('clear');logo();print('\033[1;37;1m[\033[1;32;1m✓\033[1;37;1m] Target Profile Name : \033[1;32;1m%s'%(m))
		print('\033[1;37;1m[\033[1;32;1m✓\033[1;37;1m] Target Post ID Link : \033[1;32;1m%s'%(post_id))
		print(47*'\033[1;37;1m-')
		print('\033[1;37;1m[$] Jackson Ownfire Larkaw')
		ns = open(ms, 'r').readlines()
	for i in range(repeat):
		posts = get_posts()
		comment_on_posts(posts)
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
      